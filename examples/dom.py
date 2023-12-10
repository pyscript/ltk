# LTK - Copyright 2023 - All Rights Reserved - chrislaffra.com - See LICENSE 

import ltk

colors = [ "#E40303", "#FF8C00", "#FFED00", "#008026", "#24408E", "#732982" ]

def create():
    def get_color():
        color = colors.pop()
        colors.insert(0, color)
        return color

    def new_text():
        return ltk.Text(f"Text created at {ltk.get_time()}s", {
            "color": "white",
            "background-color": get_color(),
        })

    def append(event):
        ltk.find("#dom-texts").append(new_text().element)

    def append_to(event):
        new_text().appendTo(ltk.find("#dom-texts"))

    def prepend(event):
        ltk.find("#dom-texts").prepend(new_text().element)

    def after(event):
        ltk.find("#dom-texts .ltk-text").eq(0).after(new_text().element)

    def before(event):
        ltk.find("#dom-texts .ltk-text").eq(1).before(new_text().element)

    def append_two(event):
        ltk.find("#dom-texts").append(
            new_text().element,
            new_text().element,
        )

    def append_html(event):
        html = ltk.create(new_text().prop("outerHTML"))
        ltk.find("#dom-texts").append(html)

    def remove_first_eq(event):
        ltk.find("#dom-texts .ltk-text").eq(0).remove()

    def remove_first_child(event):
        ltk.find("#dom-texts .ltk-text:nth-child(1)").remove()

    def remove_odd(event):
        ltk.find("#dom-texts .ltk-text:nth-child(odd)").remove()

    def remove_even(event):
        ltk.find("#dom-texts .ltk-text:nth-child(even)").remove()

    def remove_first_list(event):
        ltk.find_list("#dom-texts .ltk-text")[0].remove()

    def remove_last(event):
        ltk.find("#dom-texts .ltk-text:last-child").remove()

    def remove_all(event):
        ltk.find("#dom-texts .ltk-text").remove()

    def color(event):
        ltk.find("#dom-texts .ltk-text").css("background-color", get_color())

    ltk.inject_css("""
        #dom-demo .ltk-button {
            width: 150px;
            margin: 5px;
            background-color: var(--ltk-primary);
            color: var(--ltk-white);
            border-radius: 11px;
            padding: 14px;
        }
        #dom-demo .ltk-a {
            margin-right: 5px;
        }
        #dom-texts .ltk-text {
            margin: 5px;
        }
        #dom-demo .ltk-button.dom-remove {
            background-color: red;
        }
        #dom-demo .ltk-button.dom-color {
            background-color: orange;
            color: #111;
        }
    """)

    return (
        ltk.VBox(
            ltk.Heading1("Dynamic DOM Operations"),
            ltk.Text("We're using the following jQuery APIs: ",
                ltk.Link("https://api.jquery.com/append", "append"),
                ltk.Link("https://api.jquery.com/appendTo", "appendTo"),
                ltk.Link("https://api.jquery.com/prepend", "prepend"),
                ltk.Link("https://api.jquery.com/eq", "eq"),
                ltk.Link("https://api.jquery.com/after", "after"),
                ltk.Link("https://api.jquery.com/before", "before"),
                ltk.Link("https://api.jquery.com/css", "css"),
                ltk.Link("https://api.jquery.com/remove", "remove."),
            ),
            ltk.Container(
                ltk.Button("Append", append),
                ltk.Button("AppendTo", append_to),
                ltk.Button("Prepend", prepend),
                ltk.Button("After first", after),
                ltk.Button("Before second", before),
                ltk.Button("Append two", append_two),
                ltk.Button("Append html", append_html),

                ltk.Button("Remove first eq", remove_first_eq).addClass("dom-remove"),
                ltk.Button("Remove first child", remove_first_child).addClass("dom-remove"),
                ltk.Button("Remove first list", remove_first_list).addClass("dom-remove"),
                ltk.Button("Remove last", remove_last).addClass("dom-remove"),
                ltk.Button("Remove odd", remove_odd).addClass("dom-remove"),
                ltk.Button("Remove even", remove_even).addClass("dom-remove"),
                ltk.Button("Remove all", remove_all).addClass("dom-remove"),

                ltk.Button("Change color", color).addClass("dom-color"),
            ),
            ltk.VBox(
                new_text()
            )
            .attr("id", "dom-texts")
            .attr("background-color", "#A10F")
        )
        .width(400)
        .attr("id", "dom-demo")
        .attr("name", "DOM")
    )
