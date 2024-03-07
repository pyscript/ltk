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
            "#world-button",
            "click",
            ltk.Text("Then, click the World button."),
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
