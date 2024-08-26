"""
125. Valid Palindrome

A phrase is a palindrome if,
after converting all uppercase letters into lowercase letters
and removing all non-alphanumeric characters,
it reads the same forward and backward.
Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

Constraints:
- 1 <= s.length <= 2 * 10^5
- s consists only of printable ASCII characters.
"""

import string

tests = [
    ("0P", False),
    ("ama", True),
    ("amma", True),
    ("amba", False),
    ("a ma", True),
    ("a m m!a", True),
    ("A man, a plan, a canal: Panama", True),
    ("race a car", False),
    (" ", True),
]


def valid_palindrome_complex(s):
    """
    "-ab ba-"
     i     j
     "!!!!"
    """
    alphabet = set(string.ascii_letters + "0123456789")
    i = 0
    j = len(s) - 1
    while i <= j:
        c_i = s[i]
        while c_i not in alphabet and i < j:
            i += 1
            c_i = s[i]
        c_j = s[j]
        while c_j not in alphabet and j > i:
            j -= 1
            c_j = s[j]
        if c_i.lower() != c_j.lower():
            return False
        i += 1
        j -= 1
    return True


def valid_palindrome(s):
    """
    Same as above but simplified
    """
    i = 0
    j = len(s) - 1
    while i <= j:
        while i < j and not s[i].isalnum():
            i += 1
        while j > i and not s[j].isalnum():
            j -= 1
        if not s[i].lower() == s[j].lower():
            return False
        i += 1
        j -= 1
    return True


def valid_palindrome_neg(s):
    s = [c.lower() for c in s if c.isalnum()]
    return all(s[i] == s[~i] for i in range(len(s) // 2))


if __name__ == "__main__":
    for s, exp in tests:
        act = valid_palindrome(s)
        assert exp == act
