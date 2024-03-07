# LTK - Copyright 2023 - All Rights Reserved - chrislaffra.com - See LICENSE 

import ltk


class Step(ltk.Div):
    classes = [ "ltk-bubble" ]

    def __init__(self, widget, content):
        ltk.Div.__init__(self, content)
        self.content = content
        self.widget = widget
        self.css("font-family", "Arial")
        self.css("position", "absolute")
        self.css("top", -1000)
        self.css("left", -1000)
        self.css("background", "lightyellow")
        self.css("border", "5px solid gray")
        self.css("overflow", "hidden")
        self.css("border-radius", 15)
        self.css("padding", 5)
        self.appendTo(ltk.find("body"))
        self.width = self.width()
        self.height = self.height()
        self.draggable()

    def show(self):
        self.css("width", 0)
        self.css("height", 0)
        self.css("top", self.widget.offset().top)
        self.css("left", self.widget.offset().left + self.widget.width() + 28)
        self.animate(ltk.to_js({
            "width": self.width + 5,
            "height": self.height,
        }))

    def hide(self):
        self.animate(ltk.to_js({
            "width": 0,
            "height": 0,
        }), 250, ltk.proxy(lambda: self.remove()))

class Tutorial():
    def __init__(self, steps):
        self.steps = steps
        self.index = 0
        self.current = None
        self.steps = steps

    def run(self):
        self.index = 0
        self.show()
        
    def next(self):
        if self.current:
            self.current.hide()
        self.index += 1
        if self.index < len(self.steps):
            self.show()

    def show(self):
        selector, event, content = self.steps[self.index]
        widget = ltk.find(selector)
        self.current = Step(widget, content)
        self.current.show()
        widget.on(event, ltk.proxy(lambda *args: self.next()))


def tutorial():
    return Tutorial([
        (
            "#hello-button",
            "click",
            ltk.Text("First, click the Hello button."),
        ),
        (
            "#world-button",
            "click",
            ltk.Text("Then, click the World button."),
        ),
])


def create():
    return (
        ltk.VBox(
            ltk.Button("Hello", lambda event: print("hello"))
                .css("margin", 20)
                .css("font-size", 32)
                .css("background", "lightgreen")
                .css("border-radius", 10)
                .attr("id", "hello-button"),
            ltk.Button("World", lambda event: print("world"))
                .css("margin", 20)
                .css("background", "lightblue")
                .css("border-radius", 10)
                .css("font-size", 32)
                .attr("id", "world-button"),

            ltk.Button("start the tutorial", lambda event: tutorial().run())
                .css("margin", 20)
                .css("margin-top", 60)
        )
        .css("height", 800)
        .attr("name", "Tutorial")
    )
