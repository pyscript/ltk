# LTK - Copyrights Reserved 2023 - chrislaffra.com - See LICENSE 

import ltk

# Create a new widget, based on VBox
class ImageWithLabel(ltk.VBox):
    classes = [ "custom" ]

    def __init__(self, src, label):
        ltk.VBox.__init__(self, 
            # Add two widgets. Styling could be done in external CSS
            ltk.Image(src)
                # CSS selector would be ".custom .ltk-image"
                .css("width", 200),
            ltk.Text(label)
                # CSS selector would be ".custom .ltk-text"
                .css("width", "100%")
                .css("text-align", "center")
        )


def create():
    # Create the custom widget and add an orange border for clarity
    custom_widget = ImageWithLabel(
        "https://chrislaffra.com/chris.png",
        "Chris laffra"
    ).css("border", "2px solid orange")

    return ltk.VBox(
        ltk.H2("Showing a Card with a custom widget inside of it"),
        ltk.Card(custom_widget)
            .css("width", 200)
            .draggable(),
        ltk.Text("For clarity, we marked the custom widget orange.")
            .css("margin-top", 20),
        ltk.H4("Tip: drag the card."),
        ltk.Link(href="https://github.com/laffra/ltk/blob/main/examples/custom.py")
            .attr("target", "_blank")
            .text("source")
    ).attr("name", "Custom")
