# LTK - Copyright 2023 - All Rights Reserved - chrislaffra.com - See LICENSE 

import json
import logging
import pyodide # type: ignore
from pyscript import window # type: ignore

"""

Implements a publish-subscribe facility.

Note this is a standalone module, not importing anything from LTK.
This allows its use in Workers, which may not want to include any UIs.

A receiver registers for events using "subscribe".
A sender broadcasts events using "publish".

Communication between the main UI and workers is done using the DOM.

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


class _DocumentPubSub():
    subscribers = []

    def __init__(self):
        self.pubsub = self.get_pubsub()
        config = window.eval("_={ attributes: true, childList: true, subtree: true };")
        callback = pyodide.ffi.create_proxy(lambda *args: self._process_queue())
        observer = window.MutationObserver.new(callback)
        observer.observe(self.pubsub, config)

    def get_pubsub(self):
        element = window.document.getElementById("pubsub")
        if not element:
            element = window.document.createElement("div")
            element.id = "pubsub"
            window.document.body.appendChild(element)
        return element

    def _process_queue(self):
        for message in self.pubsub.children:
            sender, sender_topic, data = json.loads(message.innerText)
            for subscriber in self.subscribers:
                self._match(message, sender, sender_topic, data, *subscriber)

    def _match(self, message, sender, sender_topic, data, receiver, receiver_topic, handler):
        if sender_topic == receiver_topic and sender != receiver:
            message.remove()
            try:
                handler(data)
                _logger.info(f"[Pubsub] {json.dumps([sender, receiver, sender_topic, data])}")
            except Exception as e:
                _logger.error(f"Pubsub could not handle message: {e}")

    def subscribe(self, name, topic, handler):
        self.subscribers.append((name, topic, handler))
        self._process_queue()
 
    def publish(self, name, topic, data):
        message = window.document.createElement("message")
        message.innerText = json.dumps((name, topic, data))
        self.pubsub.appendChild(message)
        self._process_queue()


_messenger = _DocumentPubSub()

subscribe = _messenger.subscribe
publish = _messenger.publish
