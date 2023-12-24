# LTK - Copyright 2023 - All Rights Reserved - chrislaffra.com - See LICENSE 

import ltk

def create():
    return (
        ltk.VBox(

            ltk.Image("images/pydata.png")
                .css("margin-top", 50)
                .width(350),

            ltk.Link(
                "https://pydata.org/eindhoven2023/",
                "LTK was presented at PyData Eindhoven,"
            )
                .attr("target", "_blank")
                .css("color", "navy")
                .css("margin-top", 50),

            ltk.Link(
                "https://eindhoven2023.pydata.org/pydata/talk/RJVRMT/",
                "in this presentation,"
            )
                .attr("target", "_blank")
                .css("color", "navy")
                .css("margin-top", 50),

            ltk.Link(
                "https://www.youtube.com/watch?v=5nseG-iU62g&list=PLGVZCDnMOq0qkbJjIfppGO44yhDV2i4gR&index=6",
                "recorded in this video."
            )
                .attr("target", "_blank")
                .css("color", "navy")
                .css("margin-top", 50),

            ltk.Text("by Chris Laffra")
                .css("margin-top", 50),

        )
        .css("font-size", 32)
        .attr("name", "Pydata")
    )