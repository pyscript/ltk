# LTK - Copyright 2024 - All Rights Reserved - chrislaffra.com - See LICENSE 

import ltk

def create():

    def click(event):
        element = ltk.find(event.target)
        color = element.css("background-color")
        ltk.find("#style-msg").text(
            f"You pressed the '{element.text()}' button with background color: {color}"
        )

    ui = (
        ltk.VBox(
            ltk.Text("An unstyled button:"),
            ltk.Button("Default", click),

            ltk.Text("A blue button using element styles:"),
            ltk.Button("Blue", click)
                .css("background-color", "#007fff")
                .css("color", "white"),

            ltk.Text("An orange button with CSS in the constructor:"),
            ltk.Button("Orange", click, {
                "background-color": "orange",
                "color": "#111",
            }),

            ltk.Text("A button using element hover:"),
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

            ltk.Text("A button styled with a CSS class with hover:"),
            ltk.Button("Classy", click).addClass("classy"),

            ltk.Text("").attr("id", "style-msg")
        )
        .attr("name", "Styling")
    )

    # For this example, we are injecting a new style tag from Python.
    # For a real app, you probably want to use an external style sheet.
    ltk.inject_css("""
        .classy {
            width: 110px;
            background-color: var(--ltk-primary);
            color: var(--ltk-white);
            border-radius: 11px;
            padding: 14px;
        }
        .classy:hover {
            background-color: var(--ltk-secondary);
        }
    """)

    ui.find(".ltk-button").width(110).css("margin-bottom", 25)

    return ui