def __init__(self, value, style=None):
    Widget.__init__(self, style or DEFAULT_CSS)
    if isinstance(value, ModelAttribute):
        self.bind(value)
    else:
        self.element.val(value)
