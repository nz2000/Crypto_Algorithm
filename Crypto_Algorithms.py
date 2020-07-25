import sys,random,string
import numpy as np
from sympy import Matrix

def encryption(textblock,shiftvalue,inputstate):
    n = 1
    while n != 0:
        encryptedtext = ""
        for i in textblock:
            if i.isalpha():
                transitionvalue = ord(i) + shiftvalue
                if transitionvalue > ord("z"):
                    transitionvalue -= 26
            Letter = chr(transitionvalue)
            encryptedtext += Letter
        print("The encrypted value is:",encryptedtext)
        n = int(input("If you would like to end this session please enter 0, else to continue with the encryption enter 1: "))
        if n != 0:
            caesarcipher()
        else:
            sys.exit()

def decryption(textblock,shiftvalue,inputstate):
    n = 1
    while n != 0:
        decryptedvalue = ""
        for i in textblock:
            if i.isalpha():
                transitionvalue = ord(i) - shiftvalue
                if transitionvalue <ord("Z"):
                    transitionvalue += 26
            Letter = chr(transitionvalue)
            decryptedvalue += Letter
        print("The decrypted value is:",decryptedvalue)
        n = int(input("If you would like to end this session please enter 0, else to continue with the decryption enter 1: "))
        if n != 0:
            caesarcipher(i)
        else:
            sys.exit()

def caesarcipher():
    inputstate = input("Please enter encryption or decryption, depending on your intent:")
    textblock = input("Please enter the text block you would like to encrypt/decrypt: ")
    shiftvalue = int(input("Please enter the numerical value of the shift you would like to perform (This value must be a number): "))
    if (inputstate == 'encryption'):
        encryption(textblock,shiftvalue,inputstate)
    elif (inputstate == 'decryption'):
        decryption(textblock,shiftvalue,inputstate)

def encrypt(ciphercode, key,alphabet,indexvalue,charactervalue):
    encrypted = ""
    split_ciphercode = [
        ciphercode[i : i + len(key)] for i in range(0, len(ciphercode), len(key))]
    for each_split in split_ciphercode:
        i = 0
        for letter in each_split:
            number = (indexvalue[letter] + indexvalue[key[i]]) % len(alphabet)
            encrypted += charactervalue[number]
            i += 1
    return encrypted

def decrypt(cipher, key,alphabet,indexvalue,charactervalue):
    decrypted = ""
    split_encrypted = [
        cipher[i : i + len(key)] for i in range(0, len(cipher), len(key))]
    for each_split in split_encrypted:
        i = 0
        for letter in each_split:
            number = (indexvalue[letter] - indexvalue[key[i]]) % len(alphabet)
            decrypted += charactervalue[number]
            i += 1

    return decrypted

def Vigenere(alphabet,indexvalue,charactervalue,ciphercode,key,inputvalue):
    if inputvalue == 1:
        encrypted_ciphercode = encrypt(ciphercode, key,alphabet,indexvalue,charactervalue)
        print("Original ciphercode: " + ciphercode)
        print("Encrypted ciphercode: " + encrypted_ciphercode)
        return_value = int(input("Please enter 0 to quit this program, else enter 1: "))
        if return_value != 0:
            VigenereCipher()
        else:
            sys.exit()
    else:
        decrypted_ciphercode = decrypt(ciphercode, key,alphabet,indexvalue,charactervalue)
        print("Original ciphercode: " + ciphercode)
        print("Decrypted ciphercode: " + decrypted_ciphercode)
        return_value = int(input("Please enter 0 to quit this program, else enter 1: "))
        if return_value != 0:
            VigenereCipher()
        else:
            sys.exit()
    
def VigenereCipher():
    alphabet = "abcdefghijklmnopqrstuvwxyz "
    indexvalue = dict(zip(alphabet, range(len(alphabet))))
    charactervalue = dict(zip(range(len(alphabet)), alphabet))
    ciphercode = input("Please enter the text you want to work with:")
    key = input("Please enter the key for this algorithm:")
    inputvalue = int(input("Please enter 1 if you would like to encrypt the above ciphercode, for decrypting the above text please enter 2.\nPlease enter your option:"))
    Vigenere(alphabet,indexvalue,charactervalue,ciphercode,key,inputvalue)

def xor(s1, s2):
    xor_result = []
    for i in range(min(len(s1), len(s2))):
        xor_result.append(int(s1[i]) ^ int(s2[i]))  
    return xor_result

def encryptV(message, key):
    binary_message = ""
    binary_key = ""
    ciphered_text = ""

    for letter in message:
        binary_message += format(ord(letter), "b")

    for letter in key:
        binary_key += format(ord(letter), "b")

    cipher_binary = xor(binary_message, binary_key)

    return "".join(str(e) for e in cipher_binary)

def decryptV(cipher_text, key):
    binary_key = ""
    decrypted_text = ""

    for letter in key:
        binary_key += format(ord(letter), "b")

    binary_message = xor(cipher_text, binary_key)

    for i in range(0, len(binary_message), 7):
        letter = "".join(str(e) for e in binary_message[i : i + 7])
        decrypted_text += chr(int(letter, 2))

    return decrypted_text

def VernamCipher(message,key):
    inputstatus = int(input("If you would like to perform Encryption type 1, else type 2: "))
    encrypted = encryptV(message, key)
    decrypted = decryptV(encrypted, key)
    if inputstatus == 1:
        print("Original message: " + str(message))
        print("The key used was: " + key)
        print("Encrypted message (in binary): " + str(encrypted))
        return_value = int(input("Please enter 0 to quit this program, else enter 1: "))
        if return_value != 0:
            Vernam()
        else:
            sys.exit()
    else:
        print("Original message: " + str(message))
        print("The key used was: " + key)
        print("Decrypted message: " + str(decrypted))
        return_value = int(input("Please enter 0 to quit this program, else enter 1: "))
        if return_value != 0:
            Vernam()
        else:
            sys.exit()

def Vernam():
    message = input("plz input the message:")
    choice = int(input("Do you have your own key, if yes type 1, else type 2:"))
    if choice == 1:
        key = input("Please enter your given key:")
    else:
        key = "".join(random.choice(string.ascii_letters) for i in range(len(message)))
    VernamCipher(message,key)

def getKeyMatrix(key):
    k = 0
    for i in range(3):
        for j in range(3):
            np.keyMatrix[i][j] = ord(key[k]) % 65
            k += 1

def encrypthill(messageVector,cipherMatrix):
    for i in range(3):
        for j in range(1):
            cipherMatrix[i][j] = 0
        for x in range(3):
            cipherMatrix[i][j] += (np.keyMatrix[i][x] * messageVector[x][j])
            cipherMatrix[i][j] = cipherMatrix[i][j] % 26

def HillCipher1(messageVector,cipherMatrix):
    message = input("Enter 3 no. of string: ")
    message = message.upper()
    key = input("Enter the Key:")
    key = key.upper()
    getKeyMatrix(key)
    for i in range(3):
        messageVector[i][0] = ord(message[i]) % 65
    encrypthill(messageVector,cipherMatrix)
    CipherText = []
    for i in range(3):
        CipherText.append(chr(cipherMatrix[i][0] + 65))
    print("Ciphertext: ", "".join(CipherText))
    inputvariable = int(input("To restart this program please enter 1, to end this program enter 0: "))
    if inputvariable == 0:
        sys.exit()
    else:
        Hill()

def getInverseKeyMatrix(key):
    getKeyMatrix(key)
    keyMatrix=np.keyMatrix
    
    inverseKeyMatrix = Matrix(keyMatrix).inv_mod(26)
    np.inverseKeyMatrix = np.array(inverseKeyMatrix)

def HillCipher2(plainMatrix, messageVector):
    message = input("Enter 3 no. of string: ")
    message = message.upper()
    key = input("Enter the Key:")
    key = key.upper()
    getInverseKeyMatrix(key)
    for i in range(3):
        messageVector[i][0] = ord(message[i]) % 65
    decrypthill(messageVector,plainMatrix)
    PlainText = []
    for i in range(3):
        PlainText.append(chr(int(round(plainMatrix[i][0]) + 65)))
    print("Plaintext: ", "".join(PlainText))
    inputvariable = int(input("To restart this program please enter 1, to end this program enter 0: "))
    if inputvariable == 0:
        sys.exit()
    else:
        Hill()

def decrypthill(messageVector,plainMatrix):
    for i in range(3):
        for j in range(1):
            plainMatrix[i][j] = 0
        for x in range(3):
            plainMatrix[i][j] = plainMatrix[i][j] % 26
            plainMatrix[i][j] += (np.inverseKeyMatrix[i][x] * messageVector[x][j])
        plainMatrix[i][j] = plainMatrix[i][j] % 26

def Hill():
    np.keyMatrix = [[0] * 3 for i in range(3)]
    messageVector = [[0] for i in range(3)]
    cipherMatrix = [[0] for i in range(3)]
    plainMatrix = [[0] for i in range(3)]
    np.inverseKeyMatrix = [[0] * 3 for i in range(3)]
    ch=int(input("For Encryption enter 1, for Decryption enter 2: "))
    if ch == 1:
        HillCipher1(messageVector,cipherMatrix)
    elif ch == 2:
        HillCipher2(plainMatrix, messageVector)

def main():
    entryvalue = int(input("Welcome to the Unified Cryptographic Algorithm Program.\nPlease enter the numerical value associated with each algorithm depending on which algorithm you wish to use.\nCaesar Cipher: 1\nVigenere Cipher: 2\nVernam Cipher: 3\nHill Cipher: 4\nPlease enter your selection here:"))
    if entryvalue == 1:
        caesarcipher()
    elif entryvalue == 2:
        VigenereCipher()
    elif entryvalue == 3:
        Vernam()
    elif entryvalue == 4:
        Hill()

main()