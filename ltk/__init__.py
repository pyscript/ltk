# LTK - Copyrights Reserved 2023 - chrislaffra.com - See LICENSE 

from ltk.jquery import *
inject_script("ltk/ltk.js")
inject_css("ltk/ltk.css")

from pyscript import window # type: ignore

def fix_time():
    import time
    import sys

    if not hasattr(time, "time"):
        class MonkeyPatchedTimeModuleForMicroPython: pass
        clone = MonkeyPatchedTimeModuleForMicroPython()
        for key in dir(time):
            setattr(clone, key, getattr(time, key))
        setattr(clone, "time", lambda: window.Date.new().getTime() / 1000)
        sys.modules["time"] = clone

fix_time()

from ltk.widgets import *
from ltk.pubsub import publish
from ltk.pubsub import subscribe
from ltk.pubsub import TOPIC_CRITICAL
from ltk.pubsub import TOPIC_INFO
from ltk.pubsub import TOPIC_DEBUG
from ltk.pubsub import TOPIC_ERROR
from ltk.pubsub import TOPIC_WARNING
from ltk.pubsub import TOPIC_CRITICAL
from ltk.pubsub import TOPIC_REQUEST
from ltk.pubsub import TOPIC_RESPONSE
from ltk.pubsub import TOPIC_WORKER_RUN
from ltk.pubsub import TOPIC_WORKER_RESULT
from ltk.logger import *
from ltk.jquery import time