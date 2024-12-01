import ltk  # Load early on MicroPython, before logging

import examples
from pyscript import window # type: ignore
import logging

logger = logging.getLogger("kitchensink")


def cleanup(src):
    return "\n".join([
        line
        for line in src.split("\n")
        if not "# example" in line
    ])


def getsource(file):
    def setsource(src):
        src = "\n".join(src.split("\n")[2:])
        ltk.find(f'code[file="{file}"]').empty().text(src)

    ltk.get(file, setsource, "html")
    return f"Loading {file}..."


ltk.find("#progress").remove()
ltk.find("#title").append(f" took {window.startTime() / 1000:.3f}s to load")

tabs = ltk.Tabs(
    ltk.HBox(
        example
            .addClass("example"),
        ltk.Code("python", getsource(file))
            .attr("file", file)
            .css("margin-left", 20)
            .width("95%")
            .height(800)
    ).attr("name", example.attr("name"))
    for file, example in examples.items
)

@ltk.callback
def activate_tab(event, ui=None):
    index = tabs.active()
    ltk.set_url_parameter("tab", index, False)
    logger.info("Switched to tab %s", index)

tabs.activate(ltk.get_url_parameter("tab") or 0)

ltk.find(window.document.body).append(
    # ltk.Logger().element,
    ltk.Div(
        tabs.css("margin-bottom", 24)
            .attr("id", "examples")
            .on("tabsactivate", activate_tab)
    )
    .width(1300)
    .css("margin", "auto")
)

def load():
    logger.info("Kitchensink Ready")
