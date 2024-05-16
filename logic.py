data = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.',
    'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.',
    'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-',
    'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.'
}


def convert_to_morse(text: str):
    if text is None:
        return ""
    converted_data = ""
    for character in text:
        if character.upper() in data.keys():
            converted_data += data[character.upper()]
            converted_data += " "
        elif character == " ":
            converted_data += " " * 4
    return converted_data


def convert_to_text(morse: str):
    if morse is None:
        return ""
    converted_data = ""
    morse = morse.strip()
    words = morse.split(" ")
    for word in words:
        if word in data.values():
            key_list = list(data.keys())
            val_list = list(data.values())
            position = val_list.index(word)
            converted_data += key_list[position]
    converted_data = converted_data.strip()
    return converted_data
