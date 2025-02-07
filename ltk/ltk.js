/* LTK - Copyright 2024 - All Rights Reserved - chrislaffra.com - See LICENSE  */

(function ltk() {
    if (window.__ltk__) return

    const start = new Date().getTime();
    window.__ltk__ = start

    const url_base = `${document.location.protocol}//${document.location.host}`
    const url_prefix = new RegExp(`${url_base}|https:\\/\\/www.|https:\\/\\/`)

    window.get_time = () => {
        return (new Date().getTime() - start)
    }

    window.to_js = json => {
        return JSON.parse(json)
    }

    window.to_py = obj => {
        try {
            return JSON.stringify(obj, null, 4)
        } catch {
            // handle cycles in obj
            copy = {}
            for (const key of Object.keys(obj)) {
                copy[key] = `${obj[key]}`;
            }
            return JSON.stringify(copy, null, 4);
        }
    }

    window.table = () => {
        return $("<table>").addClass("ltk-table");
    }

    window.tableTitle = (table, column, title) => {
        var header = table.find("tr");
        if (!header.length) {
            header = $("<tr>")
                .addClass("ltk-table-header")
                .appendTo(table);
        }
        for (var n=header.find(".ltk-table-title").length; n<=column; n++) {
            $("<th>")
                .addClass("ltk-table-title")
                .appendTo(header);
        }
        header.find(".ltk-table-title").eq(column).text(title)
    }

    window.tableCell = (table, column, row) => {
        for (var n=table.find(".ltk-table-row").length; n<=row; n++) {
            $("<tr>")
                .addClass("ltk-table-row")
                .addClass(`ltk-row-${n}`)
                .appendTo(table);
        }
        const rowElement = table.find(".ltk-table-row").eq(row)
        for (var n=rowElement.find(".ltk-table-cell").length; n<=column; n++) {
            $("<td>")
                .addClass("ltk-table-cell")
                .addClass(`ltk-row-${row}`)
                .addClass(`ltk-col-${n}`)
                .appendTo(rowElement);
        }
        return rowElement.find(".ltk-table-cell").eq(column)
    }

    window.tableGet = (table, column, row) => {
        return tableCell(table, column, row).text()
    }

    window.tableSet = (table, column, row, value) => {
        tableCell(table, column, row).text(value)
    }

    window.ltk_get = (url, success, dataType, error, headers) => {
        if (headers) {
            $.ajax({ url, dataType, headers }).done(success).fail(error)
        } else {
            $.get(url, success, dataType).fail(error)
        }
    }

    window.ltk_post = (url, data, success, dataType, error, headers) => {
        if (headers) {
            $.ajax({ url, type: "POST", data, dataType, headers }).done(success).fail(error)
        } else {
            $.post(url, data, success, dataType).fail(error)
        }
    }

    window.ltk_delete = (url, success, error) => {
        $.ajax({ url, type: "DELETE", success}).fail(error)
    }

    window.canvas = {
        line: (context, x1, y1, x2, y2) => {
            context.beginPath()
            context.moveTo(x1, y1)
            context.lineTo(x2, y2)
            context.stroke()
        },
        rect: (context, x, y, w, h) => {
            context.beginPath()
            context.rect(x, y, w, h)
            context.stroke()
        },
        text: (context, x, y, text) => {
            context.beginPath()
            context.strokeText(x, y, text)
            context.stroke()
        },
        circle: (context, x, y, radius) => {
            context.beginPath()
            context.arc(x, y, radius, 0, 2 * Math.PI)
            context.stroke()
        },
        fillCircle: (context, x, y, radius) => {
            context.beginPath()
            context.arc(x, y, radius, 0, 2 * Math.PI)
            context.fill()
        }
    };

    window.addArrow = (from, to, label) => {
        try {
            const start = from[0];
            const end = to[0];
            if (start && end) {
                return $(new LeaderLine(start, end, {
                    dash: { },
                    size: 3,
                    middleLabel: LeaderLine.pathLabel(label || "")
                })).appendTo($("body"));
            }
        } catch(e) {
            // ignore
        }
    }

    $.fn.isInViewport = function() {
        const offset = $(this).offset();
        if (!offset) return true
        const elementTop = $(this).offset().top;
        const elementBottom = elementTop + $(this).outerHeight(); 
        const viewportTop = $(window).scrollTop() + 50;
        const viewportBottom = viewportTop + $(window).height();
        return elementBottom > viewportTop && elementTop < viewportBottom;
    };

    window.getWidget = function(id) {
        return undefined;
    };
   

    $.fn.widget = function() {
        return window.getWidget($(this))
    };

    // change the following to your own development root location
    window.development_location = "C:/Users/laffr/dev/ltk";

})()