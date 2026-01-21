/*
155. Min Stack
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:
MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.
You must implement a solution with O(1) time complexity for each function.

Example 1:

Input
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

-231 <= val <= 231 - 1
Methods pop, top and getMin operations will always be called on non-empty stacks.
At most 3 * 104 calls will be made to push, pop, top, and getMin.

Recommended Time & Space Complexity
You should aim for a solution with O(1) time for each function call and O(n) space, where n is the maximum number of elements present in the stack.
*/

package main

import "fmt"

type MinStack struct {
	valStack []int
	minStack []int 
}

func Constructor() MinStack {
    return MinStack{}
}

func (this *MinStack) Push(val int)  {
	this.valStack = append(this.valStack, val)
	if len(this.minStack) > 0 {
		this.minStack = append(this.minStack, min(this.minStack[len(this.minStack)-1], val))
	} else {
		this.minStack = append(this.minStack, val)
	}
}

func (this *MinStack) Pop()  {
    this.minStack = this.minStack[:len(this.minStack) - 1]
    this.valStack = this.valStack[:len(this.valStack) - 1]
}

func (this *MinStack) Top() int {
	vs := this.valStack
	return vs[len(vs) - 1]
}

func (this *MinStack) GetMin() int {
 	ms := this.minStack
 	return ms[len(ms) - 1]   
}

func main(){
	minStack := Constructor()
	minStack.Push(4)
	minStack.Push(1)
	minStack.Push(5)
	minStack.Push(0)
	minStack.Pop()
	fmt.Println(minStack)
	fmt.Println(minStack.Top())
	fmt.Println(minStack.GetMin())
}