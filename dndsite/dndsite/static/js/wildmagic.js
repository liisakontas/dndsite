let startResult = document.getElementById("start_roll_result")
let selectionInput = document.getElementById("selection_input")
let selectionRoll = document.getElementById("selection_roll")
let selectionResult = document.getElementById("selection_roll_result")
let roll1Value = document.getElementById("roll_para_value")
let roll1Url = document.getElementById("roll_para_url")
let roll1Text = document.getElementById("roll_para")
let roll2Url = document.getElementById("roll_para_2_url")
let roll2Text = document.getElementById("roll_para_2")
let roll2Value = document.getElementById("roll_para_2_value")

async function rollD6() {
    selectionInput.setAttribute("hidden", "")
    selectionRoll.setAttribute("hidden", "")
    roll1Url.setAttribute("hidden", "")
    roll1Text.setAttribute("hidden", "")
    selectionResult.setAttribute("hidden", "")
    roll = Math.floor(Math.random()*6) + 1
    if (roll == 1){
        wmt = Math.floor(Math.random()*100) + 1
        dataDict = await getWildMagicValue(wmt)
        roll1Text.innerText  = dataDict.effect
        roll1Text.removeAttribute("hidden");
        if (dataDict.url){
            roll1Url.href = dataDict.url
            roll1Url.removeAttribute("hidden");
        }
        else {
            roll1Url.setAttribute("hidden", "")
        }
    }
    roll1Value.innerText = "Got roll: " + roll
    startResult.removeAttribute("hidden");
    if (roll==6){
        selectionInput.removeAttribute("hidden");
        selectionRoll.removeAttribute("hidden");
    }
}

async function rollD10() {
    min = parseInt(document.getElementById("d10_input").value)
    max = min + 9;
    result = Math.floor(Math.random() * (max - min + 1) + min); 
    dataDict = await getWildMagicValue(result)
    selectionResult.removeAttribute("hidden");
    roll2Url.setAttribute("hidden", "")
    roll2Text.removeAttribute("hidden");
    roll2Value.removeAttribute("hidden");
    roll2Text.innerText = dataDict.effect
    roll2Value.innerText = "Got roll: " + result
    if (dataDict.url){
        roll2Url.href = dataDict.url
        roll2Url.removeAttribute("hidden");
    }
    else {
        roll2Url.setAttribute("hidden", "")
    }
}

async function getWildMagicValue(value) {
    let response = await fetch("/api/getwildmagicvalue/" + value + "/", {
        method: "GET",
        mode: "cors", 
        credentials: "same-origin",
        headers: {
          'X-CSRFToken': csrfToken,
        },
        referrerPolicy: "no-referrer", 
      });
      return(response.json());
}