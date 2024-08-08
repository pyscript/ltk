# LTK - Copyright 2023 - All Rights Reserved - chrislaffra.com - See LICENSE 

import logging
import ltk
from pyscript import window # type: ignore

search = window.URLSearchParams.new(window.location.search)
runtime = search.get("runtime") or "mpy"

logger = logging.getLogger()


def create():
    def feedback(text):
        ltk.find("#feedback") \
            .html(text) \
            .css("text-align", "left")
        logger.info(text)

    def choose_theme(index, option):
        theme = option.text()
        ltk.inject_css(f"https://ajax.googleapis.com/ajax/libs/jqueryui/1.13.2/themes/{theme}/jquery-ui.css")
        
    @ltk.callback
    def key_down(event):
        feedback(f"keydown: {event.keyCode}, {event.key}")

    @ltk.callback
    def button_clicked(event):
        feedback("You clicked the button")

    @ltk.callback
    def loveit(event):
        feedback(f"checkbox: {ltk.find('#love').prop('checked')}")

    @ltk.callback
    def change(event):
        element = ltk.jQuery(event.target)
        kind = element.prop("type")
        feedback(f"Changed {kind}: {element.val()}")

    @ltk.callback
    def switched(event):
        element = ltk.jQuery(event.target)
        feedback(f"Changed switch: {element.prop('checked')}")

    @ltk.callback
    def set_runtime(event):
        chosen = ltk.jQuery(event.target).attr("value")
        if chosen != runtime:
            window.setSearchParameter("runtime", chosen)

    @ltk.callback
    def open_dialog(event):
        ltk.Div(
            ltk.Text("This is a dialog")
        ).dialog()

    @ltk.callback
    def open_popup(event):
        popup = ltk.Popup(
            ltk.VBox(
                ltk.Text("This is a popup"),
                ltk.Button("Close", lambda event: popup.close())
                    .css("color", "white")
                    .css("background", "red"),
                ltk.Text("Click the red button or outside the popup to close it."),
            ).css("padding", 8)
        ).show(ltk.find("#popup"))

    widgets = [
        ltk.VBox(
            ltk.Text("Choose your favorite theme:"),
            ltk.Select(themes, 0, choose_theme),
        ),
        ltk.VBox(
            ltk.Text("Choose the Python runtime and reload the page:"),
            ltk.RadioGroup(
                ltk.Span(
                    ltk.RadioButton(runtime == "mpy")
                        .attr("name", "runtime")
                        .attr("id", "mpy")
                        .attr("value", "mpy"),
                    ltk.Label("MicroPython").attr("for", "mpy")
                ),
                ltk.Label("PyOdide",
                    ltk.RadioButton(runtime == "py")
                        .attr("name", "runtime")
                        .attr("value", "py")
                ),
            ).on("change", set_runtime)
        ),
        ltk.Button("Click me!", button_clicked),
        ltk.TextArea("This is a text area.\n\nChange me!", {
            "height": 120
        }).on("keydown", key_down),
        ltk.Span(
            ltk.Label("I love LTK",
                ltk.Checkbox(True).attr("id", "love").on("change", loveit),
            )
        ),
        ltk.HBox(
            ltk.Button("Open Dialog", open_dialog),
            ltk.Span("&nbsp;" * 4),
            ltk.Button("Open Popup", open_popup).attr("id", "popup"),
        ),
        ltk.Switch("Python is great:", True).on("change", switched),
        ltk.File().on("change", change),
        ltk.ColorPicker().on("change", change),
        ltk.DatePicker().on("change", change),
        ltk.Input("This is an input. Change me!", {
            "width": 180,
            "padding": 10,
        })
        .on("keydown", key_down)
        .on("change", change),
    ]

    def get_widgets():
        for widget in widgets:
            yield widget
            yield ltk.Paragraph()

    return (
        ltk.VBox(
            ltk.Heading1(f"Widgets on {runtime}")
                .css("text-align", "left")
                .height(50)
                .attr("id", "feedback"),
            ltk.Container(get_widgets()), {
                "padding": 50,
                "border": "1px solid gray",
            }
        )
        .height(708)
        .attr("id", "inputs")
        .attr("name", "Inputs")
    )

themes = [
    "base",
    "black-tie",
    "blitzer",
    "cupertino",
    "dark-hive",
    "dot-luv",
    "eggplant",
    "excite-bike",
    "flick",
    "hot-sneaks",
    "humanity",
    "le-frog",
    "mint-choc",
    "overcast",
    "pepper-grinder",
    "redmond",
    "smoothness",
    "south-street",
    "start",
    "sunny",
    "swanky-purse",
    "trontastic",
    "ui-darkness",
    "ui-lightness",
    "vader",
]