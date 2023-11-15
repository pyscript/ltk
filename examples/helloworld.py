# LTK - Copyrights Reserved 2023 - chrislaffra.com - See LICENSE 

import ltk

def create():
    return ltk.HBox(
        ltk.Text("Hello 🎉", {
            "padding": 50,
            "background-color": "orange",
            "font-size": 42,
        }),

        ltk.Text("World 🎉")
            .css("padding", 50)
            .css("background-color", "red")
            .css("color", "white")
            .css("font-size", 42)
    ).attr("name", "Hello World")