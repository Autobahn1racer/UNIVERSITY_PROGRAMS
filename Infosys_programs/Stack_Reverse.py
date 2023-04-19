def Reverse(word):

    stack = []
    reverse_word = ""

    for char in word:
        stack.append(char)
    
    while len(stack) != 0:
        reverse_word+= stack.pop()
    
    return reverse_word

word = input("Enter the word to be reversed: ")

print(Reverse(word))


