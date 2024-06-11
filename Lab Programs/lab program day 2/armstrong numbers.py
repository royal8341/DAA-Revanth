def armstrong(n):
    if n==0 :
     return 0
    else :
     return (n%10)**3+armstrong(n//10)
n=int(input())
o=n
result=armstrong(n)
print(result)
if result==o:
    print("true")
else:
    print("false")

