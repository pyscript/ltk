# LTK - Copyrights Reserved 2023 - chrislaffra.com - See LICENSE 

import inspect
import ltk


def create():
    
    class CustomWidget(ltk.VBox):
        classes = [ "custom" ]

        def __init__(self, src, label):
            ltk.VBox.__init__(self, 
                ltk.Image(src).css("width", 196),
                ltk.Text(label).css("width", "100%").css("text-align", "center")
            )
            self.element.css("border", "2px solid orange")


    return (
        ltk.VBox(
            ltk.H2("Showing a Card with a custom widget inside of it"),
            ltk.Card(
                CustomWidget("https://chrislaffra.com/chris.png", "Chris laffra")
            ).css("width", 200).draggable(),
            ltk.Text("For clarity, we marked the custom widget orange.").css("margin-top", 20),
            ltk.H4("Tip: drag the card."),
        )
        .attr("name", "Custom")                 # example
        .attr("src", inspect.getsource(create)) # example
    )
