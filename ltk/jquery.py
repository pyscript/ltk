# LTK - Copyrights Reserved 2023 - chrislaffra.com - See LICENSE 

import js # type: ignore
import json
import os
import pyodide # type: ignore
import traceback


timers = {}

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
    pyodide.code.run_js("window.to_js = json => JSON.parse(json);")
    return js.to_js(json.dumps(dict))

def time():
    return js.time()

def number(s):
    return js.parseFloat(s)

def schedule(function, timeout_seconds=0.1):
    if function in timers:
        js.clearTimeout(timers[function])
    timers[function] = js.setTimeout(proxy(function), timeout_seconds * 1000)

def repeat(function, timeout_seconds=1):
    if function in timers:
        js.clearTimeout(timers[function])
    timers[function] = js.setInterval(proxy(function), timeout_seconds * 1000)

def repeat(function, timeout_seconds=1.0):
    js.setInterval(proxy(function), timeout_seconds * 1000)

def get(route, handler):
    wrapper = proxy(lambda data, status, xhr: handler(data.to_py()))
    return jQuery.get(route, wrapper, "json")

def delete(route, handler):
    wrapper = proxy(lambda data, status, xhr: handler(data.to_py()))
    return js.ajax(route, "DELETE", wrapper)

def post(route, data, handler):
    payload = js.encodeURIComponent(json.dumps(data))
    wrapper = proxy(lambda data, status, xhr: handler(js.JSON.stringify(data)))
    return jQuery.post(route, payload, wrapper, "json")

def proxy(function):
    async def call_function(*args):
        try:
            result = function(*args)
            try:
                await result # await async callback when needed
            except:
                pass
        except:
            traceback.print_exc()
    return pyodide.ffi.create_proxy(call_function)

def get_url_parameter(key):
    return js.URLSearchParams.new(js.document.location.search).get(key)

def set_url_parameter(key, value):
    js.document.location = f"?{key}={value}"

def push_state(url):
    js.history.pushState(None, "", url)

injected = set()

def inject(modulepath, *files):
    types = {
        ".js": "<script>",
        ".css": "<style>",
    }
    for file in files:
        _, extension = os.path.splitext(file)
        tag = types[extension]
        path = os.path.join(os.path.dirname(modulepath), file)
        if not path in injected:
            create(tag).text(open(path).read()).appendTo(head)
        injected.add(path)

def inject_script(url, force=False):
    if force or not url in injected:
        create("<script>").attr("src", url).appendTo(head)
        injected.add(url)

def inject_css(url, force=False):
    if force or not url in injected:
        create("<link>").attr("rel", "stylesheet").attr("href", url).appendTo(head)
        injected.add(url)