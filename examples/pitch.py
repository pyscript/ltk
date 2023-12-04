# LTK - Copyright 2023 - All Rights Reserved - chrislaffra.com - See LICENSE 

import ltk

script = [ {
        "title": "Intro",
        "duration": 10,
        "color": "lightyellow",
        "lines": [
            "Hello, my name is Chris Laffra. I grew up in Holland.",
            "I have been a Staff Software engineer at Google and Uber.",
            "I worked with huge Python repositories at BofA and JPM.",
        ],
    }, {
        "title": "The problem",
        "duration": 15,
        "color": "lightblue",
        "lines": [
            "What I learned over 30 years as the biggest problem with Python:",
            "It is very hard to write fast and beautiful UIs in Python.",
            "The web is hard. Data scientists don't want to learn JavaScript.",
        ],
    }, {
        "title": "The solution",
        "duration": 25,
        "color": "lightgreen",
        "lines": [
            "LTK - The Little Toolkit solves these problems.",
            "It does that by leveraging a novel technology called PyScript.",
            "You can create widgets, style them, and handle events.",
            "With LTK, apps are written in a Pythonic fashion, without JS,",
            "... and deployed as static HTML files, e.g., on Github Pages.",
        ],
    }, {
        "title": "The ask",
        "duration": 10,
        "color": "pink",
        "lines": [
            "Write your own Python browser app in minutes on pyscript.com",
            "Go to the LTK kitchensink and explore the LTK examples.",
            "Visit chrislaffra.com today!",
        ],
    },
]

class ScriptPlayer(ltk.Widget):
    def __init__(self):
        ltk.Widget.__init__(self, ltk.HBox(*[
            ltk.Div(
                ltk.Div().css({
                    "position": "absolute",
                    "height": 10,
                    "margin-top": 45,
                    "background": "gray",
                }).attr("id", f"progress-{n}"),
                ltk.Text(section["title"]),
            ).css({
                "text-align": "center",
                "background": section["color"],
                "border": "3px solid gray",
                "height": 100,
                "font-size": 18,
                "width": 15 * section["duration"],
            })
            .css("overflow", "hidden")
            for n, section in enumerate(script)
        ]))

current = 0

def go():
    total = sum(section["duration"] for section in script)
    pitch = ltk.find("#pitch").css("width", 15 * total)
    (ltk.find("body")
        .empty()
        .css("margin", 200)
        .append(pitch)
    )

    def run():
        global current
        section = script[current]
        if section["tick"] == section["duration"]:
            current += 1
            if current >= len(script):
                ltk.schedule(ltk.window.document.location.reload, "reload", 3)
                return
            section = script[current]
            section["tick"] = 0
        section["tick"] += 1
        ltk.find(f"#progress-{current}").animate(ltk.to_js({"width": 15 * section["tick"]}), 500)
        lines = section["lines"]
        line_index = max(0, min(len(lines) - 1, int(-0.1 + len(lines) * section["tick"] / section["duration"])))
        line = lines[line_index]
        ltk.find(f"#pitch-line").text(line)
        ltk.schedule(run, "play next script section", 1.1)

    script[0]["tick"] = 0
    ltk.schedule(run, 1)
    ltk.find(".ltk-button").remove()


def create():
    return(
        ltk.VBox(
            ltk.Heading1("Why LTK?"),
            ScriptPlayer(),
            ltk.Text()
                .css("font-size", 35)
                .css("width", 900)
                .css("margin-top", 50)
                .css("text-align", "center")
                .attr("id", "pitch-line"),
            ltk.Button("Go!", lambda event: go())
                .css("margin", "20px 210px")
                .css("width", 92)
                .css("height", 32)
        )
        .attr("id", "pitch")
        .attr("name", "Pitch")
    )
