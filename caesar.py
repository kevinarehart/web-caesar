def encrypt(text, rot):
    rotated = ""
    for letter in text:
        if letter.isalpha():
            letter = rotate_character(letter, rot)
        rotated = rotated + letter
    return rotated

def alphabet_position(letter):
    letter = letter.upper()
    value = ord(letter)
    value = value - 65
    return value

def rotate_character(char, rot):
    moving = 65
    if char.islower():
        moving =  97
    x = alphabet_position(char) + int(rot)
    if x > 25:
        x = x % 26
    string = chr(x + moving)
    return string    
