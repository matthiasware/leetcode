"""
424. Longest Repeating Character Replacement
You are given a string s and an integer k.
You can choose any character of the string
and change it to any other uppercase English character.
You can perform this operation at most k times.

Return the length of the longest substring
containing the same letter you can get after performing the above operations.

Constraints:
-) 1 <= s.length <= 10^5
-) s consists of only uppercase English letters.
-) 0 <= k <= s.length

"""
from collections import namedtuple

Test = namedtuple("Test", ["string", "k", "exp"])

tests = [
    Test("A", 1, 1),
    Test("AB", 1, 2),
    Test("ABBC", 0, 2),
    Test("ABAB", 2, 4),  # Replace the two 'A's with two 'B's or vice versa.
    # Replace the one 'A' in the middle with 'B' and form "AABBBBA".
    # The substring "BBBB" has the longest repeating letters, which is 4
    Test("AABABBA", 1, 4),
    Test("AABABBA", 2, 5),
]


def character_replacement(s: str, k: int) -> int:
    """
        Create dynamic sliding window!
        In window count occurances of characters in dict.
        if window is valid we continue expanding.
        Otherwise we contract until it is valid again.
        A window is valid if:
            (right - left + 1) < (max(c) + k)
        The total number of elements in window must be smaller
        than the majority of elements
        + the number of exchanges allowed.
        Why is this valid:
            Imagine we have a set with 4 red and 2 yellow balls and
            I can exchange 3 balls.
            It holds that
                total = 4+2
                max = 4
                exchange = 3
            as long as
                total <= max + exchange 7 <= 4 + 2
            we can add balls!
    """
    counts = {}
    l = 0
    max_length = 0
    for r in range(0, len(s)):
        counts[s[r]] = counts.get(s[r], 0) + 1
        max_count = max(counts.values())

        while (r - l + 1) > max_count + k:
            counts[s[l]] -= 1
            max_count = max(counts.values())
            l += 1
        max_length = max(max_length, max(counts.values()))
    return min(len(s), max_length+k)


def character_replacement_optimized(s: str, k: int) -> int:
    """
        Same Ideas as above but with one modification:
        We will denote the max length of subarray with the
        window length
            (r - l + 1).
        The window is not allowed to shrink but only expands!
        The maximum window length we reached so far is given via:
            max_counts + k

        Time: O(n)
        Memo: O(1)
    """
    counts = {}
    max_count = 0
    l = 0
    for r in range(len(s)):
        counts[s[r]] = counts.get(s[r], 0) + 1
        max_count = max(max_count, counts[s[r]])

        if (r - l + 1) > max_count + k:
            counts[s[l]] -= 1
            l += 1
    return (r - l + 1)


if __name__ == "__main__":
    for s, k, exp in tests:
        act = character_replacement_optimized(s, k)
        print(s, k, exp, act)
