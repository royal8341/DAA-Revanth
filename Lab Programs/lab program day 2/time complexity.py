def constant_time(n):
 print("the time complexity of o(1)")
def linear_time(n):
 for i in range(0,n):
  print(i)
def quadratic_time(n):
 for i in range (0,n):
  for j in range (0,n):
   print(i,j)
n=int(input())
print(constant_time(n),linear_time(n),quadratic_time(n))
