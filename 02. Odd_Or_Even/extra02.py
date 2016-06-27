num = int(input("Please enter a number: "))
check = int(input("Please enter a check: "))
if num % 2 == 0:
    print(num, "is even")
    if num % 4 == 0:
        print(num, "can also divided by 4")
else:
    print(num, "is odd")

if num % check == 0:
    print(num, "can divide evenly by", check)
else:
    print(num, "can't divide evenly by", check)
