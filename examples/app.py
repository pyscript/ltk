# LTK - Copyrights Reserved 2023 - chrislaffra.com - See LICENSE 

import ltk

def create():
    def handler(item):
        ltk.find("#right").append(ltk.Bold(f"Selected menu item: {item.label}").element)

    left_css = {
        "border-right": "2px solid lightgray",
        "padding": "50px 20px",
        "background-color": "lightyellow",
        "width": "20%",
    }

    right_css = {
        "padding": 0,
        "background-color": "lightgreen",
        "width": "80%",
    }

    return (
        ltk.VBox(
            ltk.MenuBar(
                ltk.Menu("File",
                    ltk.MenuItem("➕", "New", "", handler),
                    ltk.MenuItem("📂", "Open", "Cmd+O", handler),
                ),
                ltk.Menu("Edit",
                    ltk.MenuItem("✂️", "Copy", "Cmd+C", handler),
                    ltk.MenuItem("📋", "Paste", "Cmd+V", handler),
                ),
            ).css("background-color", "lightblue"),
            ltk.HBox(
                ltk.VBox(ltk.Text("Left Panel"), left_css),
                ltk.VBox(ltk.Text("Right Panel"), right_css).attr("id", "right")
            ).css("border-top", "2px solid lightgray")
        )
        .attr("name", "Application")
    )