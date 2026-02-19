num = int(input("enter number to check Armstrong number:"))
o = len(str(num))
sum = 0
temp = num
while temp >0:
    d = temp%10
    sum = sum + d**o
    temp = temp//10

if num == sum:
    print("number is Armsrtong")
else:
    print("number is not Armstrong")    