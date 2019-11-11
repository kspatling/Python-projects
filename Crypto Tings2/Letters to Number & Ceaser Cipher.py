firstString, secondString, string = "abcdef", "fedcba", "abcdef"
print("Original string:", string)
print("Translated string:", string.translate(string.maketrans(firstString, secondString)))