/* LTK - Copyrights Reserved 2023 - chrislaffra.com - See LICENSE  */

(function ltk() {
    const start = new Date().getTime();

    window.time = () => {
        return (new Date().getTime() - start)
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
})()