"""
22. Generate Parentheses

Given n pairs of parentheses,
write a function to generate all combinations of well-formed parentheses.

Example 1: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

Example 2: n = 1
Output: ["()"]

Constraints:

1 <= n <= 8
"""

from collections import namedtuple

Test = namedtuple("Test", ("n", "exp"))

"""
    1 -> () 1
    2 -> (()) | ()() 2
    3 -> ((())) ()(()) (())() | (()()) (())() ()(()) ()()()
      -> ((())) ()(()) (())() | (()()) ()()()
"""

tests = [
    Test(1, ["()"]),
    Test(2, ["(())", "()()"]),
    Test(3, ["((()))", "(()())", "(())()", "()(())", "()()()"]),
    Test(
        4,
        [
            "(((())))",
            "((()()))",
            "((())())",
            "((()))()",
            "(()(()))",
            "(()()())",
            "(()())()",
            "(())(())",
            "(())()()",
            "()((()))",
            "()(()())",
            "()(())()",
            "()()(())",
            "()()()()",
        ],
    ),
]


def generateParanthesis(n: int) -> list[str]:
    """
        Complexities follow the Catalan numbers
        https://en.wikipedia.org/wiki/Catalan_number

        Stack item stores:
        - expr
        - number of currently open parentheses
        - number of remaining parenthesis to open
    """

    stack = [('', 0, n)]
    results = []
    while stack:
        expr, n_open, n_remaining = stack.pop()
        if n_remaining == 0:
            # cannot open more parentheses -> close the open ones
            results.append(expr + ")" * n_open)
            continue
        if n_open > 0:
            stack.append((expr + ")", n_open - 1, n_remaining))
        stack.append((expr + "(", n_open + 1, n_remaining - 1))
    return results


def generateParanthesis_rec(n: int) -> list[str]:
    """
        Same as above with implicit stack
    """
    def rec(expr, n_open, n_remaining):
        if n_remaining == 0:
            return [expr + ")" * n_open]
        res = []
        if n_open > 0:
            res += rec(expr + ")", n_open - 1, n_remaining)
        res += rec(expr + "(", n_open + 1, n_remaining - 1)
        return res
    return rec('', 0, n)


if __name__ == "__main__":
    for n, exp in tests:
        act = generateParanthesis_rec(n)
        act.sort()
        exp.sort()
        # print(len(act), len(exp))
        print(act, exp)
        # diff = set(exp).difference(set(act))
        # print("Diff", diff)
        assert act == exp
    
    """
    1 1
    2 2
    3 5
    4 14
    5 42
    6 132
    7 429
    8 1430
    9 4862
    """

    for n in range(1, 11):
        r = generateParanthesis(n)
        print(len(r))