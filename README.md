# ltk
LTK is a little toolkit for writing UIs in PyScript. For examples see:

 - The [LTK kitchensink](https://laffra.github.io/ltk/) for a live demo of all the widgets.
 - Why use LTK? See the [pitch](https://laffra.github.io/ltk/?tab=9), written with LTK, of course.
 - The [docs rendered using LTK](https://laffra.github.io/ltk/?runtime=py&tab=8).
 - A personal website, [chrislaffra.com](https://chrislaffra.com), which uses a number of animations, svg, styling, and timers to render a visual resume.
 - An animated [Holiday card](https://laffra.pyscriptapps.com/merry-christmas/latest/) where PyScript logo tree ornaments are animated using Python code in the browser using LTK.
   
LTK is implemented as a declarative Python library and leverages `jQuery` for DOM operations.

## Installing LTK

Install LTK from pypi:
```
python3 -m pip install pyscript-ltk
```
## Hello World

```python
import ltk

ltk.Text("Hello World").appendTo(ltk.body)
```

## Getting Started

To get started with LTK, we recommend you try it out on pyscript.com:
 -  [Minimal LTK with MicroPython](https://pyscript.com/@laffra/ltk-on-micropython/latest)
 -  [Minimal LTK with PyOdide](https://pyscript.com/@laffra/ltk-on-pyodide/latest)

## Widget Specification

New widget types are created by subclassing `ltk.Widget`:

```python
class HBox(Widget):
    classes = [ "ltk-hbox" ]
```

By default, widgets are created as `div` DOM elements. You can choose a different tag:

```python
class Preformatted(Widget):
    classes = [ "ltk-pre" ]
    tag = "pre"
```

## Creating a UI

To create a UI, elements are constructed declaratively:

```python
ltk.Table(
    ltk.TableRow(
        ltk.TableHeader("header1")
        ltk.TableHeader("header2")
    ),
    [
        ltk.TableRow(
            ltk.TableData(value1),
            ltk.TableData(value2),
        )
        for value1, value2 in data
    ],
)
```

Widgets are added to others by using `jQuery`'s `append` and `appendTo` calls:
```python
ltk.body.append(
    ltk.Table(...).element
)

container = ltk.VBox(...)
ltk.H1("This is a header").appendTo(container)
```

When an LTK widget is created, a corresponding jQuery element is attached to it in 
the `ltk.Widget.__init__` constructor. It uses the `tag` value defined by the 
declaring class and the constructed element is referred to as `element`.
As the `append` call is a JavaScript function, implemented by jQuery, we do not
pass the LTK widget directly, but pass its `element` to append to the DOM.

## Styling

Widgets can be styled using using three different approaches:

1. Styling with element styles using `jQuery`'s `css` function:
```python
ltk.Text("Error: Flux capacitor low!")
    .css("background-color", "red")
    .css("color", "white")
    .css("padding", 8)
```

2. Styling using a `dict` to make it easier to share styles:
```python
error = {
    "background-color": "red",
    "color": "white",
    "padding": 8,
}
ltk.Text("Error: Flux capacitor low!", error)
```

3. Styling using CSS classes and an external stylesheet, using `jQuery`'s `addClass` function:
```python
ltk.Text("Some text").addClass("my-special-text)
```
The external style sheet should have these rules:
```css
.ltk-text {
    font-family: Arial;
}

.my-special-text {
    font-family: Courier;
    background-color: red;
    color: white;
    padding: 8px;
}
```

External stylesheets can be included in the original `index.html` or injected at runtime from Python using:
```python
ltk.inject_style("https://example.org/awesome_styles.css")
```

## Events

Event handlers are attached using `jQuery` mechanisms. 
```python
def buy(event):
    purchase(...)

ltk.Card("Buy Now").on("click", ltk.proxy(buy))
```

You can also use the more declarative decorator:
```python
@ltk.callback
def buy(event):
    purchase(...)

ltk.Card("Buy Now").on("click", buy)
```

## Examples

See the [LTK kitchensink](https://laffra.github.io/ltk/) or explore the `examples` folder

## Applications built using LTK

- PySheets (more details soon)

## License

LTK is covered under the Apache License:

 - The Apache license is a permissive open source software license.

 - It allows users to freely use, modify, and distribute the software (including for commercial purposes).

 - Modified versions can be distributed without having to release the source code. Though source code changes should be documented.

 - The license requires modified versions to retain the Apache license and copyright notice.

 - The software is provided by the authors "as is" with no warranties.

 - Users are not granted patent rights by contributors, but contributors cannot revoke patent grants for previous contributions.

 - The license does not require derived works to adopt the Apache license. Though this is encouraged for consistency.



## Upload new version to PyPi

First build the package into a source distribution and a Python wheel:
```console
python3 -m pip install --user --upgrade setuptools wheel twine build
python3 -m build
```

Then verify whether the build works for pypi:
```console
twine check dist/*
```

Then upload to the pypi test environment:
```console
twine upload --repository pypitest dist/*
```

Finally, if the pypi test upload appears to work fine, run:
```console
twine upload dist/*
```
