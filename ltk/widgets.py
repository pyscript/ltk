# LTK - Copyrights Reserved 2023 - chrislaffra.com - See LICENSE 

import inspect
import js # type: ignore

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
shortcuts = {}


class Widget(object):
    classes = []
    instances = {}
    element = None
    tag = "div"

    def __init__(self, *children):
        self.element = (
            jQuery(f"<{self.tag}>")
                .addClass(" ".join(self.classes))
                .append(*self.flatten(children))
        )

    def flatten(self, children):
        result = []
        for child in children:
            if isinstance(child, Widget):
                result.append(child.element)
            elif inspect.isgenerator(child):
                result.extend(self.flatten(child))
            elif isinstance(child, list):
                result.extend(self.flatten(child))
            else:
                result.append(child)
        return result

    def __getattr__(self, name):
        return getattr(self.element, name)


class HBox(Widget):
    """ HBox is a widget that lays out its child widgets horizontally """
    classes = [ "ltk-hbox" ]


class VBox(Widget):
    classes = [ "ltk-vbox" ]

    
class Div(Widget):
    classes = [ "ltk-div" ]

    
class Container(Widget):
    classes = [ "ltk-container" ]

    
class Card(Container):
    classes = [ "ltk-card" ]


class Preformatted(Widget):
    classes = [ "ltk-pre" ]
    tag = "pre"


class Text(Widget):
    classes = [ "ltk-text" ]

    def __init__(self, html=""):
        Widget.__init__(self)
        self.element.html(html)
    
    
class Input(Widget):
    classes = [ "ltk-input" ]
    tag = "input"
    
    def __init__(self, value=""):
        Widget.__init__(self)
        self.element.val(value)
    
    
class Button(Widget):
    classes = [ "ltk-button" ]
    tag = "button"
    
    def __init__(self, label, click):
        Widget.__init__(self)
        self.element.text(label).on("click", proxy(click))
    
    
class Link(Text):
    classes = [ "ltk-a" ]
    tag = "a" 

    def __init__(self, href, *items):
        Widget.__init__(self, *items)
        self.attr("href", href)


class H1(Text):
    classes = [ "ltk-h1" ]
    tag = "h1"

    
class H2(Text):
    classes = [ "ltk-h2" ]
    tag = "h2"

    
class H3(Text):
    classes = [ "ltk-h3" ]
    tag = "h3"

    
class H4(Text):
    classes = [ "ltk-h4" ]
    tag = "h4"

    
class OL(Widget):
    classes = [ "ltk-ol" ]
    tag = "ol"

    
class UL(Widget):
    classes = [ "ltk-ul" ]
    tag = "ul"

    
class LI(Widget):
    classes = [ "ltk-li" ]
    tag = "li"

    
class Tabs(Widget):
    classes = [ "ltk-tabs" ]
    tag = "div"
    count = 0

    def __init__(self, *tabs):
        self.name = f"ltk-tabs-{Tabs.count}"
        Tabs.count += 1
        self.labels = UL()
        Widget.__init__(self, self.labels)
        self.attr("id", self.name)
        for tab in self.flatten(tabs):
            self.add_tab(tab)
        self.tabs()
    
    def add_tab(self, tab):
        tab_id = f"{self.name}-{self.labels.children().length}"
        print("add tab", tab, tab.attr("name"))
        self.labels.append(
            LI().append(Link(f"#{tab_id}").text(tab.attr("name")))
        )
        self.append(Div(tab).attr("id", tab_id))


class File(Widget):
    classes = [ "ltk-file" ]
    tag = "input"
    
    def __init__(self):
        Widget.__init__(self)
        self.element.attr("type", "file")
    
    
class Table(Widget):
    classes = [ "ltk-table" ]
    tag = "table"
    
    def __init__(self, *rows):
        self.element = (
            js.table()
                .addClass(" ".join(self.classes))
                .append(*self.flatten(rows))
        )

    def title(self, column, title):
        js.tableTitle(self.element, column, title)
    
    def get(self, column, row):
        return js.tableGet(self.element, column, row)

    def set(self, column, row, value):
        js.tableSet(self.element, column, row, value)
    

class TableRow(Widget):
    classes = [ "ltk-tr" ]
    tag = "tr"
    

class TableHeader(Text):
    classes = [ "ltk-th" ]
    tag = "th"
    

class TableData(Text):
    classes = [ "ltk-td" ]
    tag = "td"
    

class TextArea(Text):
    classes = [ "ltk-textarea" ]
    tag = "textarea"


class Code(Widget):
    classes = [ "ltk-code" ]
    tag = "textarea"

    def __init__(self, language, code):
        Widget.__init__(self)
        inject_script("https://cdnjs.cloudflare.com/ajax/libs/codemirror/6.65.7/codemirror.min.js")
        inject_css("https://cdnjs.cloudflare.com/ajax/libs/codemirror/6.65.7/codemirror.min.css")
        self.element.val(code)
        schedule(lambda: self.activate(language, code))
    
    def activate(self, language, code):
        js.CodeMirror.fromTextArea(self.element[0], to_js({
            "value": code,
            "mode": language,
        }))

    
class Image(Widget):
    classes = [ "ltk-image" ]
    tag = "img"
    
    def __init__(self, src):
        Widget.__init__(self)
        self.element.referrerPolicy = "referrer"
        self.element.attr("src", src)


class MenuBar(HBox):
    classes = ["ltk-menubar"]


class MenuLabel(Widget):
    classes = ["ltk-menulabel"]

    def __init__(self, label):
        Widget.__init__(self)
        self.element.text(label)


class Menu(Widget):
    classes = ["ltk-menu"]

    def __init__(self, label, *items):
        self.label = MenuLabel(label)
        self.popup = MenuPopup(*items)
        Widget.__init__(self, self.label, self.popup)
        self.label.on("click", proxy(lambda event: self.show(event)))
        self.on("mouseenter", proxy(lambda event: self.replace_other(event)))

    def replace_other(self, event):
        if find(".ltk-menupopup-open").length:
            close_all_menus()
            self.show(event)

    def show(self, event):
        close_all_menus()
        self.popup.show(self.element)
        event.preventDefault()
        return self


class Popup(Widget):
    classes = [ "popup" ]


class MenuPopup(Popup):
    classes = [ "ltk-menupopup" ]

    def show(self, element):
        close_all_menus()
        find("#main").css("opacity", 0.3)
        (self
            .appendTo(body)
            .css("top", element.offset().top + 32)
            .css("left", min(element.offset().left, body.width() - self.width() - 12))
            .addClass("ltk-menupopup-open")
        )


class MenuItem(Widget):
    classes = [ "ltk-menuitem" ]

    def __init__(self, icon, label, shortcut, selected):
        Widget.__init__(self,
            Text(icon).addClass("ltk-menuitem-icon"),
            Text(label).addClass("ltk-menuitem-label"),
            Text(shortcut).addClass("ltk-menuitem-shortcut"),
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