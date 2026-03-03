'''
Question 1 (Very Common)
“Implement a function to check if parentheses are balanced.”

Example:
Input: "({[]})" → True
Input: "([)]" → False

The solution have complextiy:
Time: O(n)
Space: O(n)
'''

def is_balanced(s: str) -> bool:
    match_dict = {
        ')': '(',
        ']': '[',
        '}': '{'
    }
    stack = []

    for char in s:
        if char in match_dict.values():
            stack.append(char)

        elif char in match_dict:
            if not stack:
                return False
            
            if stack[-1] != match_dict[char]:
                return False 
                
            stack.pop()
    return len(stack) == 0


# s = "({[]})"
s = "([)]"
print(is_balanced(s))
