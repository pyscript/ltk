const search = new URLSearchParams(window.location.search);
const runtime = search.get("runtime") || "mpy";
const start = new Date().getTime();

function setupRuntime() {
    search.set("runtime", runtime);
    document.write(`<script type="${runtime}" src="kitchensink.py" config="kitchensink.toml"></script>`)
}

function toggleRuntime() {
    setSearchParameter("runtime", runtime == "mpy" ?  "py" : "mpy");
}

function setSearchParameter(key, value) {
    search.set(key, value)
    window.location.search = search.toString();
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

pyodide.setDebug(true)