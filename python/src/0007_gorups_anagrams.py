"""
49. Group Anagrams
Given an array of strings strs,
group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging
the letters of a different word or phrase,
typically using all the original letters exactly once.

Constraints:
-) 1 <= strs.length <= 10^4
-) 0 <= strs[i].length <= 100
-) strs[i] consists of lowercase English letters.
"""

from collections import defaultdict

tests = [
    # input expected
    (
        ["eat", "tea", "tan", "ate", "nat", "bat"],
        [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]],
    ),
    ([""], [[""]]),
    (["a"], [["a"]]),
]


def is_anagram(s1: str, s2: str) -> bool:
    """
    Time: O(n)
    Memo: O(1)
    """
    counts = [0] * 26
    for c in s1:
        counts[ord(c) - ord("a")] += 0
    for c in s2:
        counts[ord(c) - ord("a")] -= 1
    if sum(counts) != 0:
        return False
    return True


def get_anagrams(strings: list[str]) -> bool:
    """
    n ... len(strings)
    m ... len(strings[i])
    Time: O(n*(m*log(m)))
    Memo: O(n*m)
    """
    # maps sorted(str) -> List[str]
    anagrams = defaultdict(list)
    for s in strings:
        s_sorted = "".join(sorted(s))
        anagrams[s_sorted].append(s)
    return list(anagrams.values())


def get_anagrams_no_sort(strings: list[str]) -> bool:
    """
    Time: O(n*m)
    Memo: O(n)
    """
    anagrams = defaultdict(list)
    for s in strings:
        counts = [0] * 26
        for c in s:
            counts[ord(c) - ord("a")] += 1
        anagrams[tuple(counts)].append(s)
    return anagrams.values()


if __name__ == "__main__":
    for strings, exp in tests:
        act = get_anagrams_no_sort(strings)
        act = [sorted(a) for a in act]
        act.sort()
        exp.sort()
        assert act == exp
