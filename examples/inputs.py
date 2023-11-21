# LTK - Copyrights Reserved 2023 - chrislaffra.com - See LICENSE 

import logging
import ltk

logger = logging.getLogger()

def create():
    def feedback(text, color):
        ltk.find("#feedback") \
            .html(text) \
            .css("text-align", "left") \
            .css("color", color)
        logger.info(text)

    def number_chosen(event, option):
        feedback(f"You chose {option.text()}", "green")
        
    @ltk.callback
    def key_down(event):
        feedback(f"keydown: {event.keyCode}, {event.key}", "blue")

    @ltk.callback
    def button_clicked(event):
        feedback("You clicked the button", "red")

    @ltk.callback
    def loveit(event):
        feedback(f"checkbox: {ltk.find('#love').prop('checked')}", "black")

    @ltk.callback
    def change(event):
        element = ltk.jQuery(event.target)
        kind = element.prop("type")
        feedback(f"Changed {kind}: {element.val()}", "purple")


    widgets = [
        ltk.Button("Click me!", button_clicked, {
            "color": "white",
            "background-color": "red",
            "padding": 6,
        }),
        ltk.Select(["One", "Two", "Three" ], "Two", number_chosen, {
            "padding": 6,
            "color": "white",
            "background-color": "green",
        }),
        ltk.TextArea("This is a text area.\n\nChange me!", {
            "height": 120
        }).on("keydown", key_down),
        ltk.Span(
            ltk.Checkbox(True).attr("id", "love").on("change", loveit),
            ltk.Label("I love LTK")
        ),
        ltk.File().on("change", change),
        ltk.ColorPicker().on("change", change),
        ltk.DatePicker().on("change", change),
        ltk.Input("This is an input. Change me!", {
            "width": 180,
            "padding": 10,
            "background-color": "pink",
        })
        .on("keydown", key_down)
        .on("change", change),
    ]

    def get_widgets():
        for widget in widgets:
            yield widget
            yield ltk.P()

    return (
        ltk.VBox(
            ltk.H1("Input widgets")
                .css("text-align", "left")
                .css("height", 50)
                .attr("id", "feedback"),
            ltk.Container(get_widgets()), {
                "padding": 50,
                "background-color": "lightyellow",
            }
        )
        .css("height", 710)
        .attr("name", "Inputs")
    )