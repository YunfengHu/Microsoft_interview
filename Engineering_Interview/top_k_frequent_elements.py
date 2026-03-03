'''
Question 2 — Top K Frequent Elements (Applied Scientist Favorite)

Problem:
Given an integer array nums and integer k, return the k most frequent elements.

nums = [1,1,1,3,2,2]
k = 2
Output: [1,2]
'''

from collections import Counter

def topKFrequent(nums, k):
    # Count the frequency of each element in the array
    count = Counter(nums)

    # Get the k most common elements
    most_common = count.most_common(k)

    return [elem for elem, freq in most_common]



# example usage
nums = [1,1,1,3,2,2]
k = 2
print(topKFrequent(nums, k))  # Output: [1, 2]