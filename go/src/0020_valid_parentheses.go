/*
Valid Parentheses
You are given a string s consisting of the following characters: '(', ')', '{', '}', '[' and ']'.

The input string s is valid if and only if:

Every open bracket is closed by the same type of close bracket.
Open brackets are closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
Return true if s is a valid string, and false otherwise.

Example 1:
Input: s = "[]"
Output: true

Example 2:
Input: s = "([{}])"
Output: true

Example 3:
Input: s = "[(])"
Output: false
Explanation: The brackets are not closed in the correct order.

Constraints:
1 <= s.length <= 1000

Recommended Time & Space Complexity
You should aim for a solution with O(n) time and O(n) space, where n is the length of the given string.
*/

package main

import "fmt"

//type stack []int
//
//func (s *stack) Push(v int) {
//	*s = append(*s, v)
//}
//
//func (s *stack) Pop() int {
//	l := len(*s)
//	e := (*s)[l-1]
//	*s = (*s)[:l-1]
//	return e
//}

type stack[T any] []T

func (s *stack[T]) Push(v T) {
	*s = append(*s, v)
}

func (s *stack[T]) Pop() T {
	l := len(*s)
	e := (*s)[l-1]
	*s = (*s)[:l-1]
	return e
}

func isValid(s string) bool {
	stack := make(stack[rune], 0)
	for _, char := range s {
		switch char {
		case '(', '[', '{':
			stack.Push(char)
		default:
			if len(stack) == 0 {
				return false
			}
			switch char {
			case ')':
				if stack.Pop() != '(' {
					return false
				}
			case ']':
				if stack.Pop() != '[' {
					return false
				}
			case '}':
				if stack.Pop() != '{' {
					return false
				}
			}
		}
	}
	return len(stack) == 0
}

func main() {
	fmt.Println(isValid("([]){"))
	//s := make(stack[int], 0)
	//fmt.Println(s)
	//s.Push(1)
	//fmt.Println(s)
	//s.Push(10)
	//s.Push(20)
	//fmt.Println(s)
	//i := s.Pop()
	//fmt.Println(i)

	//ss := &s
	//fmt.Println(len(s), len(*ss))
	//fmt.Println((*ss)[0])
}
