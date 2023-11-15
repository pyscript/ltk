# LTK - Copyrights Reserved 2023 - chrislaffra.com - See LICENSE 

import ltk

def create():
    return (
        ltk.Text("Hello World 🎉")
            .css("padding", "100px 10px")
            .css("background-color", "orange")
            .css("font-size", 42)
            .attr("name", "Hello World")
    )