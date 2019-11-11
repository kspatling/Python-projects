dict_names = []

englishWords = open('wordtest.txt', 'r')
humanNames = open('humanNames.txt', 'r')

read_englishWords = englishWords.readlines()
read_humanNames = humanNames.readlines()

for x in read_englishWords:

    dict_names.append(x.strip('\n'))

for y in read_humanNames:

    dict_names.append(y.strip('\n'))

result = any(elem in dict_names for elem in string)

print(result)

if result:

    print('Yess')

else:
    print('Nope')