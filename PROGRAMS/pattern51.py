n=int(input("enter the range of the pattern"))
for i in range(1,n+1):
    for j in range(1,(n-i)+1):
        print(end=' ')
    for k in range(1,i+1):
        print(i,end=' ')
    print()
n=n-1
for i in range(n,0,-1):
    for j in range(1,(n-i)+2):
        print(end=' ')
    for k in range(1,i+1):
        print(i,end=' ')
    print()
