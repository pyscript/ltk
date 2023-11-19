# LTK - Copyrights Reserved 2023 - chrislaffra.com - See LICENSE 

import json
import pyodide # type: ignore
import pyscript # type: ignore

timers = {}

js = pyscript.window

jQuery = js.jQuery
console = js.console
window = jQuery(js.window)
document = jQuery(js.document)
head = jQuery("head")
body = jQuery("body")
parse_int = js.parseInt
parse_float = js.parseFloat
local_storage = js.localStorage


def find(selector):
    return jQuery(selector)

def create(selector):
    return jQuery(selector)

def find_list(selector):
    elements = jQuery(selector)
    return [ elements.eq(n) for n in range(elements.length) ]

def to_js(dict):
    js.eval("window.to_js = json => JSON.parse(json);")
    return js.to_js(json.dumps(dict))

def to_py(jsobj):
    try:
        return jsobj.to_py()
    except:
        return json.loads(js.JSON.stringify(jsobj)) # Micropython has no built-in to_py

def number(s):
    return js.parseFloat(s)

def schedule(function, timeout_seconds=0.1):
    if not function:
        raise ValueError(f"schedule: Expecting a function, not {function}")
    if function in timers:
        js.clearTimeout(timers[function])
    timers[function] = js.setTimeout(proxy(function), int(timeout_seconds * 1000))

def repeat(function, timeout_seconds=1):
    js.setInterval(proxy(function), int(timeout_seconds * 1000))

def get(route, handler, kind="json"):
    def wrapper(data, *rest):
        handler(data if isinstance(data, str) else to_py(data))
    return jQuery.get(route, proxy(wrapper), kind)

def delete(route, handler):
    wrapper = proxy(lambda data, *rest: handler(to_py(data)))
    return js.ajax(route, "DELETE", wrapper)

def time():
    return js.time() / 1000

def post(route, data, handler):
    payload = js.encodeURIComponent(json.dumps(data))
    wrapper = proxy(lambda data, status, xhr: handler(js.JSON.stringify(data)))
    return jQuery.post(route, payload, wrapper, "json")

def async_proxy(function):
    async def call_function(*args):
        return await function(*args)
    return pyodide.ffi.create_proxy(call_function)

def proxy(function):
    return pyodide.ffi.create_proxy(function)

def get_url_parameter(key):
    return js.URLSearchParams.new(js.document.location.search).get(key)

def set_url_parameter(key, value, reload=True):
    search = js.URLSearchParams.new(js.window.location.search)
    search.set(key, value)
    url = f"{js.window.location.href.split('?')[0]}?{search.toString()}"
    if reload:
        js.document.location = url
    else:
        push_state(url)

def push_state(url):
    js.history.pushState(None, "", url)


def inject_script(url):
    create("<script>").attr("src", url).appendTo(head)


def inject_css(url):
    create("<link>").attr("rel", "stylesheet").attr("href", url).appendTo(head)