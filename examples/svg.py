# LTK - Copyright 2023 - All Rights Reserved - chrislaffra.com - See LICENSE 

import ltk

def create():

    def ellipse_clicked():
        ltk.find("#svg").css("background-color", "blue")

    def bind_event():
        ltk.find("#ellipse").on(
            "click",
            lambda event: ellipse_clicked()
        )

    #
    # In this specific example we need to bind events after
    # the svg is actually added to the DOM, so we use ltk.schedule
    #
    ltk.schedule(bind_event, "SVG ellipse bind_event")

    # 
    # Note that LTK is based on jQuery, which does not officially supports SVG.
    # Using jQuery methods on SVG documents, unless explicitly documented for
    # that method, might cause unexpected behaviors. 
    # 
    # Examples of jQuery methods that do support SVG are addClass and
    # removeClass.  Event handling also works, as shown in this example.
    # However, the appending of specific SVG nodes using an LTK Widget does
    # not work well. This is why in this example we construct the SVG from
    # HTML, instead of composing it out of nested widgets.
    #

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
