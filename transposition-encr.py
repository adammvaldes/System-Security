import re
import sys


#Removes duplicate characters from input string then returns first 10 chars
def parse_input(input):
    k1 = input
    temp_char = ''
    i = 0
    while i < len(k1):
        temp_char = k1[i]
        k1 = re.sub(temp_char.upper(), '', k1)
        k1 = re.sub(temp_char.lower(), '', k1)
        k1 = k1[:i] + temp_char + k1[i:]
        i += 1
    return k1


def encrypt(plain_text, key):
    columns = []
    for i in range(10):
        columns.append([])
    for i in range(10):
        for j in range(len(plain_text)//10):
            columns[i].append(plain_text[i+j*10])
    column_order = []
    alphabetical_key = ''.join(sorted(key))
    for i in range(10):
        for j in range(10):
            if key[j] == alphabetical_key[i]:
                column_order.append(j)
    ordered_columns = ""
    for i in range(10):
        for j in range(len(plain_text)//10):
            ordered_columns += str(columns[column_order[i]][j])
    return ordered_columns


key_file = sys.argv[2]
f1 = open(key_file, "r")
keys = f1.read()
key1 = keys[0:10]
key2 = keys[11:21]
#key1 = input("Input k1: ")
#key1 = TranspositionEncrypter.parse_input(key1)
#while len(key1) != 10:
#    key1 = input("Your key was not 10 characters long after removing duplicates. Try another key: ")
#    key1 = TranspositionEncrypter.parse_input(key1)
#key2 = input("Input k2: ")
#key2 = TranspositionEncrypter.parse_input(key2)
#while len(key2) != 10:
#    key2 = input("Your key was not 10 characters long after removing duplicates. Try another key: ")
#    key2 = TranspositionEncrypter.parse_input(key2)
#open("keys.txt", "w+").close()
#f2 = open("keys.txt", "a")
#f2.write(key1 + " " + key2)
fc1 = open(sys.argv[1], "r")
plain_text = fc1.read()
if len(plain_text) % 10 != 0:
    for i in range(10 - (len(plain_text) % 10)):
        plain_text += "X"
text_length = len(plain_text)
cipher_filename = sys.argv[1][:len(sys.argv[1])-4] + ".cipher"
open(cipher_filename, "w+").close()
first_encryption = encrypt(plain_text, key1)
second_encryption = encrypt(first_encryption, key2)
f2 = open(cipher_filename, "a")
f2.write(second_encryption)
