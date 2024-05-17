data = {
    'A': '. -', 'B': '- . . .', 'C': '- . - .', 'D': '- . .', 'E': '.', 'F': '. . - .',
    'G': '- - .', 'H': '. . . .', 'I': '. .', 'J': '. - - -', 'K': '- . -', 'L': '. - . .',
    'M': '- -', 'N': '- .', 'O': '- - -', 'P': '. - - .', 'Q': '- - . -', 'R': '. - .',
    'S': '. . .', 'T': '-', 'U': '. . -', 'V': '. . . -', 'W': '. - -', 'X': '- . . -',
    'Y': '- . - -', 'Z': '- - . .', '1': '. - - - -', '2': '. . - - -', '3': '. . . - -',
    '4': '. . . . -', '5': '. . . . .', '6': '- . . . .', '7': '- - . . .', '8': '- - - . .',
    '9': '- - - - .', '0': '- - - - -', ', ': '- - . . - -', '.': '. - . - . -', '?': '. . - - . .',
    '/': '- . . - .', '-': '- . . . . -', '(': '- . - - .', ')': '- . - - . -'
}


def convert_to_morse(text: str):
    if text is None:
        return ""
    morse_code = ""
    for character in text:
        if character.upper() in data.keys():
            morse_code += data[character.upper()]
            morse_code += " " * 3
        elif character == " ":
            morse_code += " " * 7
    morse_code = morse_code.strip()
    return morse_code


def convert_to_text(morse: str):
    if morse is None:
        return ""
    text = ""
    morse = morse.strip()
    words = morse.split(" " * 7)
    print(words)
    for word in words:
        characters = word.split(" " * 3)
        for character in characters:
            if character in data.values():
                key_list = list(data.keys())
                val_list = list(data.values())
                position = val_list.index(character)
                text += key_list[position].lower()
        text += " "
    text = text.strip()
    return text
