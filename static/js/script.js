// Funkcja opóźnienia
function delay(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

// Funkcja odczytująca kod Morse'a
async function readMorse() {
    var text = document.getElementById('morse_code').value;
    var dot = new Audio('/static/sounds/dot.wav');
    var line = new Audio('/static/sounds/line.wav');

    for (let char of text) {
        console.log(char);
        if (char == '.') {
            console.log("dot");
            dot.play();
        } else if (char == '-') {
            console.log("line");
            line.play();
        } else {
            await delay(100);
        }
        await delay(100);
    }
}

// Funkcja odtwarzająca dźwięk
function playSound() {
    var audio = new Audio('/static/sounds/dot.wav');
    audio.play();
}

// Funkcja kopiująca tekst do schowka
function copyTextToClipboard() {
    var textarea = document.getElementById("plain_text");
    textarea.select(); // Zaznacz tekst w polu TextArea
    document.execCommand("copy"); // Skopiuj zaznaczony tekst do schowka
    alert("Text copied to clipboard!");
}

// Funkcja kopiująca tekst do schowka
function copyMorseToClipboard() {
    var textarea = document.getElementById("morse_code");
    textarea.select(); // Zaznacz tekst w polu TextArea
    document.execCommand("copy"); // Skopiuj zaznaczony tekst do schowka
    alert("Morse code copied to clipboard!");
}
