#program to check if a number is a prime or not

num = int(input("Enter number: "))
# 1 is not a prime number
# 1 is an odd number
if num % 2 == 1 and num != 1:
    print("It's a prime")
else:
    print("It's not a prime")