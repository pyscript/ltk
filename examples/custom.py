# LTK - Copyright 2023 - All Rights Reserved - chrislaffra.com - See LICENSE 

import ltk

def create():
    class CustomWidget(ltk.VBox):
        classes = [ "custom Widget" ]

        def __init__(self, src, label):
            ltk.VBox.__init__(self, 
                ltk.Image(src).css("width", 196),
                ltk.Text(label).css("width", "100%").css("text-align", "center")
            )
            self.element.css("border", "2px solid orange")


    return (
        ltk.VBox(
            ltk.Heading2("Showing a Card with a custom widget inside of it"),
            ltk.Card(
                CustomWidget("https://chrislaffra.com/chris.png", "Chris laffra")
            ).css("width", 200).draggable(),
            ltk.Text("For clarity, we marked the custom widget orange.")
                .css("margin-top", 20),
            ltk.Heading4("Tip: drag the card."),
        )
        .attr("name", "Custom Widget")
    )
