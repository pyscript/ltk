# LTK - Copyright 2023 - All Rights Reserved - chrislaffra.com - See LICENSE 

import ltk

def get_averages():
    return {
        "Afghanistan": 12.6,
        "Albania": 11.4,
        "Algeria": 22.5,
        "Andorra": 7.6,
        "Angola": 21.55,
        "Antigua and Barbuda": 26,
        "Argentina": 14.8,
        "Armenia": 7.15,
        "Australia": 21.65,
    }


def create():
    resize_options = ltk.to_js({
        "handles": "e",
        "alsoResize": ".country",
    })

    return (
        ltk.Container(
            ltk.create("<h1>HTML Table created in Python</h1>"),
            ltk.Table(
                ltk.TableRow(
                    ltk.TableHeader("Country")
                        .css("border-right", "2px solid orange")
                        .resizable(resize_options),
                    ltk.TableHeader("Yearly Average Temperature")
                ),
                [
                    ltk.TableRow(
                        ltk.TableData(country).addClass("country"),
                        ltk.TableData(temperature),
                    )
                    for country, temperature in get_averages().items()
                ],
            ),
            ltk.Heading4("Tip: resize the country column using the orange handle."),
        )
        .attr("name", "HTML Tables")
    )