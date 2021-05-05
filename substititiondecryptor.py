# import random
#
# def generate_key():
#     letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#     # letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890,./;'[]<>?:\"{}|\!@#$%^&*()_+-= "
#     cletters = list(letters)
#     key = {}
#     for c in letters:
#         key[c] = cletters.pop(random.randint(0, len(cletters) - 1))
#     return key
#
# def encrypt(key,message):
#     cipher = ""
#     for c in message:
#         if c in key:
#             cipher += key[c]
#         else:
#             cipher += c
#     return cipher
#
# def get_decrypt_key(key):
#     dkey = {}
#     for k in key:
#         dkey[key[k]] = k
#     return dkey
#
# key = generate_key()
# print(key)
# # message= input("plesae write the message you want to encrypt:  ")
# # message = "YOU ARE AWESOME"
# # cipher = encrypt(key, message)
# cipher = input("plesae write the message you want to encrypt:  ")
# print(cipher)
# dkey = get_decrypt_key(key)
# message = encrypt(dkey, cipher)
# print(message)

import random


def generate_key():
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    cletters = list(letters)
    key = {}
    for c in letters:
        key[c] = cletters.pop(random.randint(0, len(cletters) - 1))
    return key


def encrypt(key, message):
    cipher = ""
    for c in message:
        if c in key:
            cipher += key[c]
        else:
            cipher += c
    return cipher


def get_decrypt_key(key):
    # insert code here
    dkey = {}
    for k in key:
        dkey[key[k]] = k
    return dkey

key = generate_key()
print(key)

key = generate_key()
message = "YOU ARE AWESOME"
cipher = encrypt(key, message)
print(cipher)
dkey = get_decrypt_key(key)
message = encrypt(dkey, cipher)
print(message)