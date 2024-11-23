# LTK - Copyright 2024 - All Rights Reserved - chrislaffra.com - See LICENSE 

import ltk

DELIVERY_OPTIONS = ["1-day", "2-day", "pickup"]

class Product(ltk.Model):
    name: str = "Wrench"
    price: float = 50.0
    count: int = 10
    warranty: bool = False
    service: bool = True
    delivery: int = 1
    summary: str = ""

    def changed(self, name, value):
        if name == "summary":
            return
        self.summary = f"""
            {self.count} * {self.name} =
            ${round(self.count * self.price):,}
            {'including warranty' if self.warranty else ''}
            {'with service' if self.service else ''}
            - Delivery: {DELIVERY_OPTIONS[self.delivery]}
        """

product = Product(count=60)

def create():
    form = ltk.VBox(
        row(
            "Name:",
            ltk.Input(product.name).width(300)
        ),
        row(
            "Price:",
            ltk.Input(product.price).width(300)
                .attr("type", "number")
        ),
        row(
            "Count:",
            ltk.Slider(product.count, 0, 100).width(250)
                .css("margin-top", 10),
            ltk.Label(product.count)
                .css("margin", "5px 15px")
        ),
        row(
            "Warranty:",
            ltk.Checkbox(product.warranty)
                .css("width", 18)
        ),
        row(
            "Delivery:",
            ltk.Select(DELIVERY_OPTIONS, product.delivery)
                .css("margin-top", 2)
                .height(24)
        ),
        row(
            "Service:",
            ltk.Switch("With white gloves:", product.service)
        ),
        ltk.Div("<hr>"),
        row(
            "Summary:",
            ltk.Text(product.summary)
        )
    )
    return (
        ltk.VBox(
            ltk.Heading2("LTK Model-View Demo"),
            form
                .css("border", "2px solid green")
                .css("padding", 12)
                .css("font-size", 24)
                .attr("name", "MVC"),
            ltk.Button("Buy Hammers", order_hammers)
                .css("margin-top", 24)
                .css("border-radius", 8)
            .css("padding", 12)
        )
        .attr("id", "mvc")
        .attr("name", "MVC")
    )

def order_hammers(event):
    product.name = "Hammer"
    product.count = 10
    product.price = 100.0
    product.warranty = True
    product.delivery = 2
    product.service = False

def row(label, *widgets):
    return ltk.HBox(
        ltk.Text(label)
            .css("font-size", 16)
            .height(33)
            .width(120),
        *widgets
    )
    
