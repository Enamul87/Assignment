while True:
    inp = input("Enter two words : ")
    if not inp or inp.lower() == 'D':
        break

    words = inp.split()
    if len(words) == 1:
        print(f"You entered only one word: {words[0]}")
    elif len(words) == 2:
        word1, word2 = words
        if word1 < word2:
            print(f"The word that comes before in lexicographical order is: {word1}")
        else:
            print(f"The word that comes before in lexicographical order is: {word2}")
    else:
        print("Invalid input. Please enter only two words or 'D' to exit.")

print("Over.")

inp = input("Enter a string: ")
length = len(inp)
i = length - 1
while i >= 0:
    print(inp[i])
    i -= 1


while True:
    inp= input("Enter a string (type 'D' to exit): ")
    if inp.lower() == 'D':
        break


    special_characters = [',', '.', ':', '!', '?']
    for char in special_characters:
        inp = inp.replace(char, '')


    inp = inp.upper()
    print(inp)

