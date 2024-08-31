"""
20. Valid Parentheses

Given a string s containing just the characters
'(', ')', '{', '}', '[' and ']',
determine if the input string is valid.

An input string is valid if:
- Open brackets must be closed by the same type of brackets.
- Open brackets must be closed in the correct order.
- Every close bracket has a corresponding open bracket of the same type.

Example 1: s = "()" -> true
Example 2: s = "()[]{}" -> true
Example 3: s = "(]" -> false
Example 4: s = "([])" -> true

Constraints:
1 <= s.length <= 104
s consists of parentheses only '()[]{}'
"""

from collections import namedtuple

Test = namedtuple("Test", ("s", "exp"))

tests = [
    Test("()", True),
    Test("(}", False),
    Test("()[]{}", True),
    Test("([])", True),
    Test("([]})", False),
    Test("([])", True)
]


def is_valid(s: str) -> bool:
    """
        Time: O(n)
        Memo: O(n)
    """
    stack = []
    parmap = {
        ')': '(',
        ']': '[',
        '}':  '{',
    }
    for c in s:
        # must be an opening paranthesis
        if c not in parmap:
            stack.append(c)
        # must be a closing paranthesis
        elif not stack or stack.pop() != parmap[c]:
            return False
    return not stack
            


if __name__ == "__main__":
    for s, exp in tests:
        act = is_valid(s)
        print(s, act, exp)
        assert act == exp