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

REPLACEMENTS = [
    ["name", "Jonas"],
]

function doStringReplacements(raw_string, replacements) {
    replacements.forEach(([find, replace]) => {
        raw_string = raw_string.split(`<<${find}>>`).join(replace);
    })
    return raw_string;
}

function init() {
    window.addEventListener('load', async() => {})
    updateStory(1)
}

init();

async function updateStory(id) {
    const story_graph = (await getStoryGraph(id)).data.story
    printStory(story_graph)
}

function printStory(story_graph) {
    const story_body = doStringReplacements(story_graph.body, REPLACEMENTS);
    const story_title = story_graph.title;
    document.getElementsByClassName("story_title")[0].innerText = story_title
    document.getElementsByClassName("story_body")[0].innerText = story_body

    const choices = document.getElementsByClassName("choices")[0];
    choices.innerHTML = "";
    story_graph.choices.forEach((choice) => {
        a = document.createElement("a");
        a.href = `javascript:updateStory(${choice.nextStory.id})`;
        div = document.createElement("div")
        div.className = "choice_body";
        p = document.createElement("p")
        p.innerText = doStringReplacements(choice.body, REPLACEMENTS);

        div.appendChild(p)
        a.appendChild(div)
        choices.appendChild(a)
    });
}

async function getStoryGraph(id) {
    const csrfToken = getCookie('csrftoken');
    const qlStr = { query: `query{ story(id:${id}) { title body choices{ body nextStory{ id }} }}` }
    return fetch('/graphql/', {
            method: 'POST',
            headers: {
                'X-CSRFToken': csrfToken,
                'Content-Type': 'application/json',
                'Accept': 'application/json',
            },
            body: JSON.stringify(qlStr)
        })
        .then(r => r.json())
}

function getCookie(name) {
    if (!document.cookie) {
        return null;
    }

    const cookie = document.cookie.split(';')
        .map(c => c.trim())
        .filter(c => c.startsWith(name + '='));

    if (cookie.length === 0) {
        return null;
    }
    return decodeURIComponent(cookie[0].split('=')[1]);
}