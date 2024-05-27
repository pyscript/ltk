# LTK - Copyright 2023 - All Rights Reserved - chrislaffra.com - See LICENSE 

import ltk
import random


def create():

    canvas = ltk.Canvas()
    colors = ["black", "red", "white", "blue", "green", "yellow", "purple", "teal", "orange"]

    def mousemove(event):
        canvas.fillStyle = random.choice(colors)
        canvas.fillRect(event.offsetX, event.offsetY, 50, 50)

    return (
        ltk.VBox(
            ltk.Heading2("This is a Canvas. Move the mouse draw squares."),
            canvas
                .attr("id", "pink-canvas") \
                .on("mousemove", ltk.proxy(mousemove)) \
                .attr("width", "500px") \
                .attr("height", "500px") \
                .css("width", "500px") \
                .css("height", "500px") \
                .css("border", "1px solid gray") \
                .css("background", "pink")
        )
        .attr("name", "Canvas")
    )
