'''
Problem

Given an array of integers nums and a window size k, return a list where each element is the average of the last k numbers (or fewer at the start).

Example:
nums = [1, 10, 3, 5]
k = 3
# output: [1.0, 5.5, 4.6667, 6.0]
'''

def moving_average(nums, k):
    moving_ave = []
    for i in range(len(nums)):
        if i < k:
            moving_ave.append(sum(nums[0:i+1])/(i+1))
        else:
            moving_ave.append(sum(nums[i-k+1:i+1])/k)
    return moving_ave

# Test cases
print(moving_average([1, 10, 3, 5], 3))  # [1.0, 5.5, 4.6667, 6.0]