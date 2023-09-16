def caeser(user_input, n):
    output = ""
    # a loop that applies cypher to user input
    for i in range(len(user_input)):
        char = user_input[i]

        # if this char is a space, simply skip it
        if char == " ":
            output += " "
        # if char is upper case encrypt according to ASCII character
        elif (char.isupper()):
            output += chr((ord(char) + n - 65) % 26 + 65)
        # if char is lower case encrypt according to ASCII character
        elif (char.islower()):
            output += chr((ord(char) + n - 97) % 26 + 97)
        # for some reason it is some other kind of character, for this example we will output that character.
        else:
            output = user_input[i]

    return output

#user prompts and output
print("Hello! Welcome to the Caeser Cypher. \nPlease input a string of text you would like to have encrypted")
user_input = input("String: ")
n = 1
print (caeser(user_input, n))
