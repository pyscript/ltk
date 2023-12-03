# LTK - Copyright 2023 - All Rights Reserved - chrislaffra.com - See LICENSE 

import ltk

def create():

    def ellipse_clicked():
        ltk.find("#svg").css("background-color", "blue")

    def bind_event():
        ltk.find("#ellipse").on("click", ltk.proxy(lambda event: ellipse_clicked()))

    #
    # Only in this specific example we need to bind events after
    # the svg is actually added to the DOM, so we use ltk.schedule
    #
    ltk.schedule(bind_event, "bind_event")

    return(
        ltk.VBox(
            ltk.Heading2("This is an SVG Ellipse:"),
            ltk.create("""
                <svg id="svg" height="180" width="500">
                    <ellipse id="ellipse" cx="200" cy="80" rx="100" ry="50" style="fill:yellow;stroke:purple;stroke-width:2" />
                </svg>
            """),
            ltk.Heading3("Click the yellow ellipse to change the SVG's background color."),
        )
        .attr("name", "SVG")
    )
