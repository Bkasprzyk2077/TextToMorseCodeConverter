data = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.',
    'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.',
    'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-',
    'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.'
}

def convert_to_morse(text: str):
    converted_data = ""
    for character in text:
        if character.upper() in data.keys():
            converted_data += data[character.upper()]
            converted_data += " "
        elif character == " ":
            converted_data += " " * 4  # Cztery spacje odpowiadają jednej dłuższej spację w kodzie Morse'a
    return converted_data
