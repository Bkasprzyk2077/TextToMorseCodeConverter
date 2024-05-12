data = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.',
    'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.',
    'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-',
    'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.'
}


# with open("morse.csv", "r") as file:
#     lines = file.readlines()
#     for line in lines:
#         item = line.split(",")
#         data[item[0]] = item[1].strip()
#
# should_continue = True
# while should_continue:
#     user_choice = input("Enter data co convert: ")
#     converted_data = ""
#     for character in user_choice:
#         if character.upper() in data.keys():
#             converted_data += data[character.upper()]
#             converted_data += " "
#         elif character == " ":
#             converted_data += "\n"
#     print(converted_data)

def convert_to_morse(text: str):
    converted_data = ""
    for character in text:
        if character.upper() in data.keys():
            converted_data += data[character.upper()]
            converted_data += " "
        elif character == " ":
            converted_data += "   "
    return converted_data
