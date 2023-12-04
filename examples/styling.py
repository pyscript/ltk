# LTK - Copyright 2023 - All Rights Reserved - chrislaffra.com - See LICENSE 

import ltk

def create():

    def click(event):
        element = ltk.find(event.target)
        color = element.css("background-color")
        element.parent().find(".ltk-text").text(
            f"You pressed the '{element.text()}' button with background color: {color}"
        )

    ui = (
        ltk.VBox(
            ltk.Button("Default", click),

            ltk.Button("Blue", click)
                .css("background-color", "#007fff")
                .css("color", "white"),

            ltk.Button("Modern", click)
                .css({
                    "background": "white",
                    "color": "#222",
                    "border": "1px solid gray",
                    "height": 48,
                    "border-radius": 24,
                    "font-family": "Arial",
                    "font-size": 16,
                    "padding": "10px 5px",
                })
                .hover(ltk.proxy(lambda e:
                    ltk.find(e.target)
                        .css(ltk.to_js({
                            "text-decoration": "underline" if e.type == "mouseenter" else "none",
                            "background": "#EEE" if e.type == "mouseenter" else "white",
                        }))
                )),

            ltk.Text("")
        )
        .attr("name", "Styling")
    )

    ui.find(".ltk-button").width(110).css("margin-bottom", 25)

    return ui