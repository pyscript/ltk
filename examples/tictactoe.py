# LTK - Copyrights Reserved 2023 - chrislaffra.com - See LICENSE 

import ltk

# Tic Tac Toe Game
#
# This implements a simple Tic Tac Toe game in PyScript using the LTK toolkit.
# It draws a Tic Tac Toe board that allows clicking squares to place X and O marks alternately.
#
# The UI uses LTK widget classes:
#  - Container for each square
#  - VBox and HBox to create the grid
#  - Text for the X and O labels
#
# This provides an interactive grid layout without needing much explicit layout code.

def choose(event):
    #
    # This event handler is attached to each square container:
    #  - The handler checks if the square is empty
    #  - If empty, it adds an X or O text label based on whose turn it is
    #
    square = ltk.find(event.target)
    if not square.text():
        square.append(
            ltk.Text("X" if ltk.find(".choice").length % 2 else "O")
                .addClass("choice")
        )


def enter(event):
    # First erase all existing squares
    ltk.find(".square").css("background", "white")

    # Highlight the current square, but only if does not contain a choice already
    square = ltk.jQuery(event.target)
    if not square.text():
        square.css("background", "lightblue")


def create():
    # Set up the game board:
    #  - Create a 3x3 grid of Container widgets to represent the board squares
    #  - Attach a click handler to each square container
    #  - Add the grid containers into a nested VBox/HBox layout
    #  - Render the layout into the #example div
    return ltk.Div(
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
        ltk.Link(href="https://github.com/laffra/ltk/blob/main/examples/tictactoe.py")
            .attr("target", "_blank")
            .text("source")
    ).attr("name", "Tic Tac Toe")

ltk.inject(__file__, "tictactoe.css")