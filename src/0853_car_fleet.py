"""
15:48
853. Car Fleet

There are n cars at given miles away from the starting mile 0,
traveling to reach the mile target.

You are given two integer array position and speed,
both of length n, where position[i] is the starting mile of the ith car
and speed[i] is the speed of the ith car in miles per hour.

A car cannot pass another car, but it can catch up
and then travel next to it at the speed of the slower car.

A car fleet is a car or cars driving next to each other.
The speed of the car fleet is the minimum speed of any car in the fleet.

If a car catches up to a car fleet at the mile target,
it will still be considered as part of the car fleet.

Return the number of car fleets that will arrive at the destination.

Example 1:
target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]
Output: 3

Explanation:

The cars starting at 10 (speed 2) and 8 (speed 4) become a fleet,
meeting each other at 12. The fleet forms at target.
The car starting at 0 (speed 1) does not catch up to any other car, so it is a fleet by itself.
The cars starting at 5 (speed 1) and 3 (speed 3) become a fleet,
meeting each other at 6. The fleet moves at speed 1 until it reaches target.

Example 2:
target = 10, position = [3], speed = [3]
Output: 1

Explanation: There is only one car, hence there is only one fleet.

Example 3:
target = 100, position = [0,2,4], speed = [4,2,1]
Output: 1

Explanation:

The cars starting at 0 (speed 4) and 2 (speed 2) become a fleet,
meeting each other at 4. The car starting at 4 (speed 1) travels to 5.
Then, the fleet at 4 (speed 2) and the car at position 5 (speed 1) become one fleet,
meeting each other at 6. The fleet moves at speed 1 until it reaches target.

Constraints:
n == position.length == speed.length
1 <= n <= 10^5
0 < target <= 10^6
0 <= position[i] < target
All the values of position are unique.
0 < speed[i] <= 10^6
"""

from collections import namedtuple

Test = namedtuple("Test", ["target", "positions", "speeds", "exp"])

tests = [
    Test(10, [0, 4, 2], [2, 1, 3], 1),
    Test(12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3], 3),
    Test(10, [3], [3], 1),
    Test(100, [0, 2, 4], [4, 2, 1], 1),
]


def car_fleet_naive(target: int, positions: list[int], speeds: list[int]) -> int:
    """
    Time: O(n^2)
    Memo: O(n)

    Really slow!

    target = 12 position = [10,8,0,5,3], speed = [2,4,1,1,3]

    pos:  10, 8, 0, 5, 3
    dist:  2, 4,12, 7, 9
    speed: 2, 4, 1, 1, 3
    rem/h: 1, 1,12, 7, 3

    [10,8]
    [ 2,4]

    # sort by position
    [0, 3, 5, 8, 10]
    [1, 3, 1, 4,  2]
    """
    positions, speeds = zip(*sorted(zip(positions, speeds)))
    matches = []
    for i in range(len(positions)):
        p1, s1 = positions[i], speeds[i]
        h1 = (target - p1) / s1
        for j in range(i + 1, len(positions)):
            p2, s2 = positions[j], speeds[j]
            h2 = (target - p2) / s2
            if h1 <= h2:
                matches.append((i, j))
                break
    return len(positions) - len(matches)
    # p1 + (s1 * n) == p2 + (s2 * n)
    # p1 - p2 == (s2 * n) - (s1 * n)
    # p1 - p2 == n * (s2 - s1)
    # (p1 - p2) / (s2 - s1) == n


def car_fleet_sort_stack(target: int, positions: list[int], speeds: list[int]) -> int:
    """
    Time: O(n log n)
    Memo: O(n)
    Idea:
        - sort by position, necessary, otherwise there is no way to know the next car.
        - Save fleets in a list
        - For each car check if it will be overtaken by a fleet
        - It works since we store only increasing heights,
          we can calculate the area from this element to the current index.
    """
    positions, speeds = zip(*sorted(zip(positions, speeds)))
    fleets = []
    for i in range(len(positions)):
        p1, s1 = positions[i], speeds[i]
        h1 = (target - p1) / s1
        while fleets:
            p2, s2 = fleets[-1]
            h2 = (target - p2) / s2
            if h2 <= h1:
                fleets.pop()
            else:
                break
        fleets.append((p1, s1))
    return len(fleets)


def car_fleet_stack(target: int, positions: list[int], speeds: list[int]) -> int:
    """
    Time: O(n log n)
    Memo: O(n)
    """
    positions, speeds = zip(*sorted(zip(positions, speeds), reverse=True))
    fleets = []
    for i in range(len(positions)):
        p_tail, s_tail = positions[i], speeds[i]
        h_tail = (target - p_tail) / s_tail
        if fleets:
            h_head = fleets[-1]
            if h_tail > h_head:
                fleets.append(h_tail)
        else:
            fleets.append(h_tail)
    return len(fleets)


def car_fleet(target: int, positions: list[int], speeds: list[int]) -> int:
    """
    Time: O(n log n)
    Memo: O(1)

    Idea:
        - Sort by positions, reversed
        - From top to bottom, check if tail car catches up to fleet
        - If so, add to fleet, otherwise form new fleet

        THIS IMPLEMENTATION USES EXTRA MEMORY
    """
    n_fleets = 0   # number of fleets
    h_head = 0     # time of front fleet to arrival
    for p_tail, s_tail in sorted(zip(positions, speeds), reverse=True):
        h_tail = (target - p_tail) / s_tail
        if h_tail > h_head:
            n_fleets += 1
            h_head = h_tail
    return n_fleets


if __name__ == "__main__":
    for target, positions, speeds, exp in tests:
        act = car_fleet(target, positions, speeds)
        print(act, exp)
        # assert act == exp
