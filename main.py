data = {}
with open("morse.csv", "r") as file:
    lines = file.readlines()
    for line in lines:
        item = line.split(",")
        data[item[0]] = item[1].strip()

