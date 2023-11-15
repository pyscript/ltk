# LTK - Copyrights Reserved 2023 - chrislaffra.com - See LICENSE 

import ltk

def create():
    def choose(event):
        if not ltk.find(event.target).text():
            ltk.find(event.target).append(
                ltk.Text("X" if ltk.find(".choice").length % 2 else "O")
                    .addClass("choice")
            )

    def enter(event):
        ltk.find(".square").css("background", "white")
        if not ltk.jQuery(event.target).text():
            ltk.jQuery(event.target).css("background", "lightblue")

    return (
        ltk.Div(
            ltk.H2("Tic Tac Toe Game"),
            ltk.VBox(
                ltk.HBox(
                    ltk.Container()
                        .addClass("square")
                        .on("click", ltk.proxy(choose))
                        .on("mouseenter", ltk.proxy(enter))
                    for column in range(3)
                )
                for row in range(3)
            ),
            ltk.H4("Tip: Click inside the squares."),
        )
        .attr("name", "Tic Tac Toe")
    )

ltk.inject(__file__, "tictactoe.css")