/* LTK - Copyrights Reserved 2023 - chrislaffra.com - See LICENSE  */

(function ltk() {
    const start = new Date().getTime();

    window.time = () => {
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

    KB = 1024
    MB = KB * KB
    GB = MB * MB

    function toHuman(byteCount) {
        if (byteCount > GB) return `${(byteCount / GB).toFixed()}GB`;
        if (byteCount > MB) return `${(byteCount / MB).toFixed()}MB`;
        if (byteCount > KB) return `${(byteCount / KB).toFixed()}KB`;
        return byteCount
    }

    new PerformanceObserver((list) => {
        for (const entry of list.getEntries()) {
            const type = entry.initiatorType[0].toUpperCase() + entry.initiatorType.slice(1);
            var kind = "Debug";
            var log = console.log
            if (entry.responseStatus !== 0 && entry.responseStatus !== 200) {
                kind = "Error";
                log = console.error;
            }
            log(
                "[Network]",
                JSON.stringify([
                    kind,
                    type,
                    toHuman(entry.encodedBodySize),
                    toHuman(entry.decodedBodySize),
                    `${entry.duration.toFixed()}ms`,
                    entry.name
                ])
            )
        }
    }).observe({
        type: "resource",
        buffered: true,
    });

    console.log("LTK: ltk.js loaded.")

})()