var coll = document.getElementsByClassName("collapsible");

for (let i = 0; i < coll.length; i++) {
    coll[i].addEventListener("click", function () {
        this.classList.toggle("active");

        var content = this.nextElementSibling;

        if (content.style.maxHeight) {
            content.style.maxHeight = null;
        } else {
            content.style.maxHeight = content.scrollHeight + "px";
        }

    });
}

function getTime() {
    let today = new Date();
    hours = today.getHours();
    minutes = today.getMinutes();

    if (hours < 10) {
        hours = "0" + hours;
    }

    if (minutes < 10) {
        minutes = "0" + minutes;
    }

    let time = hours + ":" + minutes;
    return time;
}

// Gets the first message
function firstBotMessage() {
    let firstMessage = "How's it going?"
    document.getElementById("botStarterMessage").innerHTML = '<p class="botText"><span>' + firstMessage + '</span></p>';

    let time = getTime();

    $("#chat-timestamp").append(time);
    document.getElementById("userInput").scrollIntoView(false);
}

firstBotMessage();

// Retrieves the responsea
async function getHardResponse(input) {
        // Simple responses
        let flag=true;
        let botHtml,result,botResponse;
        console.log(input);
        if (input == "hello") {
            result="Hello there!";
        } else if (input == "goodbye" || input== "bye") {
            result="Talk to you later!";
        } else if(input=="fine")
        {
            result="Enter the standard to get the notes"
        }
        else if(input=="1" || input=="2" || input=="3"||input=="4"||input=="5" || input=="6" ||input=="7"||input=="8"||input=="9" || input=="10"){
            sta=input
            result="Enter the subject"
        }else if(input=="Tamil" || input=="English" || input=="Maths" || input=="Science" || input=="Social Science")
        {
            sub=input
            await fetch("/search",{
                method:"POST",
                body:JSON.stringify({
                    sta,
                    sub
                })
            })
            .then(response=>response.json())
            .then(({allnotes})=>{
                if(allnotes.length)
                {
                    allnotes.forEach(note=>{
                    c=note.pdf;
                    unit=note.unit
                    result=c;
                    flag=false
                    botResponse = result;
                    botHtml='<p class="botText"><span><a href="'+botResponse+'">'+"Unit "+ unit+'</a></span></p>';
                    $("#chatbox").append(botHtml);
                    document.getElementById("chat-bar-bottom").scrollIntoView(true);
                    })
                }
                else
                {
                    result="No notes posted"
                }
            }
            );
        }
        else {
            result="Try asking something else!";
        }
        if(flag){
            botResponse = result;
            botHtml = '<p class="botText"><span>' + botResponse + '</span></p>';
            $("#chatbox").append(botHtml);
            document.getElementById("chat-bar-bottom").scrollIntoView(true);
    }
}


//Gets the text text from the input box and processes it
function getResponse() {
    let userText = $("#textInput").val();

    if (userText == "") {
        userText = "....";
    }

    let userHtml = '<p class="userText"><span>' + userText + '</span></p>';

    $("#textInput").val("");
    $("#chatbox").append(userHtml);
    document.getElementById("chat-bar-bottom").scrollIntoView(true);

    setTimeout(() => {
        getHardResponse(userText);
    }, 1000)

}

// Handles sending text via button clicks
function buttonSendText(sampleText) {
    let userHtml = '<p class="userText"><span>' + sampleText + '</span></p>';

    $("#textInput").val("");
    $("#chatbox").append(userHtml);
    document.getElementById("chat-bar-bottom").scrollIntoView(true);

    //Uncomment this if you want the bot to respond to this buttonSendText event
    // setTimeout(() => {
    //     getHardResponse(sampleText);
    // }, 1000)
}

function sendButton() {
    getResponse();
}


// Press enter to send a message
$("#textInput").keypress(function (e) {
    if (e.which == 13) {
        getResponse();
    }
});