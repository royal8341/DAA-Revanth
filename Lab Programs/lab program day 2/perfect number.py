def perfect(n):
 sum=0
 for i in range(1,n):
  if (n%i==0):
      sum+=i
 return sum
n=int(input())
result=perfect(n)
if result==n:
    print("true")
else:
    print("false")

