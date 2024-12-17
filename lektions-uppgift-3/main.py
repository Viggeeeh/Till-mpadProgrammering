UPPER = "ABCDEFGHIJKLMNOPQRSTUVWXYZÅÄÖ"
LOWER = "abcdefghijklmnopqrstuvwxyzåäö"

string_input = input("Skriv något: ")
mode = input("konvertera till upper eller lower: ")

def string_converter(string_input, mode):
    converted_string = ""
    if mode.upper() == "LOWER":
        for letter in string_input:
            if letter in UPPER:
                letter_index = UPPER.index(letter)
                converted_string += LOWER[letter_index]
            else:
                converted_string += letter  
    else:
        for letter in string_input:
            if letter in LOWER:
                letter_index = LOWER.index(letter)
                converted_string += UPPER[letter_index]
            else:
                converted_string += letter  
    return converted_string

converted_string = string_converter(string_input, mode)
print(converted_string)
