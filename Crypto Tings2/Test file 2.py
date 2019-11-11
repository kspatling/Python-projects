word = input('Enter your word: ')
caesar_multiplicative = input('Would you like to use Caesar Cipher (CC) or Multiplicative Cipher (MC)?')

word = list(word)
bruteforce_total = 1

outputchar = []
dict_names = []

multiplicative_cipher = {

    '0': 'A', '1': 'B', '2': 'C', '3': 'D', '4': 'E', '5': 'F', '6': 'G', '7': 'H', '8': 'I', '9': 'J', '10': 'K', '11': 'L', '12': 'M', '13': 'N', '14': 'O', '15': 'P', '16': 'Q', '17': 'R', '18': 'S', '19': 'T', '20': 'U', '21': 'V', '22': 'W', '23': 'X', '24': 'Y', '25': 'Z',
    'a': '0', 'b': '1', 'c': '2', 'd': '3', 'e': '4', 'f': '5', 'g': '6', 'h': '7', 'i': '8', 'j': '9', 'k': '10', 'l': '11', 'm': '12', 'n': '13', 'o': '14', 'p': '15', 'q': '16', 'r': '17', 's': '18', 't': '19', 'u': '20', 'v': '21', 'w': '22', 'x': '23', 'y': '24', 'z': '25'

}

englishWords = open('wordtest.txt', 'r')
humanNames = open('humanNames.txt', 'r')

read_englishWords = englishWords.readlines()
read_humanNames = humanNames.readlines()

for x in read_englishWords:

    dict_names.append(x.strip('\n'))

for y in read_humanNames:

    dict_names.append(y.strip('\n'))

def findInverse(inverseshift):

    inverseshift = inverseshift % 26;

    for x in range(1, 26):

        if ((inverseshift * x) % 26 == 1):

            return x

    return 1


if caesar_multiplicative == 'CC':

    dec_enc = input('Would you like to Decrypt (D) or Encrypt (E) or Brute Force (BF) your message: ')

    if dec_enc == 'E':

        key_value = input('What is your key value?: ')

        for x in word:

            output = ord(x) + int(key_value)

            if x.isupper():

                if output > ord('Z'):

                    output = output - 26

            if x.islower():

                if output > ord('z'):

                    output = output - 26

            if x == ' ':

                output = ord(x)

            try:

                if int(x) * 0 == 0:

                    output = ord(x)

            except:
                pass

            outputchar.append(chr(output))

            makeitastring = ''.join(map(str, outputchar))

        print(makeitastring)

    if dec_enc == 'D':

        key_value = input('What is your key value?: ')

        for x in word:

            output = ord(x) - int(key_value)

            if x.isupper():

                if output < ord('A'):

                    output = output + 26

            if x.islower():

                if output < ord('a'):

                    output = output + 26

            if x == ' ':

                output = ord(x)

            try:

                if int(x) * 0 == 0:

                    output = ord(x)

            except:

                pass

            outputchar.append(chr(output))

        makeitastring = ''.join(map(str, outputchar))

        print(makeitastring)

    if dec_enc == 'BF':

        if bruteforce_total >= 26:

            quit()

        while bruteforce_total < 26:

            for x in word:

                output = ord(x) - bruteforce_total

                if x.isupper():

                    if output < ord('A'):

                        output = output + 26

                if x.islower():

                    if output < ord('a'):

                        output = output + 26

                if x == ' ':

                    output = ord(x)

                try:

                    if int(x) * 0 == 0:
                        output = ord(x)

                except:

                    pass

                outputchar.append(chr(output))

            makeitastring = ''.join(map(str, outputchar))

            compare = list(makeitastring.split(' '))

            for x in compare:

                result = any(elem in compare for elem in dict_names)

                print(result)
                print(compare)

                if result:

                    print('ITS IN THEIR #{} '.format(bruteforce_total) + makeitastring)

                else:

                    print('ITS NOT IN THEIR BF #{} '.format(bruteforce_total) + makeitastring)

            makeitastring = ''.join(map(str, outputchar))

            bruteforce_total = bruteforce_total + 1

            outputchar = []

if caesar_multiplicative == 'MC':

    dec_enc = input('Would you like to Decrypt (D) or Encrypt (E) or Multiplicative Cipher or Brute Force (BF)your message: ')

    if dec_enc == 'E':

        key_value = input('What is your key?: ')

        while True:

            shift = findInverse(int(key_value))

            if shift == 1:

                key_value = input('That is an invalid key shift! What is your key?: ')

            else:

                for x in word:

                    if x == ' ':

                        output_new = ' '

                        outputchar.append(output_new)

                    if x.isupper():

                        output = (list(multiplicative_cipher.keys())[list(multiplicative_cipher.values()).index(x)])

                        output_new = ((int(output) * int(key_value)) % 26)

                        final_output = multiplicative_cipher[str(output_new)]

                        outputchar.append(final_output)

                    if x.islower():

                        output = multiplicative_cipher[str(x)]

                        output_new = ((int(output) * int(key_value)) % 26)

                        final_output = (list(multiplicative_cipher.keys())[list(multiplicative_cipher.values()).index(str(output_new))])

                        outputchar.append(final_output)

                    try:

                        if int(x) * 0 == 0:
                            outputchar.append(str(x))

                    except:

                        pass


                makeitastring = ''.join(map(str, outputchar))

                print(makeitastring)
                break

    if dec_enc == 'D':

        key_value = input('What is your key?: ')

        while True:

            shift = findInverse(int(key_value))

            if shift == 1:

                key_value = input('That is an invalid key shift! What is your key?: ')

            else:

                for x in word:

                    if x == ' ':

                        output_new = ' '

                        outputchar.append(output_new)

                    if x.isupper():

                        output = (list(multiplicative_cipher.keys())[list(multiplicative_cipher.values()).index(x)])

                        output_new = ((int(output) * int(shift)) % 26)

                        final_output = multiplicative_cipher[str(output_new)]

                        outputchar.append(final_output)

                    if x.islower():

                        output = multiplicative_cipher[str(x)]

                        output_new = ((int(output) * int(shift)) % 26)

                        final_output = (list(multiplicative_cipher.keys())[list(multiplicative_cipher.values()).index(str(output_new))])

                        outputchar.append(final_output)

                    try:

                        if int(x) * 0 == 0:
                            outputchar.append(str(x))

                    except:

                        pass

                makeitastring = ''.join(map(str, outputchar))

                print(makeitastring)
                break






