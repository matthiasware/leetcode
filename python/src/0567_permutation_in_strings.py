"""
567. Permutation in String

Given two strings s1 and s2,
return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.

Constraints:
-) 1 <= s1.length, s2.length <= 104
-) s1 and s2 consist of lowercase English letters.
"""

from collections import namedtuple
import timeit
from functools import partial

Test = namedtuple("Test", ["str1", "str2", 'exp'])

tests = [
    Test("ab", "eidbaooo", True),
    Test("ab", "eidboaoo", False),
    Test("ab", "ghilkba", True),
    Test("hello", "ooolleoooleh", False)
]


def check_inclusion_sort(str1: str, str2: str) -> bool:
    """
        n = len(str1)
        m = len(str2)

        Time: O(n*log(n)) + O(m * n*log(n)) -> O(m * n*log(n))
        Memo: O(n)
    """
    str1 = sorted(str1)
    for i in range(len(str2) - len(str1)):
        sub_str = str2[i:i+len(str1)+1]
        if sorted(sub_str) == str1:
            return True
    return False


def check_inclusion(str1: str, str2: str) -> bool:
    """
        Idea: Sliding window that keeps tracks of the characters within
              Match window characters with str1 with a counter array.
              Sets cannot be used, however multisets work.
        n ... len(str1)
        m ... len(str2)
        Time: O(n) + O(m) -> O(n+m)
        Memo: O(1)
    """
    str1_counts = [0] * 26
    for c in str1:
        str1_counts[ord(c) - ord('a')] += 1

    str2_counts = [0] * 26
    i_left = 0
    for i_right, c in enumerate(str2):
        str2_counts[ord(c) - ord('a')] += 1

        if str2_counts == str1_counts:
            return True
        if (i_right - i_left + 1) == len(str1):
            str2_counts[ord(str2[i_left]) - ord('a')] -= 1
            i_left += 1
    return False


if __name__ == "__main__":
    for str1, str2, exp in tests:
        act = check_inclusion(str1, str2)
        assert act == exp

    str1 = "uipolk"
    str2 = ("asfsdafaffiansdfihians"
            "falihfilansdifhliansbd"
            "iflhialsnbsfsdafdsfdfias")
    n_repts = 100_000
    t_sort = timeit.timeit(partial(check_inclusion_sort, str1, str2),
                           number=n_repts)
    t_sets = timeit.timeit(partial(check_inclusion, str1, str2),
                           number=n_repts)

    print(f'sort: {t_sort:.4f}, smart: {t_sets:.4f}')
