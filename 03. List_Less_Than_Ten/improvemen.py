#improvement of list
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

new_list = []
element = int(input("Enter a limitation:"))

for i in a:
    if i < element:
        new_list.append(i)

print(new_list)
