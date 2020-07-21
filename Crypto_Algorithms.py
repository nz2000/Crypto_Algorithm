import sys

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
            caesarcipher(inputstate)
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
            caesarcipher(inputstate)
        else:
            sys.exit()
    
    

def caesarcipher(inputstate):
    textblock = input("Please enter the text block you would like to encrypt/decrypt: ")

    shiftvalue = int(input("Please enter the numerical value of the shift you would like to perform (This value must be a number): "))


    if (inputstate == 'encryption'):

        encryption(textblock,shiftvalue,inputstate)
        
    elif (inputstate == 'decryption'):

        decryption(textblock,shiftvalue,inputstate)

def main():

    entryvalue = int(input("Welcome to the Unified Cryptographic Algorithm Program.\nPlease enter the numerical value associated with each algorithm depending on which algorithm you wish to use.\nCaesar Cipher: 1\nPlease enter your selection here:"))
    inputstate = input("Please enter encryption or decryption, depending on your intent:")
    if entryvalue == 1:
        caesarcipher(inputstate)

main()