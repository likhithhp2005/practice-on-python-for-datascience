#Write a Python program to check whether a string is a palindrome.
s = input("Enter a string: ")
cleaned = ''.join(s.split()).lower()

if cleaned == cleaned[::-1]:
    print("Palindrome string")
else:
    print("Not a palindrome")