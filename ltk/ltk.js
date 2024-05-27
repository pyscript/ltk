/* LTK - Copyright 2023 - All Rights Reserved - chrislaffra.com - See LICENSE  */

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

    window.ltk_get = (url, success, kind, error) => {
        $.get(url, success, kind).fail(error)
    }

    window.ltk_post = (url, payload, success, kind, error) => {
        $.post(url, payload, success, kind).fail(error)
    }

    window.ltk_delete = (url, success, error) => {
        $.ajax({ url, type: "DELETE", success}).fail(error)
    }

    window.canvasRects = (context, coordinatesJson) => {
        const coordinates = JSON.parse(coordinatesJson)
        context.beginPath()
        for (var n = 0; n < coordinates.length; n += 5) {
            x = coordinates[n]
            y = coordinates[n + 1]
            w = coordinates[n + 2]
            h = coordinates[n + 3]
            context.rect(x, y, w, h)
        }
    }

    window.canvasFillRects = (context, coordinatesJson) => {
        const coordinates = JSON.parse(coordinatesJson)
        context.beginPath()
        for (var n = 0; n < coordinates.length; n += 5) {
            x = coordinates[n]
            y = coordinates[n + 1]
            w = coordinates[n + 2]
            h = coordinates[n + 3]
            context.fillStyle = coordinates[n + 4]
            context.fillRect(x, y, w, h)
        }
    }

    window.canvasDrawTexts = (context, coordinatesJson) => {
        const coordinates = JSON.parse(coordinatesJson)
        context.beginPath()
        context.strokeStyle = "red"
        for (var n = 0; n < coordinates.length; n += 5) {
            x = coordinates[n]
            y = coordinates[n + 1]
            text = coordinates[n + 2]
            color = coordinates[n + 3]
            w = coordinates[n + 4]
            context.fillStyle = color
            context.fillText(text, x, y, w)
        }
    }

    window.canvasDrawLines = (context, lineWidth, strokeStyle, coordinatesJson) => {
        const coordinates = JSON.parse(coordinatesJson)
        context.lineWidth = lineWidth
        context.strokeStyle = strokeStyle
        for (var n = 0; n < coordinates.length; n += 4) {
            context.beginPath()
            context.moveTo(coordinates[n], coordinates[n + 1])
            context.lineTo(coordinates[n + 2], coordinates[n + 3])
            context.stroke()
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
})()