import ltk
from polyscript import xworker # type: ignore

ltk.find("#fan").append("Worker is running...")

subscribe = xworker.sync.subscribe
publish = xworker.sync.publish

def handle_message(message):
    ltk.find("#fan").append(message)

subscribe("Worker-Fan", "message", handle_message)