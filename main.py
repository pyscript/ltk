import examples
import ltk


def cleanup(src):
    return "\n".join([
        line
        for line in src.split("\n")[:-2]
        if not "# only needed for example" in line
    ])


ltk.body.append(
    ltk.Tabs(
        ltk.HBox(
            example.css("width", "50%"),
            ltk.VBox(
                ltk.H2("The source:"),
                ltk.TextArea(cleanup(example.attr("src")))
                    .css("height", 400)
            ).css("width", "50%"),
        ).attr("name", example.attr("name"))
        for example in examples.elements
    )
)
