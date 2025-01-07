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
