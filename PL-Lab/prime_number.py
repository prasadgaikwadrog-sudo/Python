n = int(input("Enter a number to check prime or not:"))
f = 0
if n==2:
    f=1
""" i = 2  
while i< n:
    if n % i== 0:
        f =0
        break
    else:
        f =1
    i=i+1"""
for i in range (2,n):
    if n%i == 0 :
       f = 0
       break
    else:
       f = 1
if f == 1:
    print("prime")
else:
    print("non-prime")        