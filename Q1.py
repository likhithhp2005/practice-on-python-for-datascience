#Write a program to find the N-th largest element in a list.
nums = [45, 22, 89, 34, 100, 67, 54]
n = int(input("Enter N value: "))

nums.sort(reverse=True)
if n <= len(nums):
    print(f"The {n}th largest element is:", nums[n-1])
else:
    print("N is larger than the list size!")