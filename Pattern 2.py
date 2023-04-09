n = int(input())

for i in range(0,n):
    
    if i==0:
        b = 2*n-1
        for i in range(0,b):
            print('*',end='')
        print()
        continue
    for j in range(0,i):
        print('b',end='')
    print(end='')
    
    print('*',end='')
    
    for k in range(0,n-i):
        print('i',end='')
    if i<n-1:
        print('*',end='')
    for j in range(0,i):
        print('b',end='')
    print()