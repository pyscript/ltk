# LTK - Copyright 2024 - All Rights Reserved - chrislaffra.com - See LICENSE 

import ltk

def create():
    @ltk.callback
    def choose(event):
        if not ltk.find(event.target).text():
            ltk.find(event.target).append(
                ltk.Text("X" if ltk.find(".tictactoe-choice").length % 2 else "O")
                    .addClass("tictactoe-choice")
            )

    @ltk.callback
    def enter(event):
        ltk.find(".tictactoe-inside").removeClass("tictactoe-inside")
        if not ltk.find(event.target).text():
            ltk.find(event.target).addClass("tictactoe-inside")

    return (
        ltk.VBox(
            ltk.Heading2("Tic Tac Toe Game"),
            ltk.VBox(
                ltk.HBox(
                    ltk.Container()
                        .addClass("tictactoe-square")
                        .on("click", choose)
                        .on("mouseenter", enter)
                    for column in range(3)
                )
                for row in range(3)
            ),
            ltk.Heading3("Tip: Click inside the squares."),
            ltk.Label("The CSS:"),
            ltk.TextArea("CSS will be loaded here...").addClass("tictactoe-css"),
        )
        .attr("name", "TicTacToe")
    )

ltk.get(
    "examples/tictactoe.css",
    lambda css: ltk.find(".tictactoe-css").text(css),
    "html"
)

ltk.inject_css("examples/tictactoe.css")