"""
76. Minimum Window Substring

Given two strings s and t of lengths m and n respectively,
return the minimum window substring of s such that
every character in t (including duplicates) is included in the window.
If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

Example 1: s = "ADOBECODEBANC", t = "ABC" Output: "BANC"
Explanation: The minimum window substring "BANC"
             includes 'A', 'B', and 'C' from string t.

Example 2: s = "a", t = "a" Output: "a"
Explanation: The entire string s is the minimum window.

Example 3: s = "a", t = "aa" Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.

Constraints:
m == s.length
n == t.length
1 <= m, n <= 105
s and t consist of uppercase and lowercase English letters.

Follow up: Could you find an algorithm that runs in O(m + n) time?
"""
from collections import namedtuple
from collections import defaultdict

Test = namedtuple("Test", ("s", "t", "exp"))

tests = (
    Test('a', 'a', 'a'),
    Test('ADOBECODEBANC', 'ABC', 'BANC'),
    Test('a', 'aa', ''),
    Test('OUZODYXAZV', 'XYZ', 'YXAZ'),
    Test('xyz', 'xyz', 'xyz'),
    Test('x', 'xy', '')
)


def has_dct_subset_keys_with_values_less_equal(m1: dict[str: int],
                                               m2: dict[str: int]) -> bool:
    for k, v in m1.items():
        if k in m2:
            if v > m2[k]:
                return False
        else:
            return False
    return True


def min_window(s: str, t: str) -> str:
    """
        Idea: Expand window until its valid.
              Contract as long as it stays valid.
        Time: O(n)
        Memo: O(1) since the number of characters is limited to 128
    """
    tdct = defaultdict(lambda: 0)
    for c in t:
        tdct[c] += 1
    sdct = defaultdict(lambda: 0)
    idcs = ()
    minlen = len(s) + 1

    i_left = 0
    for i_right in range(0, len(s)):
        # expand window
        right = s[i_right]
        if right not in tdct:
            continue
        sdct[right] += 1

        # contract window
        while has_dct_subset_keys_with_values_less_equal(tdct, sdct):
            current_len = i_right - i_left + 1
            if current_len < minlen:
                minlen = current_len
                idcs = (i_left, i_right)
            left = s[i_left]
            sdct[left] -= 1
            i_left += 1
    if not idcs:
        return ""
    else:
        return s[idcs[0]: idcs[1]+1]


if __name__ == '__main__':
    for s, t, exp in tests:
        act = min_window(s, t)
        print(f"s='{s}', t='{t}, exp='{exp}' act='{act}'")
        assert act == exp
