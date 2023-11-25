# LTK - Copyright 2023 - All Rights Reserved - chrislaffra.com - See LICENSE 

import inspect
import ltk

def link(tag):
    url = "https://developer.mozilla.org/en-US/docs/Web/HTML/Element/"
    return f"<a href={url}{tag} target=_blank>{tag}</a>"

def get_method_doc(clazz, name):
    import textwrap
    item = getattr(clazz, name)
    if inspect.isfunction(item):
        is_constructor = item.__name__ == "__init__"
        name = clazz.__name__ if is_constructor else item.__name__
        if name.startswith("_"):
            return
        signature = str(inspect.signature(item)).replace("self, ", "")
        default = f"Injects HTML element of type <{link(clazz.tag)}>" if is_constructor else ""
        docstring = (item.__doc__ or "").replace("<", "&lt;").replace("\n", "<br>")
        docstring = textwrap.dedent(f"{default}. {docstring}")
        doc = ltk.Text(docstring).css("color", "darkgreen").css("width", 500)
        return ltk.ListItem(ltk.VBox(ltk.Text(f"{name}{signature}"), doc))

def get_widget_doc(name):
    item = ltk.__dict__.get(name)
    if item and type(item) == type:
        doc = (item.__doc__ or "").replace("<", "&lt;")
        return ltk.VBox(
            ltk.Heading2(name),
            ltk.Text(doc),
            ltk.UnorderedList(
                list(filter(None, [
                    get_method_doc(item, method)
                    for method in dir(item)
                ])),
            ),
        )

def create():
    try:
        import textwrap
    except:
        return ltk.Span(
            ltk.Span("⚠️ You need to run on "),
            ltk.Link("?runtime=py&tab=8", "Pyodide"),
            ltk.Span(" to see documentation for LTK.") \
        ).css("color", "red").attr("name", "LTK Documentation")
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
