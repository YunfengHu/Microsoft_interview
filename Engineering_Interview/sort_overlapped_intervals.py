'''
Problem

You’re given a list of intervals intervals, where each interval is [start, end] (inclusive).
Merge all overlapping intervals and return the merged list sorted by start.

Example

Input: [[1,3],[2,6],[8,10],[15,18]]

Output: [[1,6],[8,10],[15,18]]
'''

from typing import List

def merge_intervals(intervals: List[List[int]]) -> List[List[int]]:
    if not intervals:
        return []

    # 1) Sort by start time
    intervals.sort(key=lambda x: x[0])

    merged = []
    cur_start, cur_end = intervals[0]

    # 2) Sweep and merge
    for start, end in intervals[1:]:
        if start <= cur_end:  # overlap
            cur_end = max(cur_end, end)
        else:
            merged.append([cur_start, cur_end])
            cur_start, cur_end = start, end

    # 3) Add last interval
    merged.append([cur_start, cur_end])
    return merged


# Example usage
intervals = [[1,3],[2,6],[8,10],[15,18]]
print(merge_intervals(intervals))  # Output: [[1,6],[8,10],[15,18]]