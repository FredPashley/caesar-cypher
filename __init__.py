
"""
SEE LICENSE FILE FOR LICENSE.

Copyright (c) 2020 Freddy Pashley
"""

import string

def caesar(text, s):
    result = ""
    letters = ['abcdefghijklmnopqrstuvwxyz']
    for i in range(len(text)):
        char = text[i]

        if (char.isupper()):
            result += chr((ord(char) + s-65) % 26 + 65)
        elif (char.islower()):
            result += chr((ord(char) + s-97) % 26 + 97)
        elif char not in letters:
            result += char
    return result

def decaesar(text, s):

    alphabet = string.ascii_lowercase # "abcdefghijklmnopqrstuvwxyz"
    u_alphabet = string.ascii_uppercase # "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    encrypted_message = text
    key = s
    
    decrypted_message = ""
    for c in encrypted_message:

        if c in alphabet:
            position = alphabet.find(c)
            new_position = (position - key) % 26
            new_character = alphabet[new_position]
            decrypted_message += new_character
        elif c in u_alphabet:
            position = u_alphabet.find(c)
            new_position = (position - key) % 26
            new_character = u_alphabet[new_position]
            decrypted_message += new_character
        else:
            decrypted_message += c
    return "Key: " + str(key) + ". " + decrypted_message

