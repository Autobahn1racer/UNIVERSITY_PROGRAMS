def para_check(word):
    stack = []
    opening_braces = ['(','{','[']
    closing_braces = [')','}',']']

    for char in word:
        if char.isalpha() and char.isalnum():
            continue
        else:
            stack.append(char)
    current_open = ""
    current_close = ""

    
    while len(stack) != 0:
        for A in stack:
            if A in opening_braces:
                current_open = A
            elif A in closing_braces:
                current_close = A
                num1 = opening_braces.index(current_open)
                num2 = closing_braces.index(current_close)
                
                if num1 != num2:
                    return "Not valid"
                else:
                    del stack[num1]
                    del stack[num2]
                print(stack)
    if len(stack)==0: return "Valid"

word = input()
print(para_check(word))

        