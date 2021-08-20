import nltk
import re
from nltk.corpus import words, names


def encrypt(plain_text: str, key: int) -> str:
    encrypted_text = ''
    for character in plain_text:
        temp_char = character
        if temp_char.isalpha():
            shift = 97 if character.islower() else 65
            temp_char = chr((ord(character) + key - shift) % 26 + shift)
        encrypted_text += temp_char
    return encrypted_text


def decrypt(encrypted_text: str, key: int) -> str:
    return encrypt(encrypted_text, -key)


def crack(text: str) -> str:
    cracked = ""
    min_percentage_accepted = 50

    for key in range(0, 26):
        word_list = nltk.corpus.words.words()
        decrypted = decrypt(text, key)
        msg = decrypted.split()
        counter = 0
        for word in msg:
            cleaned_word = re.sub(r"[^a-zA-Z]+", "", word).lower()
            if cleaned_word in word_list:
                counter += 1

        percentage_of_english_words = int(counter / len(msg) * 100)
        if percentage_of_english_words > min_percentage_accepted:
            min_percentage_accepted = percentage_of_english_words
            cracked = decrypted

    return cracked


if __name__ == "__main__":
    print(encrypt("give me your8 hand", 15))
    print(decrypt(encrypt("Ali8", 15), 15))
    print(crack(encrypt("please5 stay away.", 15)))
