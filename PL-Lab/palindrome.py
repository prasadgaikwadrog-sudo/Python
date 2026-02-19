n = input("enter number to check Palindrome or not :")
i = n[::-1]
if i == n:
    print("number is palindrome")
else:
    print("number is not palindrome")    