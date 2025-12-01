let selectedPeer = null;

// ==========================
// Fetch Peers
// ==========================
async function loadPeers() {
    let res = await fetch("/peers");
    let data = await res.json();

    let peerList = document.getElementById("peerList");
    peerList.innerHTML = "";

    Object.keys(data).forEach(ip => {
        let div = document.createElement("div");
        div.className = "peer";
        div.innerText = ip;

        div.onclick = () => {
            selectedPeer = ip;
            alert("Chatting with: " + ip);
        };

        peerList.appendChild(div);
    });
}

// ==========================
// Fetch Messages
// ==========================
async function loadMessages() {
    let res = await fetch("/messages");
    let data = await res.json();

    let msgBox = document.getElementById("messages");
    msgBox.innerHTML = "";

    data.forEach(msg => {
        let p = document.createElement("p");
        p.innerText = msg;
        msgBox.appendChild(p);
    });

    msgBox.scrollTop = msgBox.scrollHeight;
}

// ==========================
// Send Message
// ==========================
async function sendMessage() {
    if (!selectedPeer) {
        alert("Select a peer first!");
        return;
    }

    let msgInput = document.getElementById("messageInput");
    let text = msgInput.value.trim();

    if (!text) return;

    await fetch("/send", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            ip: selectedPeer,
            msg: text
        })
    });

    msgInput.value = "";
}

document.getElementById("sendBtn").onclick = sendMessage;

// ==========================
// Auto refresh peers + messages
// ==========================
setInterval(loadPeers, 2000);
setInterval(loadMessages, 1000);
