name = input("What's your name? ")

alphabet = {"A" : 1, "B" : 2, "C" : 3, "D" : 4, "E" : 5, "F" : 6, "G" : 7,
    "H" : 8, "I" : 9, "J" : 10, "K" : 11, "L" : 12, "M" : 13, "N" : 14,
    "O" : 15, "P" : 16, "Q" : 17, "R" : 18, "S" : 19, "T" : 20, "U" : 21,
    "V" : 22, "W" : 23, "X" : 24, "Y" : 25, "Z" : 26
    }

def numerify_word(string):
    string_list = list(string)
    for pos, letter in enumerate(string_list):
        letter = letter.upper()
        for key, value in alphabet.items():
            if key == letter:
                string_list[pos] = value
    return (string, string_list, sum(string_list))[2]

print(name)
