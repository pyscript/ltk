import examples
import ltk


def cleanup(src):
    return "\n".join([
        line
        for line in src.split("\n")
        if not "# example" in line
    ])

ltk.find("#progress").remove()

ltk.body.append(
    ltk.Div(
        ltk.Tabs(
            ltk.HBox(
                example.css("width", "40%"),
                ltk.VBox(
                    ltk.H2("The source:"),
                    ltk.TextArea(cleanup(example.attr("src")))
                        .css("height", 400)
                        .css("border-width", 0)
                        .css("font-family", "Courier")
                )
                .css("width", "60%")
                .css("padding-left", 24)
                .css("border-left", "2px solid lightgray"),
            ).attr("name", example.attr("name"))
            for example in examples.elements
        ).css("margin-bottom", 24),
        ltk.Link("https://github.com/laffra/ltk", ltk.Text("source"))
            .attr("target", "_blank")
    )
    .css("width", 1300)
    .css("margin", "auto")
)