# LTK - Copyright 2023 - All Rights Reserved - chrislaffra.com - See LICENSE 

import ltk

source = """
ltk.VBox(
    ltk.HBox(
        ltk.Span("Edit the text in"),
        ltk.Span("the editor below")
            .css("margin", 12),
    )
    .css("height", 40)
    .css("background", "lightblue")
    .css("border", "1px solid gray"),

    ltk.HBox(
        ltk.Span("This UI will update live")
            .css("margin", 12),
        ltk.Span("With every character you type!")
            .css("margin-top", 24),
    )
    .css("height", 80)
    .css("background", "lightyellow")
    .css("border", "2px solid red"),
)
""".strip()

def create():
    editor = Editor(source)

    def show_output():
        print(editor.text())
        eval(editor.text()).appendTo(
            ltk.find("#editor-output")
                .empty()
        )

    ltk.schedule(ltk.proxy(lambda: show_output()), "show output", 0.1)

    return(
        ltk.VerticalSplitPane(
            ltk.Div()
                .css("border", "1px solid gray")
                .attr("id", "editor-output"),
            editor
                .on("keyup", ltk.proxy(lambda event: show_output()))
                .css("border", "1px solid gray")
                .attr("id", "editor"),
            "interactive editor"
        )
        .css("height", 805)
        .css("width", 400)
        .css("font-size", 14)
        .attr("name", "Editor")
    )

class Editor(ltk.Div):
    classes = [ "editor" ]

    def __init__(self, value):
        ltk.Div.__init__(self)
        ltk.schedule(ltk.proxy(lambda: self.create(value)), "refresh editor", 0.1)

    def create(self, value):
        config = ltk.to_js({
            "mode": {
                "name": "python",
                "version": 3,
                "singleLineStringErrors": False
            },
            "lineNumbers": True,
            "indentUnit": 4,
            "matchBrackets": True,
        })
        self.editor = ltk.window.CodeMirror(self.element[0], config)
        self.editor.setSize("100%", "100%")
        self.text(value)

    def text(self, text=None):
        return self.editor.setValue(text) if text is not None else self.editor.getValue()
