# LTK - Copyright 2023 - All Rights Reserved - chrislaffra.com - See LICENSE 

import ltk

def create():

    return(
        ltk.VerticalSplitPane(
            ltk.HorizontalSplitPane(
                ltk.Text("Top - Left").css("background", "lightyellow"),
                ltk.Text("Top - Right").css("background", "pink"),
                "demo-horizonal-split-top"
            ),
            ltk.HorizontalSplitPane(
                ltk.Text("Bottom - Left").css("background", "lightgreen"),
                ltk.Text("Bottom - Right").css("background", "lightblue"),
                "demo-horizonal-split-bottom"
            ),
            "demo-vertical-split"
        )
        .css("font-size", 32)
        .attr("name", "Splits")
    )
