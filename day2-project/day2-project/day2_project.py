import random
while True:
    decrypted =  ""
    key = 0
    encrypted = ""
    inp = ""
    enlvl = ""
    print("(E)ncrypt, (D)ecrypt, or (Q)uit")
    inp = input()
    if inp == "Q" or inp == "q":
        quit()
    if inp == "E" or inp == "e":
        print("Enryption Level? \n(L)ow, (M)edium, (H)igh")
        enlvl = input()
        if enlvl == "L" or enlvl == "l":
            key = random.randrange(0, 20)
        if enlvl == "M" or enlvl == "m":
            key = random.randrange(0, 500)
        if enlvl == "H" or enlvl == "h":
            key = random.randrange(0, 1000000)
        print("Decrypted text?")
        inp = input()
        for i in inp:
            encrypted += chr(ord(i) ^ key)
        print(encrypted)
        print("The decryption key is: " + str(key))
    if inp == "D" or inp == "d":
        print("Key?")
        key = int(input())
        print("Encrypted text?")
        inp = input()
        for i in inp:
            decrypted += chr((ord(i) ^ key))
        print(decrypted)