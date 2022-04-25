#!/usr/bin/env python3
import os, sys

# Function to convert bytes to integer by using bitwise operation OR.
def bytes_to_integer(string_in_bytes):
    i = int()
    i = 0
    for byte in string_in_bytes:
        i = i << 8
        i = i | byte
    return i

# Function to convert integer to bytes by using bitwise operation OR.
def nb(i, l): 
    o = i
    a = []
    mask = int("1"*8,2)
    for j in range(l):
        a.insert(0, o & mask)
        o >>= 8
    return bytes(a)

# Function to encrypt the file by using randomly generated key.
def encrypt(pfile, kfile, cfile):
    
    pText = b''
    with open(pfile, "rb") as fp:
        #pText = fp.read().strip()
        pText = fp.read()
    pInt = bytes_to_integer(pText)

    kText = os.urandom(len(pText))
    with open(kfile, "wb") as fp:
        fp.write(kText)
    kInt = bytes_to_integer(kText)

    cInt = pInt ^ kInt
    
    cText = nb(cInt, len(pText))
    
    with open(cfile, "wb") as fp:
        fp.write(cText)

# Function to decrypt the file.
def decrypt(cfile, kfile, pfile):
    with open(kfile, "rb") as fp:
        #kText = fp.read().strip()
        kText = fp.read()
    kInt = bytes_to_integer(kText)
    
    with open(cfile, "rb") as fp:
        #cText = fp.read().strip()
        cText = fp.read()
    cInt = bytes_to_integer(cText)
    
    pInt = cInt ^ kInt
    
    pText = b''
    with open(pfile, "wb") as fp:
        pText = nb(pInt, len(kText))
        fp.write(pText)
    #pText = nb(pInt, len(kText))

# Function to instruct how to use the program.
def usage():
    print("Usage:")
    print("encrypt <plaintext file> <output key file> <ciphertext output file>")
    print("decrypt <ciphertext file> <key file> <plaintext output file>")
    sys.exit(1)

if len(sys.argv) != 5:
    usage()
elif sys.argv[1] == 'encrypt' :
    encrypt(sys.argv[2], sys.argv[3], sys.argv[4])
elif sys.argv[1] == 'decrypt' :
    decrypt(sys.argv[2], sys.argv[3], sys.argv[4])
else:
    usage()