'''
Question 5 — Design-y Coding: Moving Average Stream

Problem:
Implement a class that computes the moving average over the last k numbers.

m = MovingAverage(3)
m.next(1) -> 1.0
m.next(10) -> 5.5
m.next(3) -> 4.67
m.next(5) -> 6.0
'''

class MovingAverage:
    def __init__(self, size:int):
        self.size = size
        self.window = []
        self.sum = 0

    def next(self, val:int) -> float:
        if len(self.window) == self.size:
            self.sum -= self.window.pop(0)
        self.window.append(val)
        self.sum += val
        return self.sum / len(self.window)

# Example usage:
m = MovingAverage(3)
print(m.next(1))   # Output: 1.0
print(m.next(10))  # Output: 5.5
print(m.next(3))   # Output: 4.67
print(m.next(5))   # Output: 6.0