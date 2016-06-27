num = input("Please input a number, this number will be determinded  as even or odd: ")
remainder = int(num) % 2
if remainder == 0:
    print("This number is even")
    if remainder == int(num) % 4:
        print("This number can be divided by 4")
else:
    print("this number is odd")
