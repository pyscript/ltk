# LTK - Copyright 2023 - All Rights Reserved - chrislaffra.com - See LICENSE 

import json
import logging
import sys
import time

"""

Implements a publish-subscribe facility.

Note this is a standalone module, not importing anything from LTK.
This allows its use in Workers, which may not want to include any UIs.

A receiver registers for events using "subscribe".
A sender broadcasts events using "publish".

Communication between the main UI and workers is done using the worker sync.

"""

__all__ = [
    "TOPIC_CRITICAL", "TOPIC_INFO", "TOPIC_DEBUG", "TOPIC_ERROR", "TOPIC_WARNING", "TOPIC_CRITICAL",
    "TOPIC_REQUEST", "TOPIC_RESPONSE", "TOPIC_WORKER_RUN", "TOPIC_WORKER_RESULT",
    "publish", "subscribe",
]

TOPIC_INFO = "log.info"
TOPIC_DEBUG = "log.debug"
TOPIC_ERROR = "log.error"
TOPIC_WARNING = "log.warning"
TOPIC_CRITICAL = "log.critical"

TOPIC_REQUEST = "app.request"
TOPIC_RESPONSE = "app.response"
TOPIC_WORKER_RUN = "worker.run"
TOPIC_WORKER_RESULT = "worker.result"

_logger = logging.getLogger('root')
_log_topics = {
    "log.info": _logger.info,
    "log.debug": _logger.debug,
    "log.error": _logger.error,
    "log.warning": _logger.warning,
    "log.critical": _logger.critical,
}

_name = "pubsub_mpy" if "MicroPython" in sys.version else "pubsub_py"

start = time.time()

class _Message():
    def __init__(self, sender, receiver, topic, data):
        self.sender = sender
        self.receiver = receiver
        self.topic = topic
        self.data = data

class _PubSub():
    def __init__(self):
        self.subscribers = []
        self.queue = {}
   
    def match(self, message, receiver, receiver_topic, handler):
        if message.topic == receiver_topic and message.sender != receiver:
            try:
                handler(message.data)
                log = _log_topics.get(message.topic, _logger.info)
                log(f"[Pubsub] {json.dumps(['handle', message.sender, receiver, message.topic, str(message.data)])}")
            except Exception as e:
                try:
                    import traceback
                    traceback.print_exc()
                except:
                    print("no traceback", _name)
                    pass
                _logger.error(f"Pubsub could not handle message: {e} {message.sender} {receiver} {message.topic} data={message.data}")
            return True

    def process_queue(self):
        for key, message in list(self.queue.items()):
            for subscriber in self.subscribers:
                if self.match(message, *subscriber):
                    self.remove_from_queue(key)

    def add_to_queue(self, message):
        self.queue[f"{_name}-{time.time()}"] = message

    def remove_from_queue(self, key):
        del self.queue[key]

    def publish(self, sender, receiver, topic, data):
        self.add_to_queue(_Message(sender, receiver, topic, data))
        _logger.info(f"[Pubsub] {json.dumps(['publish', sender, receiver, topic, str(data)])}")
        self.process_queue()

    def subscribe(self, name, topic, handler):
        self.subscribers.append([name, topic, handler])
        self.process_queue()



try:
    from polyscript import xworker
    print("PUBSUB: setup xworker", xworker)
    subscribe = xworker.sync.subscribe
    publish = xworker.sync.publish
except:
    print("PUBSUB: setup main")
    _messenger = _PubSub()

    subscribe = _messenger.subscribe
    publish = _messenger.publish

    def register_worker(worker):
        _workers.append(worker)
        worker.sync.publish = publish
        worker.sync.subscribe = subscribe

    