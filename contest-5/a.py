invalid = ["a","e","i","o","u","y"]
message = raw_input()
newWord = ""
for letter in message:
    if letter.lower() not in invalid:
        newWord += "."
        newWord += letter.lower()

print newWord