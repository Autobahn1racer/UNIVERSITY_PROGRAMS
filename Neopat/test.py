n = list(input())
print(n)
l = []
for i in n:
    if i == ',':
        continue
    else:
        i = int(i)
        l.append(i)

print(max(l))