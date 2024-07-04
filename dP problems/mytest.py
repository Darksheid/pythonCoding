from collections import Counter

def hasDuplicates(nums):
    s= Counter(nums)
    for i in s.values():
        if i > 1: return True

nums=[4,5,6]
for i,n in enumerate(nums):
    print(i,n)
