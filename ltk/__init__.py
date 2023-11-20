# LTK - Copyrights Reserved 2023 - chrislaffra.com - See LICENSE 

import sys

def fix_time():
    import time

    if not hasattr(time, "time"):
        class MonkeyPatchedTimeModuleForMicroPython:
            """ Monkey patch for time.time() for MicroPython """
            pass

        clone = MonkeyPatchedTimeModuleForMicroPython()
        for key in dir(time):
            setattr(clone, key, getattr(time, key))
        setattr(clone, "time", lambda: time.ticks_ms() / 1000)
        sys.modules["time"] = clone

fix_time()

from ltk.jquery import *
from ltk.widgets import *

inject_script("ltk/ltk.js")
inject_css("ltk/ltk.css")

from ltk.jquery import time