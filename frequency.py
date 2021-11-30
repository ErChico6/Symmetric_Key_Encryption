import re
import string
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

def keys(sorted_freq_corpus, sorted_freq_cipher):

    alphabet= string.ascii_lowercase
    dec_key = ''

    for alpha in alphabet:

        for i,j in zip(sorted_freq_cipher, sorted_freq_corpus):

            if alpha==i:

                dec_key+=j

    return dec_key
