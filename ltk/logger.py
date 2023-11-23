# LTK - Copyrights Reserved 2023 - chrislaffra.com - See LICENSE 

import json
import logging
from ltk.widgets import *
from ltk.pubsub import PubSubUI

logger = logging.getLogger('root')
logger.setLevel(logging.DEBUG)


class Logger(HBox):
    classes = [ "ltk-log-list ltk-hbox" ]
    level = logging.INFO
    messages = []
    icons = { 
        logging.CRITICAL : '💥',
        logging.ERROR    : '🔥️',
        logging.WARNING  : '🤔',
        logging.INFO     : 'ⓘ',
        logging.DEBUG    : '🐞',
    }
    levels = dict((value, key) for key, value in icons.items())

    def __init__(self):
        self.log_ui = VBox()
        HBox.__init__(self,
            PubSubUI(),
            self.log_ui.attr("id", "ltk-log-ui")
        )
        self.element.resizable(to_js({ "handles": "n" }))
        self.add_table()
        self.setup_logger()
        self.setup_console()
        self.setup_py_error()
        self.filter_rows()

    def add_table(self):
        self.selector = find('#ltk-log-level')
        self.element.css("opacity", 0)
        VBox(
            HBox(
                Text().text("When"),
                Text().text("Level"),
                Text().text("Message"),
            ),
            Container(
                Select(
                    [ name for name, level in sorted(self.levels.items(), key = lambda item: item[1]) ],
                    self.icons[self.level],
                    lambda _, option: self.set_level(option.text()),
                ).attr("id", "ltk-log-level"),
                Input("")
                    .attr("placeholder", "Filter")
                    .attr("id", "ltk-log-filter")
                    .on("keyup", lambda event: self.apply_filter()),
                Button("clear", lambda event: self.clear()),
                Button("x", lambda event: self.element.css("display", "none")),
            ).addClass("ltk-log-buttons")
        ).addClass("ltk-log-header").appendTo(self.log_ui.element)

    def set_level(self, selected):
        self.level = self.levels[selected]
        self.filter_rows()

    def apply_filter(self):
        self.filter_rows()

    def filter_rows(self):
        filter_text = find("#ltk-log-filter").val()
        height = 26
        rows = find_list(".ltk-log-row")
        for row in rows:
            message = row.find(".ltk-text:nth-child(3)").text()
            visible = int(row.attr("level")) >= self.level and (not filter_text or filter_text in message)
            row.css("display", "block" if visible else "none")
            if visible:
                height += 25
        find("#ltk-log-ui").css("top", "").css("height", min(250, height))

    def clear(self):
        find(".ltk-log-row").remove()
        self.filter_rows()

    def setup_logger(self):
        logger_widget = self

        class Handler(logging.StreamHandler):
            level = Logger.level
            formatter = logging.Formatter(fmt=' %(name)s :: %(levelname)-8s :: %(message)s')

            def emit(self, record):
                message = getattr(record, "msg", getattr(record, "message", "???"))
                logger_widget.add(record.levelno, message)

        logger.addHandler(Handler())

    def add(self, level, *args, **argv):
        try:
            message = " ".join(map(str, args))
            if message.startswith("js_callable_proxy"):
                return
            self.messages.append(message)
            find(".ltk-log-header").after(
                HBox(
                    Text().text(f"{time():.2f}"),
                    Text().text(Logger.icons[level]),
                    Text().text(message.replace("\n", "\\n")),
                )
                .addClass("ltk-log-row")
                .attr("level", level)
                .animate(to_js({ "height": 24  }), 700)
            )
            if level == logging.ERROR:
                console.orig_error(*args)
            else:
                console.orig_log(*args)
            self.filter_rows()
            self.element.animate(to_js({"opacity": 1}), 1300)
        except Exception as e:
            print("Log error:", e)

    def setup_console(self):
        console.orig_log = console.log
        console.orig_warn = console.warn
        console.orig_error = console.error
        console.log = self.console_log
        console.warn = self.console_log
        console.error = self.console_log
        try:
            import warnings
            warnings.warn = self.console_log
        except:
            pass # Micropython

    def setup_py_error(self):
        def find_errors():
            py_error = find(".py-error")
            if py_error.length > 0:
                lines = py_error.text().strip().split("\n")
                self.add(logging.ERROR, f"{lines[-1]}: {py_error.text()}")
                py_error.remove()
        repeat(find_errors, 1)

    def console_log(self, *args, **argv):
        try:
            if not args:
                return

            def format(arg):
                if arg.__class__.__name__ == "jsobj":
                    try:
                        return json.dumps(to_py(arg))
                    except:
                        pass
                return str(arg)

            message = " ".join(filter(None, [format(arg) for arg in args]))
            level = self.get_level(message)
            self.add(level, message)
        except Exception as e:
            print(e)

    def get_level(self, message):
        level = logging.INFO
        if "Traceback" in message or "Error" in message:
            level = logging.ERROR
        if "Debug" in message or "js_callable_proxy" in message or message.startswith("💀🔒 - Possible deadlock"):
            level = logging.DEBUG
        return level
