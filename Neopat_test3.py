a = input()
l1 = int(a[0])
l2 = int(a[2])
l3 = int(a[4])
r = int(a[6])

t1 = input()
t1=list(t1)
for i in range (0,3):
    if t1[i] == ' ':
        t1.pop(i)
t1[l1] = r
t1=tuple(t1)

t2 = input()
t2=list(t2)
for i in range (0,3):
    if t2[i] == ' ':
        t2.pop(i)
t2[l2] = r
t2=tuple(t2)

t3 = input()
t3=list(t3)
for i in range (0,3):
    if t3[i] == ' ':
        t3.pop(i)
t3[l3] = r
t3=tuple(t3)

L1=[]

L1.append(t1)
L1.append(t2)
L1.append(t3)

print(L1)



