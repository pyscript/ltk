# LTK - Copyrights Reserved 2023 - chrislaffra.com - See LICENSE 

import inspect
import ltk

def get_method_doc(clazz, name):
    item = getattr(clazz, name)
    if inspect.isfunction(item):
        name = clazz.__name__ if item.__name__ == "__init__" else item.__name__
        if not name.startswith("_"):
            try:
                import textwrap
                docstring = textwrap.dedent(item.__doc__ or "").strip()
                doc = ltk.Preformatted(docstring).css("color", "darkgreen")
            except:
                doc = ltk.Span(
                    ltk.Span("⚠️ Use "),
                    ltk.Link("?runtime=py&tab=5", "Pyodide"),
                    ltk.Span(" to see doc strings") \
                ).css("color", "red")
            return ltk.LI(ltk.Text(name), doc)


def get_widget_doc(name):
    item = ltk.__dict__.get(name)
    if item and type(item) == type:
        doc = item.__doc__
        return ltk.VBox(
            ltk.H2(name),
            ltk.Text(doc),
            ltk.UL(
                list(filter(None, [
                    get_method_doc(item, method)
                    for method in dir(item)
                ])),
            ),
        )

def create():
    return (
        ltk.VBox(
            list(filter(None, [
                get_widget_doc(name)
                for name in sorted(dir(ltk))
            ]))
        )
        .css("max-height", 800)
        .css("overflow-y", "scroll")
        .attr("name", "LTK Documentation")
    )
