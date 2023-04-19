f_in = open("numbers.txt",'w')
f_in.write("123\n4\n98\n34\n34\n2323\n233")
f_in.close()

with open("numbers.txt") as f:
    sum = 0
    for n in f:
        n = n.strip()
        sum = sum + int(n)

print(sum)


