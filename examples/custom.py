# LTK - Copyright 2024 - All Rights Reserved - chrislaffra.com - See LICENSE 

import ltk

def create():
    class CustomWidget(ltk.VBox):
        classes = [ "custom Widget" ]

        def __init__(self, src, label):
            ltk.VBox.__init__(self, 
                ltk.Image(src).width(196),
                ltk.Text(label).width("100%").css("text-align", "center")
            )
            self.css("border", "2px solid orange")

    card = ltk.Card(
        CustomWidget("images/chris.png", "Chris laffra")
    )

    def animate(event):
        card.animate({ "left": 0, "top": 0 }, 500)

    return (
        ltk.VBox(
            ltk.Heading2("Showing a Card with a custom widget inside of it"),
            card.width(234)
                .attr("id", "card")
                .draggable(),
            ltk.Text("For clarity, we marked the custom widget orange.")
                .css("margin-top", 20),
            ltk.Heading4("Tip: drag the card and then press the button below"),
            ltk.Button("Reset", animate)
                .width(90)
        )
        .css("padding", 8)
        .css("border", "1px solid gray")
        .css("background", "lightyellow")
        .attr("name", "Custom")
        .height(790)
    )
