"""
347. Top K Frequent Elements

Given an integer array nums and an integer k,
return the k most frequent elements. You may return the answer in any order.

Follow up: Your algorithm's time complexity must be better than O(n log n),
where n is the array's size.

Constraints:
-) 1 <= nums.length <= 10^5
-) -10^4 <= nums[i] <= 10^4
-) k is in the range [1, the number of unique elements in the array].
-) It is guaranteed that the answer is unique.
"""

import heapq
from collections import defaultdict, Counter

tests = [
    # lst, k, expected
    ([1, 1, 1, 2, 2, 3], 2, [1, 2]),
    ([1], 1, [1]),
    ([1, 1, 1, 2, 2, 3], 2, [1, 2]),
    ([1, 1, 2, 2, 2, 2, 3, 3, 3, 4], 2, [3, 2]),
    ([4, 4, 1, 1, 3, 3, 2], 3, [4, 3, 1]),
    ([2, 2, 1, 1, 1, 0, 0, 0, 3], 2, [1, 0]),
]


def k_most_frequent(lst: list[int], k: int) -> list[int]:
    """
    Time: O(n*log(n))
    Memo: O(n)
    """
    dct = defaultdict(int)
    for n in lst:
        dct[n] += 1
    topk = sorted(dct.items(), key=lambda x: x[1], reverse=True)
    topk = [i[0] for i in topk[:k]]
    return topk


def add_to_heap_if_bigger(heap: list[int], k: int,
                          num: int, freq: int) -> None:
    if len(heap) < k:
        heapq.heappush(heap, (freq, num))
    else:
        (root_freq, root_num) = heap[0]
        if freq > root_freq:
            heapq.heappushpop(heap, (freq, num))


def k_most_frequent_heap(lst: list[int], k: int) -> list[int]:
    """
    Time: O(n*log(n)) ???
    Memo: O(k)
    """
    lst.sort()

    # stores k most frequent nums (freq, num)
    heap = []

    num = lst[0]
    freq = 1
    idx = 1
    while idx < len(lst):
        if lst[idx] != num:
            add_to_heap_if_bigger(heap, k, num, freq)
            freq = 1
            num = lst[idx]
        else:
            freq += 1
        idx += 1
    add_to_heap_if_bigger(heap, k, num, freq)
    topk = [heapq.heappop(heap)[1] for _ in range(k)]
    return topk


def k_most_common_counter(lst: list[int], k: int) -> list[int]:
    """
    Time: O(n + k log(n))
    https://stackoverflow.com/questions/29240807/python-collections-counter-most-common-complexity
    Memo: O(n+k) counter + return list
    """
    counter = Counter(lst)
    return [n for n, _ in counter.most_common(k)]


if __name__ == "__main__":
    for lst, k, exp in tests:
        act = k_most_frequent_heap(lst, k)
        assert sorted(act) == sorted(exp)
