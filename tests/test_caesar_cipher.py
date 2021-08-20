import pytest
from caesar_cipher.caesar_cipher import crack, decrypt, encrypt

# encrypt a string with a given shift
# decrypt a previously encrypted string with the same shift
# encryption should handle upper and lower case letters
# encryption should allow non-alpha characters but ignore them, including white space


@pytest.mark.parametrize(
    "input,expected_value,key",
    [
        ("I love syrup on my pancakes.", "I love syrup on my pancakes.", 3),
        ("He ran all the way to the county fair.",
         "He ran all the way to the county fair.", 15),
        ("He ran all the way to the county fair. Do You?",
         "He ran all the way to the county fair. Do You?", 6),
        ("He Ran All The Way To The County Fair.",
         "He Ran All The Way To The County Fair.", 9),
    ],
)
def test_encrypt_decrypt(input, expected_value, key):

    assert expected_value == decrypt(encrypt(input, key), key)


# decrypt encrypted version of It was the best of times, it was the worst of times. WITHOUT knowing the shift used.
def test_crack():
    encrypted = encrypt("It was the best of times, it was the worst of times.", 14)
    assert crack(encrypted) == "It was the best of times, it was the worst of times."
