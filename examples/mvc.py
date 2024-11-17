# LTK - Copyright 2023 - All Rights Reserved - chrislaffra.com - See LICENSE 

import ltk

class Product(ltk.Model):
    """ This is a model with two fields """
    name: str = ""
    price: float = 0.0

product = Product()

def clear(event):
    product.name = ""

def create():
    return (
        ltk.VBox(
            ltk.Heading2("LTK Model-View Demo"),

            ltk.Label("Product Name (as ltk.Input):"),
            ltk.Input(product.name)
                .attr("placeholder", "Please enter a name")
                .css("border", "2px solid red"),

            ltk.Break(),

            ltk.Label("Product Name (as ltk.Text):"),
            ltk.Text(product.name)
                .css("border", "2px solid green")
                .css("height", 34),

            ltk.Break(),
            ltk.Button("Clear product.name", ltk.proxy(clear)),
        )
        .css("font-size", 24)
        .attr("name", "MVC")
    )
