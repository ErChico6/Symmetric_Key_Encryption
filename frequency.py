import re
# this module allows us to make computations with text
# add link documentation

import string


def clean(text_file):

    first_tbr = "\n"
    second_to_be_removed = "[^a-z]" #this refers to each non alphabetical character (the ^ stands for a negation)

    text_file = re.sub(first_tbr, " ", text_file)
    text_file = re.sub(second_to_be_removed, " ", text_file) #removes the \n and replace them it with a blank space.

    return text_file


def frequencies(text_file):

    freq_dict = {}
    text_file = cleaning(text_file)

    for character in text_file:

        if character == ' ':
            continue

        if character not in freq_dict:
            freq_dict[character] = 1

        else:
            freq_dict[character]+= 1

    freq_dict = dict(sorted(freq_dict.items(),key=lambda x:x[1],reverse=True))

    return freq_dict


def decryption(cipher_text, key):

    #I initialize an empty plaintext as base
    plaintext = ''

    alphabet = string.ascii_lowercase

    # I associate to each alphabet character the corresponding
    # 'decodification character'
    dict = {i:j for i,j in zip (alphabet, key)}

    for char in cipher_text:

        # if the character is not in the alphabet there's no
        # need to substitute it
        if char not in dict.keys():
            plaintext +=char
            continue

        for i,j in dict.items():

            if char == i:
                plaintext +=j
                break

    return plaintext
