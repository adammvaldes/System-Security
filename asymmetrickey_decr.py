from subprocess import Popen, PIPE, STDOUT
import sys
import os


def decrypt(c, d, n):
    pro = Popen(['bc', 'gcd'], stdout=PIPE, stdin=PIPE, stderr=PIPE)
    encode_c_d_n = "m = {}^{}%{}\nprint m\n".format(c, d, n).encode('utf-8')
    stdout_data = pro.communicate(input=encode_c_d_n)[0]
    m = stdout_data.decode('utf-8')[:]
    return m


f1 = open(sys.argv[2], "r")
key_text = f1.read()
key_numbers = ""
key_numbers_list = key_text.split()
f2 = open(sys.argv[1], "r")
private_keys = f2.read()
private_keys = private_keys.split(", ")
d = private_keys[0]
n = private_keys[1]
decrypted_keys = ""
for i in range(len(key_numbers_list)):
    decrypted_keys += chr(int(decrypt(key_numbers_list[i], d, n)))
txt_filename = sys.argv[2][:len(sys.argv[1])-6] + ".txt"
open(txt_filename, "w+").close()
f3 = open(txt_filename, "a")
f3.write(decrypted_keys)
