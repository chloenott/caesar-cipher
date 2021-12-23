from nltk.corpus import words, names
import re
import functools

word_list, name_list = words.words(), names.words()

def encrypt(unencrypted_text, shift):
    return "".join( \
                    [chr((ord(character) + shift - 97) % 26 + 97) if re.search(r"[a-z]", character) else \
                        chr((ord(character) + shift - 65) % 26 + 65) if re.search(r"[A-Z]", character) else \
                        character \
                    for character in unencrypted_text])

def decrypt(encrypted_text, shift):
    return encrypt(encrypted_text, -shift)

def crack(encrypted_text):
    return (lambda match_proportion: \
                decrypt(encrypted_text, match_proportion.index(max(match_proportion))) if max(match_proportion) > 0.5 \
                else "" \
            )([sum([word.lower() in word_list for word in decrypt(encrypted_text, i).split()]) / len(encrypted_text.split()) for i in range(26)])