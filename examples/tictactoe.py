# LTK - Copyrights Reserved 2023 - chrislaffra.com - See LICENSE 

import inspect
import ltk

def choose(event):
    square = ltk.find(event.target)
    if not square.text():
        square.append(
            ltk.Text("X" if ltk.find(".choice").length % 2 else "O")
                .addClass("choice")
        )


def enter(event):
    ltk.find(".square").css("background", "white")
    square = ltk.jQuery(event.target)
    if not square.text():
        square.css("background", "lightblue")


def create():
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
        .attr("name", "Tic Tac Toe") # example
        .attr("src", inspect.getsource(create)) # example
    )

ltk.inject(__file__, "tictactoe.css")