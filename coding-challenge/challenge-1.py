

def swapStrCase(string):
    i = 0
    while len(string) > i:
        character = ord(string[i])
        #i += 1
        if ord(string[i]) > 97:
            lowercase = ord(string[i]) - 32
            i += 1
            new_lowercase = chr(lowercase)
            print(new_lowercase)
        else:
            uppercase = ord(string[i]) + 32
            i += 1
            new_uppercase =chr(uppercase)
            print(new_uppercase)

swapStrCase("Hello World")