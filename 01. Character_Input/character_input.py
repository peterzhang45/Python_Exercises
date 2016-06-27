import datetime

now = datetime.datetime.now()

name = input("Please enter your name: ")
age = input("Please enter you age: ")

time = int(now.year)+ (100 - int(age))

string = ("Hi "+ name + ", in " + str(time) + ", you will turn 100 years old!\n")

print(string)

times = input("How many time you want to print out the previous message: ")

print(int(times) * string)
