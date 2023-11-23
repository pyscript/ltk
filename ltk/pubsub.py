import logging
import ltk
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

logger = logging.getLogger('root')
subscribers = []
ui_singleton = None


class Component(ltk.VBox):
    classes = [ "ltk-pubsub-component ltk-vbox" ]

    def __init__(self, name):
        self.title = ltk.Text(name).addClass("ltk-pubsub-component-title")
        self.line = ltk.Div().addClass("ltk-pubsub-component-line")
        ltk.VBox.__init__(self, self.title, self.line)

class Call(ltk.Div):
    classes = [ "ltk-pubsub-call" ]

    def __init__(self, sender, receiver, topic, data):
        ltk.Div.__init__(self)
        count = sender.parent().find(".ltk-pubsub-call").length
        self.css("width", abs(sender.title.position().left - receiver.title.position().left))
        self.css("left", round(sender.title.position().left + sender.title.width() / 2 + 8))
        self.css("top", round(sender.title.position().top + sender.title.height() * 2 + 26 + count * 32))
        Dot(self, topic, data)

class Dot(ltk.Div):
    classes = [ "ltk-pubsub-dot" ]

    def __init__(self, line, topic, data):
        ltk.Div.__init__(
            self,
            ltk.Div(f"{topic}: {data}").addClass("label"),
        )
        line.append(self.element)
        self.element.animate(ltk.to_js({ "left": line.width() - 5 }), 2000)


class PubSubUI(ltk.HBox):
    classes = [ "ltk-pubsub-ui ltk-hbox" ]
    components = {}

    def __init__(self):
        global ui_singleton
        ltk.HBox.__init__(self)
        self.element.attr("id", "ltk-pubsub-ui")
        self.element.resizable(ltk.to_js({ "handles": "e" }))
        ui_singleton = self

    def log(self, sender_name, receiver_name, topic, data):
        self.element.css("width", "100%")
        self.element.prependTo(ltk.find(".ltk-log-list").children().eq(0))
        sender = self.get_component(sender_name)
        receiver = self.get_component(receiver_name)
        self.append(Call(sender, receiver, topic, data).element)

    def get_component(self, name):
        if not name in self.components:
            component = Component(name)
            self.components[name] = component
            component.appendTo(self.element)
        return self.components[name]



def setup_document_pubsub():
    ltk.find("body").append(ltk.create("<div>").attr("id", "pubsub"))
    ltk.find("#pubsub")[0].addEventListener("DOMNodeInserted", pyodide.ffi.create_proxy(handle_queue))


def handle_queue(*args):
    print("handle queue")
    for child in ltk.find_list("#pubsub message"):
        message =  json.loads(child.text())
        sender, sender_topic, data = message
        for subscriber in subscribers:
            receiver, receiver_topic, handler = subscriber
            if sender_topic == receiver_topic and sender != receiver:
                if ui_singleton:
                    ui_singleton.log(
                        sender,
                        receiver,
                        sender_topic,
                        data,
                    )
                handler(data)
                child.remove()


def subscribe(name, topic, handler):
    subscribers.append((name, topic, handler))
    handle_queue()


def publish(name, topic, data):
    print("pubsub: publish", name, topic, data)
    ltk.find("#pubsub").append(
        ltk.create("<message>")
            .text(json.dumps((name, topic, data)))
    )

setup_document_pubsub()