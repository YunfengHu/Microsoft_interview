'''
Two Sum (Hash Map)

Problem: Given nums and target, return indices of two numbers that add to target.

Idea: As you scan, store value -> index. For current x, look for target-x.
'''

def two_sum(nums, target):
    seen = {}
    for i,n in enumerate(nums):
        complement = target - n
        if complement in seen:
            return [i, seen[complement]]
        seen[n] = i


# Test cases
print(two_sum([3, 3, 11, 15], 6))  # [0, 1]
           