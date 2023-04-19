n =int(input())
f_in=open("input.txt", "w")

for i in range(0,n):
    f_in.write(input())
    f_in.write("\n")
f_in.close()

file = open("input.txt",'r')
max = 0
min = 1e10
for j in file:
    j = int(j)
    if max<j:
        max = j
    
    if min > j:
        min = j
    
    
print(max)
print(min)

file.close()