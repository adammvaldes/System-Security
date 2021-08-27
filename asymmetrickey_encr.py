from subprocess import Popen, PIPE, STDOUT
import sys
import os


def subpsfunc(a, b, op):
    p = Popen(['bc'], stdout=PIPE, stdin=PIPE, stderr=PIPE)
    encode_a_b  = "{} {} {}\n".format(a,op,b).encode('utf-8')
    stdout_data = p.communicate(input=encode_a_b)[0]
    #print(stdout_data.decode('utf-8')[:-1])
    return stdout_data.decode('utf-8')[:-1]


def encrypt(m, e, n):
    #p = 283
    #q = 353
    pro = Popen(['bc', 'gcd'], stdout=PIPE, stdin=PIPE, stderr=PIPE)
    encode_m_e_n = "c = {}^{}%{}\nprint c\n".format(m, e, n).encode('utf-8')
    #encode_p = "p = {}\nq = {}\nn = p * q\ntotient_n=(p-1)*(q-1)\ne = 0\nj = 0\nfor(i=1; i<totient_n; i++) {{if (gcd(i,totient_n)==1) {{e = i; j++; if(j==7){{break;}} }} }}\nprint e, 110011\nfor(d=1; d<totient_n; d++){{ if (d * e % totient_n == 1) {{break}} }}\nprint d\n".format(
        #p, q).encode('utf-8')
    stdout_data = pro.communicate(input=encode_m_e_n)[0]
    c = stdout_data.decode('utf-8')[:]
    #print("n: " + n)
    return c


f1 = open(sys.argv[2], "r")
key_text = f1.read()
key_numbers = ""
for i in range(len(key_text)):
    if key_text[i] == " ":
        key_numbers += "\n"
        key_numbers += str(ord(key_text[i]))
        key_numbers += "\n"
        i += 1
    key_numbers += str(ord(key_text[i]))
    key_numbers += " "
#print(key_numbers)
f2 = open(sys.argv[1], "r")
public_keys = f2.read()
public_keys = public_keys.split(", ")
########
p = 283
q = 353
pro = Popen(['bc', 'gcd'], stdout=PIPE, stdin=PIPE, stderr=PIPE)
encode_p = "p = {}\nq = {}\nn = p * q\ntotient_n=(p-1)*(q-1)\ne = 0\nj = 0\nfor(i=1; i<totient_n; i++) {{if (gcd(i,totient_n)==1) {{e = i; j++; if(j==7){{break;}} }} }}\nprint e, 110011\nfor(d=1; d<totient_n; d++){{ if (d * e % totient_n == 1) {{break}} }}\nprint d\n".format(p, q).encode('utf-8')
stdout_data = pro.communicate(input=encode_p)[0]
n = stdout_data.decode('utf-8')[:]
#print(n)
v = n[14:]
v2 = v.split("110011")
e = int(v2[0])
d = int(v2[1])
#print("e: " + str(e) + " d: " + str(d))
###########
encrypted_keys = ""
key_numbers_list = key_numbers.split()
#print(text)
for i in range(10):
    encrypted_keys += str(encrypt(key_numbers_list[i], public_keys[0], public_keys[1]))
    if i < 9:
        encrypted_keys += " "
encrypted_keys += "\n" + str(encrypt(key_numbers_list[10], public_keys[0], public_keys[1])) + "\n"
for i in range(10):
    encrypted_keys += str(encrypt(key_numbers_list[i+12], public_keys[0], public_keys[1]))
    if i < 9:
        encrypted_keys += " "
cipher_filename = sys.argv[2][:len(sys.argv[1]) - 4] + "cipher"
open(cipher_filename, "w+").close()
f3 = open(cipher_filename, "a")
f3.write(encrypted_keys)
#f3 = open("wrappedKeys", "a")
#f3.write(encrypted_keys)
#c = pow(42, e) % (p*q)
#m = pow(c, d) % (p*q)
#print("m: " + str(m))
#encode_q = "q = {}\nprint q\n".format(q).encode('utf-8')
#stdout_data = pro.communicate(input=encode_q)[0]
#print(stdout_data.decode('utf-8')[:])
#return stdout_data.decode('utf-8')[:-1]
#print(public_keys)
#AsymmetricKeyEncrypter.encrypt("a")
#a = 2
#b = 3
#op = '+'
#if len(sys.argv) == 4:
#    a = sys.argv[1]
#    b = sys.argv[3]
#    op = sys.argv[2]
#    print("{} {} {}".format(a, op, b))
#x = int(subpsfunc(a, b, op)) + 2
#x = int(subpsfunc(x, 5, '='))
#subpsfunc('x', 5, '=')
#x = subpsfunc('print x','' ,'')
e = public_keys[0]
n = public_keys[1]
#print("e: " + str(e) + " n: " + str(n))
#print(subpsfunc("p", 5, "="))
#print(subpsfunc("q", 11, "="))
#print(reassign("totient_n", "p-1", "*", "q-1"))
#print(bc_print("totient_n"))
#print("gcd: " + gcd("p", "q"))
#print("gcd2: " + gcd(20, 5))
#print(str(x))
