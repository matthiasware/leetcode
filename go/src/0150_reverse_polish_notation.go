/Users/matthias.mitterreiter/projects/leetcode/go/src/0150_reverse_polish_notation.go/*
Evaluate Reverse Polish Notation
You are given an array of strings tokens that represents a valid arithmetic expression in Reverse Polish Notation.

Return the integer that represents the evaluation of the expression.

The operands may be integers or the results of other operations.
The operators include '+', '-', '*', and '/'.
Assume that division between integers always truncates toward zero.

Example 1:
Input: tokens = ["1","2","+","3","*","4","-"]
Output: 5

Explanation: ((1 + 2) * 3) - 4 = 5

Constraints:
-) 1 <= tokens.length <= 1000.
-) tokens[i] is "+", "-", "*", or "/", or a string representing an integer in the range [-100, 100].


Recommended Time & Space Complexity
You should aim for a solution with O(n) time and O(n) space, where n is the size of the input array.
*/

package main

import (
	"fmt"
	"strconv"
)

type Stack []int

func (s *Stack) Push(i int){
	*s = append(*s, i)
}

func (s *Stack) Pop() int{
	idx := len(*s) - 1
	item := (*s)[idx]
	*s = (*s)[:idx]
	return item
}


func evalRPN(tokens []string) int {
	stack := Stack{}
	for _, token := range tokens {
		if token == "+" {
			op2 := stack.Pop()
			op1 := stack.Pop()
			res := op1 + op2
			stack.Push(res)
		} else if token == "-"{
			op2 := stack.Pop()
			op1 := stack.Pop()
			res := op1 - op2
			stack.Push(res)
		} else if token == "*" {
			op2 := stack.Pop()
			op1 := stack.Pop()
			res := op1 * op2
			stack.Push(res)
		} else if token == "/" {
			op2 := stack.Pop()
			op1 := stack.Pop()
			res := op1 / op2
			stack.Push(res)
		} else {
			num, _ := strconv.Atoi(token)
			stack.Push(num)
		}
	}
	res := stack.Pop()
	return res
}

func evalRPNFunc(tokens []string) int {
	ops := map[string]func(int, int) int {
		"+": func(a int, b int) int {return a + b},
		"-": func(a int, b int) int {return a - b},
		"*": func(a int, b int) int {return a * b},
		"/": func(a int, b int) int {return a / b},
	}
	stack := Stack{}
	for _, token := range tokens {
		op, ok := ops[token]
		if ok {
			op2 := stack.Pop()
			op1 := stack.Pop()
			res := op(op1, op2)
			stack.Push(res)
		} else {
			num, _ := strconv.Atoi(token)
			stack.Push(num)
		}
	}
	res := stack.Pop()
	return res
}

type Test struct {
	tokens []string
	result int
}

func main(){
	tests := []Test{
		{[]string{"1",}, 1},
		{[]string{"1","2","+"}, 3},
		{[]string{"1","2","+","3","*","4","-"}, 5},
		{[]string{"2","1","+","3","*"}, 9},
		{[]string{"4","13","5","/","+"}, 6},
		{[]string{"10","6","9","3","+","-11","*","/","*","17","+","5","+"}, 22},
	}
	for _, test := range tests {
		act := evalRPNFunc(test.tokens)
		var colCode string
		if act == test.result {
			colCode = "\033[32m"
		} else {
			colCode = "\033[31m"
		}
		fmt.Printf("%s exp: %3d act: %3d input: %v \n", colCode, test.result, act, test.tokens)
	}
}