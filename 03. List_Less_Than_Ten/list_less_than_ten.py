#print one by one

list_a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
temp = 0
while (temp < len(list_a)):
    if list_a[temp] < 5:
        print(list_a[temp])
    temp = temp + 1

#create a new list to print the result
temp = 0
new_list = []
while (temp < len(list_a)):
    if list_a[temp] < 5:
        new_list.append(list_a[temp])
    temp = temp + 1

print(new_list)
