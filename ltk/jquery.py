# LTK - Copyrights Reserved 2023 - chrislaffra.com - See LICENSE 

import json
import pyodide # type: ignore
from pyscript import window


timers = {}


jQuery = window.jQuery
parse_int = window.parseInt
parse_float = window.parseFloat
local_storage = window.localStorage


def find(selector):
    return jQuery(selector)


def create(selector):
    return jQuery(selector)


def find_list(selector):
    elements = jQuery(selector)
    return [ elements.eq(n) for n in range(elements.length) ]


def to_js(dict):
    return window.to_js(json.dumps(dict))


def to_py(jsobj):
    try:
        return jsobj.to_py()
    except:
        try:
            return json.loads(window.to_py(jsobj)) # Micropython has no built-in to_py
        except:
            return str(jsobj)


def number(s):
    return parse_float(s)


def schedule(python_function, timeout_seconds=0.1):
    if not python_function:
        raise ValueError(f"schedule: Expecting a function, not {python_function}")
    if python_function in timers:
        window.clearTimeout(timers[python_function])
    timers[python_function] = window.setTimeout(proxy(python_function), int(timeout_seconds * 1000))


def repeat(python_function, timeout_seconds=1):
    window.setInterval(proxy(python_function), int(timeout_seconds * 1000))


def get(route, handler, kind="json"):
    def wrapper(data, *rest):
        handler(data if isinstance(data, str) else to_py(data))
    return jQuery.get(route, proxy(wrapper), kind)


def delete(route, handler):
    wrapper = proxy(lambda data, *rest: handler(to_py(data)))
    return window.ajax(route, "DELETE", wrapper)


def time():
    return window.time() / 1000


def post(route, data, handler):
    payload = window.encodeURIComponent(json.dumps(data))
    wrapper = proxy(lambda data, *rest: handler(window.JSON.stringify(data)))
    return jQuery.post(route, payload, wrapper, "json")


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
    return pyodide.ffi.create_proxy(function)


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


def inject_script(url):
    create("<script>").attr("src", url).appendTo(window.document.head)


def inject_css(url):
    create("<link>").attr("rel", "stylesheet").attr("href", url).appendTo(window.document.head)