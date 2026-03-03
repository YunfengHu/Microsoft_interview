'''
Question 2 (Microsoft Favorite)
“Find the first non-repeating character in a string.”

Example:
"leetcode" → "l"
"loveleetcode" → "v"
'''

from collections import Counter 

def first_non_repeating_character(s):
    char_count = Counter(s)

    for char in s:
        if char_count[char] == 1:
            return char 
    return "There is no non-repeating character." 


# s = "leetcode"
s = "loveleetcode"
print(first_non_repeating_character(s))
