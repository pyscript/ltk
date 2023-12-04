# LTK - Copyright 2023 - All Rights Reserved - chrislaffra.com - See LICENSE 

import ltk

def create():

    def click(event):
        element = ltk.find(event.target)
        ltk.find("#styling-text").text(
            f"You pressed the button with background color: {element.css('background-color')}"
        )

    ui = (
        ltk.VBox(
            ltk.Button("Unstyled", click),
            ltk.Button("Blue", click)
                .css("background-color", "blue")
                .css("color", "white")
                .css("border", "none")
                .css("font-family", "Arial")
                .css("padding", 19),
            ltk.Button("Red", click)
                .css("background-color", "red")
                .css("color", "white")
                .css("border", "3px solid black")
                .css("border-radius", 15)
                .css("font-family", "Arial")
                .css("padding", 19),
            ltk.Break(),
            ltk.Button("Modern", click)
                .css("background-color", "lightgray")
                .css("color", "#222")
                .css("border", "none")
                .css("height", 48)
                .css("border-radius", 24)
                .css("font-family", "Arial")
                .css("font-size", 16)
                .css("padding", "10px 5px"),
            ltk.Text("")
                .css("margin-top", 50)
                .attr("id", "styling-text")
        )
        .attr("name", "Styling")
    )

    ui.find(".ltk-button").width(110).css("margin-bottom", 25)

    return ui