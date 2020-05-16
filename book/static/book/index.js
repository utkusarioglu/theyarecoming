colorSets = [{
    "--main-bg-color-1": "#FFFFFF",
    "--main-bg-color-2": "#000000",
}, {
    "--main-bg-color-1": "#000000",
    "--main-bg-color-2": "#FFFFFF",
}]

CONSOLE = true;

function manageColorChange() {

}

function scheduleColorChange(timer, set_no) {
    setTimeout(() => changeColors(colorSet[set_no]), timer)
}

function changeColors(colorSet) {
    const root = document.documentElement;
    Object.entries(colorSet).forEach(([property, value]) => {
        CONSOLE && console.log(property, value);
        root.style.setProperty(property, value);
    });
}

function init() {
    // window.addEventListener('load', () => changeColors(colorSets[0]))
    window.addEventListener('load', () => getThings())
}

// init();

function getThings() {
    fetch("/story/1?format=json")
        .then((response) => {
            return response.json();
            // return response.body.getReader().read().then(({ done, value }) => {
            //     console.log(done, value)
            // })
        })
        .then((story_set) => {
            console.log(story_set[0])
        })
        // .then((response => {
        //     console.log(response.value)
        // }))
}