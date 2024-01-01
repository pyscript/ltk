# LTK - Copyright 2023 - All Rights Reserved - chrislaffra.com - See LICENSE 

import json
import pyodide # type: ignore
from pyscript import document # type: ignore
from pyscript import window # type: ignore
import os
import time
import sys

__all__ = [
    "jQuery", "parse_int", "parse_float", "local_storage", "find", "create", "find_list", "to_js",
    "to_py", "schedule", "repeat", "get", "delete", "get_time", "post", "async_proxy", "observe",
    "proxy", "get_url_parameter", "set_url_parameter", "push_state", "inject_script", "inject_css",
    "callback",
]
    
def is_micro_python():
    return not hasattr(time, "time")

def _fix_time_on_micropython():
    if is_micro_python():
        class MonkeyPatchedTimeModuleForMicroPython:
            pass
        clone = MonkeyPatchedTimeModuleForMicroPython()
        for key in dir(time):
            setattr(clone, key, getattr(time, key))
        setattr(clone, "time", lambda: window.Date.new().getTime() / 1000)
        sys.modules["time"] = clone


jQuery = window.jQuery
find = jQuery
create = jQuery
parse_int = window.parseInt
parse_float = window.parseFloat
local_storage = window.localStorage
timers = {}

KB = 1024
MB = KB * KB
GB = MB * MB


def toHuman(byteCount):
    if byteCount > GB: return f"{round(byteCount / GB)}GB"
    if byteCount > MB: return f"{round(byteCount / MB)}MB"
    if byteCount > KB: return f"{round(byteCount / KB)}KB"
    return f"{byteCount} bytes"


def callback(function):
    def inner(*args, **argv):
        return function(*args, **argv)
    return proxy(inner)


def get_time():
    return window.get_time() / 1000


def find_list(selector):
    elements = jQuery(selector)
    return [ elements.eq(n) for n in range(elements.length) ]


def to_js(python_object):
    if python_object.__class__.__name__ == "jsobj":
        return python_object
    return window.to_js(json.dumps(python_object))


def to_py(jsobj):
    try:
        return jsobj.to_py()
    except:
        try:
            return json.loads(window.to_py(jsobj)) # Micropython has no built-in to_py
        except:
            return str(jsobj)


def schedule(python_function, key, timeout_seconds=0.1):
    if not python_function:
        raise ValueError(f"schedule: Expecting a function, not {python_function}")
    if key in timers:
        window.clearTimeout(timers[key])
    timers[key] = window.setTimeout(proxy(python_function), int(timeout_seconds * 1000))


def repeat(python_function, timeout_seconds=1):
    window.setInterval(proxy(python_function), int(timeout_seconds * 1000))


def get(url, handler, kind="json"):
    start = get_time()
    @callback
    def success(response, *rest):
        data = response if isinstance(response, str) else to_py(response)
        size = len(response) if data is response else len(json.dumps(data))
        window.console.log("[Network] GET OK", f"{get_time() - start:.2f}", toHuman(size), url)
        handler(data)
    @callback
    def error(jqXHR, textStatus, errorThrown):
        window.console.error("[Network] GET ERROR", f"{get_time() - start:.2f}", jqXHR.status, repr(errorThrown), url)
        return handler(f'{{"Error": "{errorThrown}"}}')
    window.ltk_get(url, success, kind, error)


def delete(url, handler):
    wrapper = proxy(lambda data, *rest: handler(to_py(data)))
    def error(jqXHR, textStatus, errorThrown):
        window.console.error("[Network] DELETE ERROR", jqXHR.status, repr(errorThrown), url)
    return window.ajax(url, "DELETE", wrapper).fail(proxy(error))


def post(url, payload, handler, kind="json"):
    start = get_time()
    if "?" in url:
        index = url.index("?")
        url = f"{url[:index]}?_=p&{url[index:]}"
    payload = window.encodeURIComponent(json.dumps(payload))
    @callback
    def success(response, *rest):
        data = response if isinstance(response, str) else to_py(response)
        response_size = len(response) if data is response else len(json.dumps(data))
        size = f"{toHuman(len(payload))}/{toHuman(response_size)}"
        window.console.log("[Network] POST OK", f"{get_time() - start:.2f}", size, url)
        return handler(data)
    @callback
    def error(jqXHR, textStatus, errorThrown):
        window.console.error("[Network] POST ERROR", f"{get_time() - start:.2f}", jqXHR.status, repr(errorThrown), url)
        return handler(f'{{"Error": "{errorThrown}"}}')
    window.ltk_post(url, payload, success, kind, error)


def async_proxy(function):
    async def call_function(*args):
        return await function(*args)
    return pyodide.ffi.create_proxy(call_function)


def observe(element, handler):
    config = window.eval("_={ attributes: true, childList: true, subtree: true };")
    callback = pyodide.ffi.create_proxy(lambda *args: handler(element))
    observer = window.MutationObserver.new(callback)
    observer.observe(element[0], config)


def proxy(function):
    if not function:
        return None
    return pyodide.ffi.create_proxy(function) if not is_micro_python() else function


def get_url_parameter(key):
    return window.URLSearchParams.new(window.document.location.search).get(key)


def set_url_parameter(key, value, reload=True):
    search = window.URLSearchParams.new(window.location.search)
    search.set(key, value)
    url = f"{window.location.href.split('?')[0]}?{search.toString()}"
    if reload:
        window.document.location = url
    else:
        push_state(url)


def push_state(url):
    window.history.pushState(None, "", url)


def inject_script(file_or_url_or_text, type=None, worker=None):
    try:
        script = create("<script>").text(open(file_or_url_or_text).read())
    except:
        if file_or_url_or_text.endswith(".js"):
            script = create("<script>").attr("src", file_or_url_or_text)
        else:
            script = create("<script>").text(file_or_url_or_text)
    if type:
        script.attr("type", type)
    if worker:
        script.attr("worker", "")
    script.appendTo(window.document.head)


def inject_css(file_or_url_or_text):
    try:
        node = create("<style>").text(open(file_or_url_or_text).read())
    except:
        if "{" in file_or_url_or_text:
            node = create("<style>").text(file_or_url_or_text)
        else:
            node = create("<link>").attr("rel", "stylesheet").attr("href", file_or_url_or_text)
    node.appendTo(window.document.head)


_fix_time_on_micropython()
inject_script("ltk/ltk.js")
inject_css("ltk/ltk.css")