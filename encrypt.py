LETTERS = 'abcdefghijklmnopqrstuvwxyz'

def encrypt(initial, shift):
    
    initial = initial.lower()
    output = ""

    for char in initial:
        if char in LETTERS:
            output += LETTERS[(LETTERS.index(char) + shift) % len(LETTERS)]

    return output 