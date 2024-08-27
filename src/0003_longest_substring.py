"""
    3. Longest Substring without repeating character.

    Given a string S,
    find the length of the longest substring
    without repeating characters.

    Expected Time Complexity: O(|S|).
    Expected Auxiliary Space: O(K) where K is constant.

    1 ≤ |S| ≤ 10^5
"""

tests = [
    ("", 0),
    ("a", 1),
    ("ab", 2),
    ("aa", 1),
    ("geeksforgeeks", 7),  # eksforg
    ("abcabcbb", 3),
    ("bbbbb", 1),
    ("pwwkew", 3),
    ("abdefgabef", 6),  # either: "abdefg" , "bdefga" and "defgab"."
    ("qwerty", 6),
]


def longest_substring_01(s: str) -> int:
    i_start = 0
    i_end = 0
    visited = set()
    l_max = 0
    while i_end < len(s):
        if s[i_end] not in visited:
            l_max = max(l_max, i_end - i_start + 1)
            visited.add(s[i_end])
        else:
            while s[i_start] != s[i_end]:
                visited.remove(s[i_start])
                i_start += 1
            i_start += 1
        i_end += 1
    return l_max


def longest_substring_02(string: str) -> int:
    """
    Time: O(n)
    Memo: O(k) for k ... max amount of characters
    """
    visited = set()
    l_max = 0

    i_left = 0
    i_right = 0
    while i_right < len(string):
        if string[i_right] in visited:
            while string[i_right] in visited:
                visited.remove(string[i_left])
                i_left += 1
        visited.add(string[i_right])
        l_max = max(l_max, len(visited))
        i_right += 1
    return l_max


def longest_substring_03(string):
    """use deque"""
    pass


if __name__ == "__main__":
    for s, exp in tests:
        act = longest_substring_02(s)
        assert act == exp
