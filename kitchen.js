const runtime = document.location.hash == "#py" ? "py" : "mpy";
const start = new Date().getTime();

function setupRuntime() {
    document.location.hash = runtime;
    document.write(`<script type="${runtime}" src="kitchen.py" config="kitchen.toml"></script>`)
}

function toggleRuntime() {
    document.location.hash = runtime == "mpy" ?  "py" : "mpy";
    document.location.reload()
}

function setupToggle() {
    const toggle = document.createElement("a");
    const name = runtime == "mpy" ? "MicroPython" : "Pyodide";
    toggle.text = name;
    toggle.style = "margin-left: 12px; cursor: pointer; color: blue;"
    toggle.addEventListener("click", toggleRuntime)
    document.getElementById("title").appendChild(toggle);
}

function startTime() {
    return new Date().getTime() - start;
}

setupRuntime()
setupToggle()