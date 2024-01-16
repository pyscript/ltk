# LTK - Copyright 2023 - All Rights Reserved - chrislaffra.com - See LICENSE 

from examples import app
from examples import custom
from examples import documentation
from examples import dom
from examples import inputs
from examples import pitch
from examples import pizza
from examples import pubsub
from examples import pydata
from examples import styling
from examples import svg
from examples import table
from examples import tictactoe

items = [
    ("examples/styling.py", styling.create()),
    ("examples/dom.py", dom.create()),
    ("examples/inputs.py", inputs.create()),
    ("examples/tictactoe.py", tictactoe.create()),
    ("examples/table.py", table.create()),
    ("examples/custom.py", custom.create()),
    ("examples/app.py", app.create()),
    ("examples/pubsub.py", pubsub.create()),
    ("examples/documentation.py", documentation.create()),
    ("examples/pitch.py", pitch.create()),
    ("examples/svg.py", svg.create()),
    ("examples/pydata.py", pydata.create()),
    ("examples/pizza.py", pizza.create()),
]