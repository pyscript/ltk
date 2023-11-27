import ltk
from polyscript import xworker # type: ignore

ltk.find("#fan").append("Worker is running...")

def handle_message(sender, topic, data):
    ltk.find("#fan").append(f"Worker fan: {data}")

subscribe = xworker.sync.subscribe
publish = xworker.sync.publish
xworker.sync.handler = handle_message

subscribe("Worker-Fan", "message", "remote_fan")