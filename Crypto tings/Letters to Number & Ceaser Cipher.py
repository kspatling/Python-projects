running = True
running2 = True

letters = input('Word: ')
dec_enc = input('Would you like to D (Decrypt) or E (Encrypt) or BF (Brute Force):')

dec_or_enc = ['D', 'E']

letters_multiplicative_cipher = {

    '0': 'A', '1': 'A',
    '1': 'A',
    '2': 'A',
    '3': 'A',
    '4': 'A',
    '5': 'A',
    '6': 'A',
    '7': 'A',
    '8': 'A',
    '9': 'A',
    '10': 'A',
    '11': 'A',
    '12': 'A',
    '13': 'A',
    '14': 'A',
    '15': 'A',
    '16': 'A',
    '17': 'A',
    '18': 'A',
    '19': 'A',
    '20': 'A',


}

if dec_enc in str(dec_or_enc):
    key_change = input('Change key value between 1 - 25: ')

    if int(key_change) > 25:
        print('You can only choose between 1 - 25!')
        key_change = input('Change key value between 1 - 25: ')

else:
    print('Brute Force Commencing!')
    print('...')

number = len(letters)
word_split = list(letters.strip(','))
crypto = []
i = 0

bruteforce = 1

seperator = ','

if dec_enc == 'E':

    while True:

        if number == 0:

            word = ''.join(map(str, crypto))
            print(word)

            break

        change = word_split[i]

        changed = ord(change) + int(key_change)

        if changed > ord('z'):
            changed = chr(changed - 26)

        else:
            changed = chr(changed)

        crypto.append(changed)

        i = i + 1

        number = number - 1


if dec_enc == 'D':

    for x in word_split:

        output = chr((ord(x)) - int(key_change))

        crypto.append(output)

    word = ''.join(map(str, crypto))

    print(word)

if dec_enc == 'BF':

    while bruteforce <= 26:

        if bruteforce == 26:

            print('Brute Force Complete!')

            break

        for x in word_split:

            output = chr((ord(x)) - bruteforce)

            crypto.append(output)

        word = ''.join(map(str, crypto))

        print('#{}: '.format(bruteforce) + word)

        bruteforce = bruteforce + 1

        crypto = []