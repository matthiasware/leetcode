"""
150. Evaluate Reverse Polish Notation

You are given an array of strings tokens
that represents an arithmetic expression in a Reverse Polish Notation.

Evaluate the expression.
Return an integer that represents the value of the expression.

Note that:
The valid operators are '+', '-', '*', and '/'.
Each operand may be an integer or another expression.

The division between two integers always truncates toward zero.

There will not be any division by zero.
The input represents a valid arithmetic expression in a reverse polish notation.
The answer and all the intermediate calculations can be represented in a 32-bit integer.

Example 1:
tokens: ["2","1","+","3","*"]
return: 9
Explanation: ((2 + 1) * 3) = 9

Example 2:
tokens: ["4","13","5","/","+"]
return: 6
Explanation: (4 + (13 / 5)) = 6

Example 3:
tokens: ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
return: 22
Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22

["10","6","-132","/","*","17","+","5","+"]

Constraints:
1 <= tokens.length <= 104
tokens[i] is either an operator: "+", "-", "*", or "/", or an integer in the range [-200, 200].
"""

from collections import namedtuple
import operator as op
import math

Test = namedtuple("Test", ["tokens", "exp"])

tests = [
    Test(["5"], 5),
    Test(["2", "3", "+"], 5),
    Test(["2", "3", "-"], -1),
    Test(["2", "3", "*"], 6),
    Test(["2", "3", "/"], 0),
    Test(["2", "1", "+", "3", "*"], 9),
    Test(["4", "13", "5", "/", "+"], 6),
    Test(["4", "2", "-", "1", "+"], 3),
    Test(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"], 22),
]


def eval_rpn(tokens: list[str]) -> int:
    """
        Time: O(n)
        Memo: O(n)
    """
    op_dct = {
        '-': op.sub,
        '+': op.add,
        '*': op.mul,
        '/': lambda a, b: math.trunc(op.truediv(a, b)),
    }
    stack = []
    for tok in tokens:
        if tok in op_dct:
            opd2, opd1 = stack.pop(), stack.pop()
            operator = op_dct[tok]
            res = operator(opd1, opd2)
            stack.append(res)
        else:
            stack.append(int(tok))

    return stack[-1]


if __name__ == '__main__':
    for tokens, exp in tests:
        act = eval_rpn(tokens)
        assert act == exp