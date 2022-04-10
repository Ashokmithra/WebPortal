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

function StaterMessage() {
    let fmessage = "Hi,Enter your standard to get the notes"
    botHtml='<p class="botText"><span>'+ fmessage+'</span></p>';
    $("#chatbox").append(botHtml);
    document.getElementById("chat-bar-bottom").scrollIntoView(true);
}

StaterMessage();

async function getHardResponse(input) {
        let flag=true,checking=false;
        let botHtml,result,botResponse;
        console.log(input);
        if(input=="1" || input=="2" || input=="3"||input=="4"||input=="5" || input=="6" ||input=="7"||input=="8"||input=="9" || input=="10"){
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
                    botHtml='<p class="botText"><span><a  href="'+botResponse+'">'+"Unit "+ unit+'</a></span></p>';
                    $("#chatbox").append(botHtml);
                    document.getElementById("chat-bar-bottom").scrollIntoView(true);
                    })
                    StaterMessage();
                }
                else
                {
                    checking=true
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
            if(checking){StaterMessage();}

    }
}


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

function buttonSendText(sampleText) {
    let userHtml = '<p class="userText"><span>' + sampleText + '</span></p>';

    $("#textInput").val("");
    $("#chatbox").append(userHtml);
    document.getElementById("chat-bar-bottom").scrollIntoView(true);


}

function sendButton() {
    getResponse();
}


$("#textInput").keypress(function (e) {
    if (e.which == 13) {
        getResponse();
    }
});