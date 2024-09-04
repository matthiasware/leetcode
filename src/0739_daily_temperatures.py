"""
739. Daily Temperatures

Given an array of integers temperatures represents the daily temperatures,
return an array answer such that answer[i] is the number of days
you have to wait after the ith day to get a warmer temperature.
If there is no future day for which this is possible, keep answer[i] == 0 instead.

Example 1: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]

Example 2: temperatures = [30,40,50,60]
Output: [1,1,1,0]

Example 3: temperatures = [30,60,90]
Output: [1,1,0]

Constraints:
1 <= temperatures.length <= 10^5
30 <= temperatures[i] <= 100
"""

from collections import namedtuple

Test = namedtuple("Test", ["temperatures", "exp"])

tests = [
    Test([30, 40, 50, 60], [1, 1, 1, 0]),
    Test([1, 2, 3], [1, 1, 0]),
    Test([73, 74, 75, 71, 69, 72, 76, 73], [1, 1, 4, 2, 1, 1, 0, 0]),
    Test([30, 60, 90], [1, 1, 0]),
]

def daily_temperatures_naive(temps: list[int]) -> list[int]:
    """
        Time: O(n^2)
        Memo: O(n)
    """  
    days = []
    for i, t1 in enumerate(temps):
        for j, t2 in enumerate(temps[i+1:], start=i+1):
            if t2 > t1:
                days.append(j - i)
                break
        else:
            days.append(0)
    return days


def daily_temperatures(temperatures: list[int]) -> list[int]:
    """
        Ideas:
        idcs:  0   1   2   3   4   5   6   7
        temperatures: 73, 74, 75, 71, 69, 72, 76, 73
        days:  1   1   0   2   1   0   0   0
                                   i
        stack: (75, 2)

        Time: O(n)
        Memo: O(n)

    """
    stack = []
    days = [0] * len(temperatures)
    for i, temp in enumerate(temperatures):
        while stack and temp > temperatures[stack[-1]]:
            j = stack.pop()
            days[j] = i - j
        stack.append(i)
    return days


if __name__ == "__main__":
    for temps, exp in tests:
        act = daily_temperatures(temps)
        print(act, exp)
        assert act == exp