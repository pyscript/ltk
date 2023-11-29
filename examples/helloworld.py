# LTK - Copyright 2023 - All Rights Reserved - chrislaffra.com - See LICENSE 

import ltk

def create():
    return (
        ltk.HBox(
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
        )
        .height("100%")
        .attr("name", "HelloWorld")
    )