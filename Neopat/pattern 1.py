n = int(input())

for i in range(0,n):
    for j in range(i,n):
        print('b',end='')
    print()
    
    print('*')
    
    for k in range(n-i,n):
        print('i')
    print()