package main

import "fmt"

type stack []rune

func (s stack) Push(v rune) stack {
	return append(s, v)
}

func (s stack) Pop() (stack, rune) {
	l := len(s)
	return s[:l-1], s[l-1]
}

func isValid(s string) bool {
	// len(s) >= 1
	sk := make(stack, 0)
	var op rune
	for _, r := range s {
		switch r {
		case '(', '[', '{':
			sk = sk.Push(r)
		default:
			if len(sk) < 1 {
				return false
			}
			sk, op = sk.Pop()
			switch r {
			case ')':
				if op != '(' {
					return false
				}
			case ']':
				if op != '[' {
					return false
				}
			case '}':
				if op != '{' {
					return false
				}
			default:
				return false
			}
		}
	}
	if len(sk) > 0 {
		return false
	}
	return true
}

func main() {
	// [
	// []
	// [)
	// [()
	// [()]
	// [(])
	fmt.Println(isValid("[(])"))
}
