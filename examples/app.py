import ltk

def create():
    def handler(item):
        ltk.find("#right").append(ltk.Text(f"Menu item: {item.label}").element)
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
                ltk.VBox(ltk.Text("Left Panel"))
                    .attr("id", "left")
                    .css("border-right", "2px solid lightgray")
                    .css("padding", "50px 20px")
                    .css("background-color", "lightyellow")
                    .css("width", "20%"),
                ltk.VBox(ltk.Text("Right Panel"))
                    .attr("id", "right")
                    .css("padding", "50px 20px")
                    .css("background-color", "lightgreen")
                    .css("width", "80%"),
            ).css("border-top", "2px solid lightgray")
        )
        .attr("name", "Application")
    )