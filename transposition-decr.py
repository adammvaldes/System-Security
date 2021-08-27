import sys


def decrypt(cipher_text, key):
    columns = []
    for i in range(10):
        columns.append([])
    for i in range(10):
        for j in range(len(cipher_text)//10):
            columns[i].append(cipher_text[i + j * 10])
    column_order = []
    alphabetical_key = ''.join(sorted(key))
    for i in range(10):
        for j in range(10):
            if key[j] == alphabetical_key[i]:
                column_order.append(j)
    decrypted_columns = []
    for i in range(10):
        decrypted_columns.append([])
    cipher_text_index = 0
    while cipher_text_index < len(cipher_text):
        for column in decrypted_columns:
            if len(column) < len(cipher_text)//10 and cipher_text_index < len(cipher_text):
                while len(column) < len(cipher_text)//10:
                    column.append(cipher_text[cipher_text_index])
                    cipher_text_index += 1
    key_order = []
    for i in range(len(alphabetical_key)):
        for j in range(len(key)):
            if alphabetical_key[j] == key[i]:
                key_order.append(j)
    decrypted_text = ""
    for i in range(len(cipher_text)//10):
        for j in range(len(key_order)):
            decrypted_text += decrypted_columns[key_order[j]][i]
    return decrypted_text


key_file = sys.argv[2]
f1 = open(key_file, "r")
keys = f1.read()
key1 = keys[0:10]
key2 = keys[11:21]
fc3 = open(sys.argv[1], "r")
cipher_text = fc3.read()
first_decryption = decrypt(cipher_text, key2)
second_encryption = decrypt(first_decryption, key1)
txt_filename = sys.argv[1][:len(sys.argv[1])-6] + "txt"
open(txt_filename, "w+").close()
fc4 = open(txt_filename, "a")
fc4.write(second_encryption)
