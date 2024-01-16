# LTK - Copyright 2023 - All Rights Reserved - chrislaffra.com - See LICENSE 

import ltk

def create():

    @ltk.callback
    def order(event):
        pizza_type = ltk.find("#pizza-type input:checked").parent().text()
        specialties = ltk.find("#specialties input:checked").parent().text()
        toppings = ltk.find("#toppings input:checked").parent().text()
        msg = f"""
                Thank you for your order:<br>
                Pizza type: {pizza_type}<br>
                Specialties: {specialties}<br>
                Toppings: {toppings}<br>
        """
        ltk.find("#summary").html(msg)

    return(
        ltk.VBox(
            ltk.Heading1("Dave's Pizza Place"),
            
            ltk.HBox(ltk.Label("Date:"), ltk.DatePicker()),
            
            ltk.Break(),
            ltk.HBox(
                ltk.Form(
                    ltk.FieldSet(
                        ltk.Legend("Pizza type:"),
                        ltk.RadioGroup(
                            ltk.Label("Small ($8)", ltk.RadioButton(True).element),
                            ltk.Label("Medium ($10)", ltk.RadioButton(False).element),
                            ltk.Label("Large ($15)", ltk.RadioButton(False).element),
                        )
                    ).attr("id", "pizza-type")
                ),
                ltk.Form(
                    ltk.FieldSet(
                        ltk.Legend("Specialties:"),
                        ltk.RadioGroup(
                            ltk.Label("Super Cheesy ($3)", ltk.RadioButton(True).element),
                            ltk.Label("Extra Meaty ($5)", ltk.RadioButton(False).element),
                            ltk.Label("Veggie ($2)", ltk.RadioButton(False).element),
                        )
                    ).attr("id", "specialties")
                ),
                ltk.Form(
                    ltk.FieldSet(
                        ltk.Legend("Toppings:"),
                        ltk.Label("Extra Cheese ($1.50)", ltk.Checkbox(False).element),
                        ltk.Label("Pepperoni ($1.50)", ltk.Checkbox(False).element),
                        ltk.Label("Mushrooms ($1.50)", ltk.Checkbox(False).element),
                    ).attr("id", "toppings")
                ),
            ),
            ltk.Break(),
            ltk.Button("Place Order", order),
            ltk.Break(),
            ltk.Text("").attr("id", "summary")
        )
        .attr("name", "Pizza")
    )

