"""
242. Given two strings s and t,
return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging
the letters of a different word or phrase,
typically using all the original letters exactly once.

Constraints:
-) 1 <= s.length, t.length <= 5 * 10^4
-) s and t consist of lowercase English letters
"""

tests = [
    ("anagram", "nagaram", True),
    ("anagramn", "nagaramm", False),
    ("rat", "car", False),
]


def valid_anagram_sort(s1: str, s2: str) -> bool:
    """
    Time: O(n*log(n))
    Memo: O(n)
    """
    return sorted(s1) == sorted(s2)


def valid_anagram_hashing(s1: str, s2: str) -> bool:
    """
    Time: O(n)
    Memo: O(1) since we only store 26 key-value pairs
    """
    hm = {}
    for c in s2:
        if c not in hm:
            hm[c] = 1
        else:
            hm[c] += 1
    for c in s1:
        if c not in hm:
            return False
        if hm[c] == 0:
            return False
        hm[c] -= 1
    return True


def valid_anagram_count_array(s1: str, s2: str) -> bool:
    """
    Time: O(n)
    Memo: O(1)
    """
    counts = [0] * 26
    for c in s1:
        counts[ord(c) - ord("a")] += 1
    for c in s2:
        counts[ord(c) - ord("a")] -= 1
    for c in counts:
        if c != 0:
            return False
    return True


if __name__ == "__main__":
    for s1, s2, exp in tests:
        act = valid_anagram_count_array(s1, s2)
        assert act == exp
