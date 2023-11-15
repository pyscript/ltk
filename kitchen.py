import examples
import js
import ltk


def cleanup(src):
    return "\n".join([
        line
        for line in src.split("\n")
        if not "# example" in line
    ])


def getsource(file):
    def setsource(src):
        src = "\n".join(src.split("\n")[2:])
        ltk.find(f'textarea[file="{file}"]').val(src)

    ltk.get(file, setsource, "html")
    return file


ltk.find("#progress").remove()
ltk.find("#title").append(f" took {js.startTime() / 1000}s to load")


ltk.body.append(
    ltk.Div(
        ltk.Tabs(
            ltk.HBox(
                example.css("width", "40%"),
                ltk.VBox(
                    ltk.H2("The source:"),
                    ltk.TextArea(getsource(file))
                        .attr("file", file)
                        .css("height", 800)
                        .css("border-width", 0)
                        .css("font-family", "Courier")
                )
                .css("width", "60%")
                .css("padding-left", 24)
                .css("border-left", "2px solid lightgray"),
            ).attr("name", example.attr("name"))
            for file, example in examples.items
        ).css("margin-bottom", 24),
        ltk.Link(
            "https://github.com/laffra/ltk",
            ltk.HBox(
                ltk.Image("https://github.com/favicon.ico").width(20),
                ltk.Text("See the LTK project at Github")
            )
        ).attr("target", "_blank")
    )
    .css("width", 1300)
    .css("margin", "auto")
)