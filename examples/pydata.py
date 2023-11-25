# LTK - Copyright 2023 - All Rights Reserved - chrislaffra.com - See LICENSE 

import ltk

def create():
    return (
        ltk.VBox(

            ltk.Image("https://pydata.org/wp-content/uploads/2019/06/pydata-logo-final.png")
                .css("margin-top", 50)
                .css("width", 350),

            ltk.Link(
                "https://pydata.org/eindhoven2023/",
                "Come visit PyData Eindhoven"
            )
                .attr("target", "_blank")
                .css("color", "navy")
                .css("margin-top", 50),

            ltk.Text("on November 30 and learn more about LTK, the Pyscript Little Toolkit")
                .css("margin-top", 50),

            ltk.Link(
                "https://eindhoven2023.pydata.org/pydata/talk/RJVRMT/",
                "in this presentation"
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