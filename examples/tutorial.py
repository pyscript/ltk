# LTK - Copyright 2023 - All Rights Reserved - chrislaffra.com - See LICENSE 

import ltk

def tutorial():
    return ltk.Tutorial([
        (
            "#hello-button",
            "click",
            ltk.Text("First, click the Hello button."),
        ),
        (
            "#hello-world",
            "drag",
            ltk.Text("Then drag the pink text box."),
        ),
        (
            "#world-button",
            "click",
            ltk.Text("Finally, click the World button."),
        ),
])


def create():
    return (
        ltk.VBox(
            ltk.Button("Hello", lambda event: print("hello"))
                .css("margin", 20)
                .css("font-size", 32)
                .css("background", "lightgreen")
                .css("border-radius", 10)
                .attr("id", "hello-button"),

            ltk.Text("Hello World")
                .css("margin", 20)
                .css("background", "pink")
                .css("border-radius", 10)
                .css("font-size", 24)
                .css("padding", 20)
                .css("width", 120)
                .attr("id", "hello-world")
                .draggable(),

            ltk.Button("World", lambda event: print("world"))
                .css("margin", 20)
                .css("background", "lightblue")
                .css("border-radius", 10)
                .css("font-size", 32)
                .attr("id", "world-button"),

            ltk.Button("start the tutorial", lambda event: tutorial().run())
                .css("margin", 20)
                .css("margin-top", 60)
        )
        .css("height", 800)
        .attr("name", "Tutorial")
    )
