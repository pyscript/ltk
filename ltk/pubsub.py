import logging
import pyodide # type: ignore
import json

from pyscript import window # type: ignore

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


class DocumentPubSub():
    subscribers = []

    def __init__(self):
        self.pubsub = window.document.createElement("pubsub")
        window.document.body.appendChild(self.pubsub)
        config = window.eval("_={ attributes: true, childList: false, subtree: false };")
        callback = pyodide.ffi.create_proxy(lambda mutations, observer: self._process_queue())
        observer = window.MutationObserver.new(callback)
        observer.observe(self.pubsub, config)

    def _process_queue(self):
        for message in self.pubsub.children:
            sender, sender_topic, data = json.loads(message.innerText)
            for subscriber in self.subscribers:
                self._match(
                    sender, sender_topic, data,
                    *subscriber
                )
                message.remove()

    def _match(self, sender, sender_topic, data, receiver, receiver_topic, handler):
        if sender_topic == receiver_topic and sender != receiver:
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


_messenger = DocumentPubSub()
subscribe = _messenger.subscribe
publish = _messenger.publish
