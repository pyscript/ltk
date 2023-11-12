# LTK - Copyrights Reserved 2023 - chrislaffra.com - See LICENSE 

import ltk

# Create an HTML table to display country temperature data
# Use LTK widgets to generate the table structure

def create():
    # In this example we construct the UI by iteratively appending to a container.
    # Elements are added to the container using jQuery "append" and "appendTo" calls.
    # The table itself is created with a more declarative creation pattern.
    container = ltk.Container().attr("name", "HTML Tables")

    # DOM elements can be created using ltk objects, or directly with HTML.
    container.append(
        ltk.create("""
            <h1>
                HTML Table created in Python
            </h1>
        """)
    )

    # Resize options to be used for the first colum. We pass a Python dict 
    # to JavaScript and convert it to a map using the "to_js" function.
    resize_options = ltk.to_js({
        "handles": "e",
        "alsoResize": ".country",
    })

    ltk.Table(
        # Create a table with headers for country and temperature.
        ltk.TableRow(
            ltk.TableHeader("Country")
                .css("border-right", "2px solid orange")
                .resizable(resize_options),
            ltk.TableHeader("Yearly Average Temperature")
        ),
        # Populate the table rows with country and temperature data.
        [
            ltk.TableRow(
                ltk.TableData(country).addClass("country"),
                ltk.TableData(temperature),
            )
            for country, temperature in get_averages().items()
        ],
    ).appendTo(container)

    container.append(ltk.H4("Tip: resize the country column using the orange handle."))

    return container


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