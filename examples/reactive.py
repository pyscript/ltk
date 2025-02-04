# LTK - Copyright 2024 - All Rights Reserved - chrislaffra.com - See LICENSE 

import ltk

DELIVERY_OPTIONS = ["1-day", "2-day", "pickup"]

class Product(ltk.Model):
    count: int = 10
    name: str = "Screwdriver"
    price: float = 50.0
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

product1 = Product(name="Wrench", delivery=0)
product2 = Product(name="Drill", count=6, price=500, service=False)

def increment_count(event):
    product1.count += 10

def order_hammers(event):
    product2.name = "Hammer"
    product2.count = 10
    product2.price = 100.0
    product2.warranty = True
    product2.delivery = 2
    product2.service = False

def create_form(name, product):
    return ltk.VBox(
        ltk.Label(name),
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

def create():
    return (
        ltk.VBox(
            ltk.Heading2("Reactive LTK Demo"),
            create_form("Product 1", product1)
                .css("border", "2px solid green")
                .css("padding", 12)
                .css("margin-bottom", 12)
                .css("font-size", 24),
            create_form("Product 2", product2)
                .css("border", "2px solid green")
                .css("padding", 12)
                .css("font-size", 24)
                .attr("name", "Reactive"),
            ltk.Button("Set Product 2 to Hammer", order_hammers)
                .css("margin-top", 24)
                .css("border-radius", 8)
                .css("padding", 12),
            ltk.Button("Increment Product 1 count", increment_count)
                .css("margin-top", 24)
                .css("border-radius", 8)
                .css("padding", 12),
        )
        .attr("id", "reactive")
        .attr("name", "Reactive")
    )

def row(label, *widgets):
    return ltk.HBox(
        ltk.Text(label)
            .css("font-size", 16)
            .height(33)
            .width(120),
        *widgets
    )
    
