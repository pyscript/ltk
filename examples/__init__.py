# LTK - Copyright 2023 - All Rights Reserved - chrislaffra.com - See LICENSE 

from examples import app
from examples import custom
from examples import documentation
from examples import helloworld
from examples import inputs
from examples import pubsub
from examples import pydata
from examples import styling
from examples import svg
from examples import table
from examples import tictactoe

items = [
    ("examples/styling.py", styling.create()),
    ("examples/helloworld.py", helloworld.create()),
    ("examples/inputs.py", inputs.create()),
    ("examples/tictactoe.py", tictactoe.create()),
    ("examples/table.py", table.create()),
    ("examples/custom.py", custom.create()),
    ("examples/app.py", app.create()),
    ("examples/pubsub.py", pubsub.create()),
    ("examples/documentation.py", documentation.create()),
    ("examples/svg.py", svg.create()),
    ("examples/pydata.py", pydata.create()),
]