#Write a program that displays how many times each element appears in a list.
lst = [2, 4, 2, 8, 4, 8, 6, 2]
freq = {}

for num in lst:
    freq[num] = freq.get(num, 0) + 1

for key, value in freq.items():
    print(f"{key} occurs {value} times")