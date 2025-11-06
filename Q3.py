#Write a Python program to remove duplicates from a list without using set().
lst = [1, 3, 5, 3, 7, 1, 9, 5]
unique = []

for item in lst:
    if item not in unique:
        unique.append(item)

print("List after removing duplicates:", unique)