"""
155. Min Stack

Design a stack that supports push, pop, top,
and retrieving the minimum element in constant time.

Implement the MinStack class:

MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.
You must implement a solution with O(1) time complexity for each function.

Example 1:
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

Output
[null,null,null,null,-3,null,0,-2]

Explanation
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2

Constraints:
-2^31 <= val <= 2^31 - 1
Methods pop, top and getMin operations will always be called on non-empty stacks.
At most 3 * 10^4 calls will be made to push, pop, top, and getMin.
"""


def test_01():
    ms = MinStack()
    ms.push(-2)
    ms.push(0)
    ms.push(-3)
    assert ms.getMin() == -3
    ms.pop()
    assert ms.top() == 0
    assert ms.getMin() == -2


def test_02():
    ms = MinStack()
    ms.push(-2)
    ms.push(0)
    ms.push(-1)
    assert ms.getMin() == -2
    assert ms.top() == -1
    ms.pop()
    assert ms.getMin() == -2


class MinStack:
    def __init__(self):
        self.stack = []
        self.min_indices = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if (not self.min_indices) or (val < self.stack[self.min_indices[-1]]):
            self.min_indices.append(len(self.stack) - 1)

    def pop(self) -> None:
        idx = len(self.stack) - 1
        if idx == self.min_indices[-1]:
            self.min_indices.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.stack[self.min_indices[-1]]


if __name__ == '__main__':
    test_01()
    test_02()