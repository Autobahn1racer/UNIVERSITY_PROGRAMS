a = "23,45.67"
b=''
for i in range (0,len(a)):
    if a[i] == ',':
        b+='.'
    elif a[i]=='.':
        b+=','
    else:
        b+=a[i]
print(b)