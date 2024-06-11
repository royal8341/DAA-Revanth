def fibb(n):
    if(n==0 or n==1):
        return n
    else:
        return fibb(n-1)+fibb(n-2)
n=int(input())
for i in range(1,n):
    print(fibb(i))
