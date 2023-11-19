# LTK - Copyrights Reserved 2023 - chrislaffra.com - See LICENSE 

import inspect
from pyscript import window as js # type: ignore

from ltk.jquery import jQuery
from ltk.jquery import proxy
from ltk.jquery import find
from ltk.jquery import body
from ltk.jquery import document
from ltk.jquery import schedule
from ltk.jquery import to_js
from ltk.jquery import inject_css
from ltk.jquery import inject_script

timers = {}

BROWSER_SHORTCUTS = [ "Cmd+N","Cmd+T","Cmd+W", "Cmd+Q" ]
DEFAULT_CSS = {}
shortcuts = {}


class Widget(object):
    """Base class for LTK widgets."""
    classes = []
    instances = {}
    element = None
    tag = "div"

    def __init__(self, *args):
        """
        Initialize a new Widget instance.
        
        Args:
            *args: The content to add to this widget. Can be other widgets, strings, lists, etc.
        
        Sets:
            self.element: The jQuery element representing this widget.
        """
        self.element = (
            jQuery(f"<{self.tag}>")
                .addClass(" ".join(self.classes))
                .append(*self._flatten(args))
        )
        self._handle_css(args)

    def _handle_css(self, args):
        """Apply CSS styles passed in the args to the widget.

        Iterates through the args and checks for any that are dicts, 
        treating them as CSS style definitions to apply to the widget.
        """
        for arg in filter(lambda arg: isinstance(arg, dict), args):
            for key, value in arg.items():
                self.css(key, value)

    def _flatten(self, children):
        """Flatten a list of child widgets into a flat list.

        Arguments:
            children (list): A list of child widgets.
            Each child can be a Widget, a jQuery element. 
            Also allowed is a list or a generator of widgets.
            Finally, if one of the children is a dict, it is used to set CSS values on the receiver

        Returns:
            list: A flat list containing the child widgets and any
                grandchildren widgets.
        """
        result = []
        for child in children:
            if isinstance(child, dict):
                continue
            elif isinstance(child, Widget):
                result.append(child.element)
            elif inspect.isgenerator(child) or type(child).__name__ == "generator":
                result.extend(self._flatten(child))
            elif isinstance(child, list):
                result.extend(self._flatten(child))
            else:
                result.append(child)
        return result

    def __getattr__(self, name):
        try:
            return getattr(self.element, name)
        except AttributeError as e:
            raise AttributeError(f"Cannot find attribute '{name}' in the LTK widget {self}, nor in its jQuery element")


class HBox(Widget):
    """ Lays out its child widgets horizontally """
    classes = [ "ltk-hbox" ]


class VBox(Widget):
    """ Lays out its child widgets vertically """
    classes = [ "ltk-vbox" ]

    
class Div(Widget):
    """ Wraps a <div> """
    classes = [ "ltk-div" ]

    
class Container(Widget):
    """ Wraps a <div> """
    classes = [ "ltk-container" ]

    
class Card(Container):
    """ A container with special styling looking like a card """
    classes = [ "ltk-card" ]


class Preformatted(Widget):
    """ Wraps an HTML <pre> element """
    classes = [ "ltk-pre" ]
    tag = "pre"


class Text(Widget):
    """ A <div> to hold text """
    classes = [ "ltk-text" ]

    def __init__(self, text="", style=DEFAULT_CSS):
        Widget.__init__(self, style)
        self.element.text(str(text))
    
    
class Input(Widget):
    """ Wraps an <input> """
    classes = [ "ltk-input" ]
    tag = "input"
    
    def __init__(self, value="", style=DEFAULT_CSS):
        Widget.__init__(self, style)
        self.element.val(value)
    
    
class Button(Widget):
    """ Wraps an HTML <button> element """
    classes = [ "ltk-button" ]
    tag = "button"
    
    def __init__(self, label:str, click, style=DEFAULT_CSS):
        """
        Initialize a new Button instance.
        
        Args:
            label:str: The label for the button
            click:function(event): The event handler for this button
            style:dict [optional] CSS values to set on the element
        """
        Widget.__init__(self, style)
        self.element.text(label).on("click", proxy(click))
    
    
class Link(Text):
    """ Wraps an <a> """
    classes = [ "ltk-a" ]
    tag = "a" 

    def __init__(self, href, *items):
        Widget.__init__(self, *items)
        self.attr("href", href)


class Strong(Text):
    """ Wraps an <strong> """
    classes = [ "ltk-strong" ]
    tag = "strong"

    
class Bold(Text):
    """ Wraps an <b> """
    classes = [ "ltk-b" ]
    tag = "b"

    
class Italic(Text):
    """ Wraps an <i> """
    classes = [ "ltk-i" ]
    tag = "i"

    
class H1(Text):
    """ Wraps an <h1> """
    classes = [ "ltk-h1" ]
    tag = "h1"

    
class H2(Text):
    """ Wraps an <h2> """
    classes = [ "ltk-h2" ]
    tag = "h2"

    
class H3(Text):
    """ Wraps an <h3> """
    classes = [ "ltk-h3" ]
    tag = "h3"

    
class H4(Text):
    """ Wraps an <h4> """
    classes = [ "ltk-h4" ]
    tag = "h4"

    
class OL(Container):
    """ Wraps an <ol> """
    classes = [ "ltk-ol" ]
    tag = "ol"

    
class UL(Container):
    """ Wraps a <ul> """
    classes = [ "ltk-ul" ]
    tag = "ul"

    
class LI(Container):
    """ Wraps a <li> """
    classes = [ "ltk-li" ]
    tag = "li"
 

class Span(Widget):
    """ Wraps a <span> """
    classes = [ "ltk-span" ]
    tag = "span"

    
class Tabs(Widget):
    """ Wraps a jQueryUI tabs """
    classes = [ "ltk-tabs" ]
    tag = "div"
    count = 0

    def __init__(self, *tabs):
        self.name = f"ltk-tabs-{Tabs.count}"
        Tabs.count += 1
        self.labels = UL()
        Widget.__init__(self, self.labels)
        self.attr("id", self.name)
        for tab in self._flatten(tabs):
            self.add_tab(tab)
        self._handle_css(tabs)
        self.tabs()
    
    def add_tab(self, tab):
        tab_id = f"{self.name}-{self.labels.children().length}"
        self.labels.append(
            LI().append(Link(f"#{tab_id}").text(tab.attr("name")))
        )
        self.append(Div(tab).attr("id", tab_id))
    
    def active(self):
        return self.element.tabs("option", "active")

    def activate(self, index):
        self.element.tabs("option", "active", index)

    def get_tab(self, index):
        return self.element.find(f"li:nth-child({index + 1})")

    def get_panel(self, index):
        return self.element.children().eq(index + 1)



class File(Widget):
    """ Wraps a <input type=file> """
    classes = [ "ltk-file" ]
    tag = "input"
    
    def __init__(self, style=DEFAULT_CSS):
        Widget.__init__(self, style)
        self.element.attr("type", "file")
    
    
class Table(Widget):
    """ Wraps a <table> """
    classes = [ "ltk-table" ]
    tag = "table"
    
    def __init__(self, *rows):
        self.element = (
            js.table()
                .addClass(" ".join(self.classes))
                .append(*self._flatten(rows))
        )

    def title(self, column, title):
        js.tableTitle(self.element, column, title)
    
    def get(self, column, row):
        return js.tableGet(self.element, column, row)

    def set(self, column, row, value):
        js.tableSet(self.element, column, row, value)
    

class TableRow(Widget):
    """ Wraps a <tr> """
    classes = [ "ltk-tr" ]
    tag = "tr"
    

class TableHeader(Text):
    """ Wraps a <th> """
    classes = [ "ltk-th" ]
    tag = "th"
    

class TableData(Text):
    """ Wraps a <td> """
    classes = [ "ltk-td" ]
    tag = "td"
    

class TextArea(Text):
    """ Wraps a <textarea> """
    classes = [ "ltk-td" ]
    classes = [ "ltk-textarea" ]
    tag = "textarea"


class Code(Widget):
    """ Wraps a block of code """
    classes = [ "ltk-code" ]
    tag = "code"

    def __init__(self, language, code, style=DEFAULT_CSS):
        Widget.__init__(self, style)
        if not hasattr(js, "hljs"):
            inject_css("https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/styles/default.min.css")
            inject_script("https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/highlight.min.js")
            inject_script(f"https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/languages/{language}.min.js")
        self.element.text(code).css("opacity", 0)
        schedule(self.highlight)

    def highlight(self):
        if hasattr(js, "hljs"):
            js.hljs.highlightAll()
            self.element.animate(to_js({ "opacity": 1}))
        else:
            schedule(self.highlight, 0.1)

    
    
class Image(Widget):
    """ Wraps an <img> """
    classes = [ "ltk-image" ]
    tag = "img"
    
    def __init__(self, src, style=DEFAULT_CSS):
        Widget.__init__(self, style)
        self.element.referrerPolicy = "referrer"
        self.element.attr("src", src)


class MenuBar(HBox):
    """ Creates a horizontal menubar """
    classes = ["ltk-menubar"]


class MenuLabel(Widget):
    """ Creates a label used in menus """
    classes = ["ltk-menulabel"]

    def __init__(self, label, style=DEFAULT_CSS):
        Widget.__init__(self, style)
        self.element.text(label)


class Menu(Widget):
    """ Creates a menu """
    classes = ["ltk-menu"]

    def __init__(self, label, *items, style=DEFAULT_CSS):
        self.label = MenuLabel(label)
        self.popup = MenuPopup(*items)
        Widget.__init__(self, self.label, self.popup, style)
        self.label.on("click", proxy(lambda event: self.show(event)))
        self.on("mouseenter", proxy(lambda event: self.replace_other(event)))

    def replace_other(self, event):
        if find(".ltk-menupopup-open").length:
            close_all_menus()
            self.show(event)

    def show(self, event):
        """ Render the menu visible """
        close_all_menus()
        self.popup.show(self.element)
        event.preventDefault()
        return self


class Popup(Widget):
    """ Wraps a div that is positioned on top of all other widgets """
    classes = [ "popup" ]


class MenuPopup(Popup):
    """ Creates a menu that is a popup """
    classes = [ "ltk-menupopup" ]

    def show(self, element):
        close_all_menus()
        find("#main").css("opacity", 0.3)
        (self
            .appendTo(body)
            .css("top", element.offset().top + 28)
            .css("left", min(element.offset().left + 2, body.width() - self.width() - 12))
            .addClass("ltk-menupopup-open")
        )


class MenuItem(Widget):
    """ Creates a menuitem used inside a menu """
    classes = [ "ltk-menuitem" ]

    def __init__(self, icon, label, shortcut, selected, style=DEFAULT_CSS):
        Widget.__init__(self,
            Text(icon).addClass("ltk-menuitem-icon"),
            Text(label).addClass("ltk-menuitem-label"),
            Text(shortcut).addClass("ltk-menuitem-shortcut"),
            style
        )
        self.on("click", proxy(lambda event: self.select(event)))
        self.on("select", proxy(lambda event: self.select(event)))
        if shortcut in BROWSER_SHORTCUTS:
            raise ValueError(f"Cannot capture shortcut {shortcut} as the browser won't allow that")
        if shortcut:
            shortcuts[shortcut] = self
        self.label = label
        self.selected = selected
    
    def select(self, event):
        close_all_menus()
        self.selected(self)
        event.preventDefault()
         
        
def close_all_menus(event=None):
    if event and jQuery(event.target).hasClass("ltk-menulabel"):
        return
    find(".ltk-menupopup-open").removeClass("ltk-menupopup-open")

body.on("click", proxy(close_all_menus))


def _handle_shortcuts():
    def handle_keydown(event):
        shortcut = f"{'Cmd+' if event.metaKey else ''}{event.key.upper() if event.key else ''}"
        if shortcut in shortcuts:
            event.preventDefault()
            shortcuts[shortcut].select(event)
    document.on("keydown", proxy(handle_keydown))


_handle_shortcuts()