# LTK - Copyright 2024 - All Rights Reserved - chrislaffra.com - See LICENSE 

import ltk
import random


def create():

    canvas = ltk.Canvas()
    colors = ["black", "red", "white", "blue", "green", "yellow", "purple", "teal", "orange"]

    def mousemove(event):
        canvas.fill_style = random.choice(colors)
        canvas.fill_rect(event.offsetX, event.offsetY, 50, 50)

        canvas.fill_style = random.choice(colors)
        canvas.fill_circle(event.offsetX + 25, event.offsetY + 25, 25)

        canvas.stroke_style = "black"
        canvas.rect(event.offsetX + 8, event.offsetY + 8, 34, 34)
        canvas.circle(event.offsetX + 25, event.offsetY + 25, 12)

    return (
        ltk.VBox(
            ltk.Heading2("This is a Canvas. Move the mouse to draw."),
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
