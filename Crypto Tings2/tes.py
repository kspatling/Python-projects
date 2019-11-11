with open('words.txt', 'r') as fileinput:
   for line in fileinput:
       line = line.rstrip().upper()
       f = open('word.txt', 'w')
       f.write(line)

