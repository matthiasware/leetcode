/*
go test -bench=. -benchmem 0150_reverse_polish_notation_test.go
*/

package main

import (
	"strconv"
	"testing"
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

type FastStack struct {
	data []int
	top int
}

func (s *FastStack) Push(i int) {
    s.data[s.top] = i
    s.top++
}

func (s *FastStack) Pop() int {
    s.top--
    return s.data[s.top]
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

func evalRPNFast(tokens []string) int {
    stack := FastStack{
        data: make([]int, len(tokens)), 
        top:  0,
    }

    for _, token := range tokens {
        switch token {
        case "+":
            op2 := stack.Pop()
            op1 := stack.Pop()
            stack.Push(op1 + op2)
        case "-":
            op2 := stack.Pop()
            op1 := stack.Pop()
            stack.Push(op1 - op2)
        case "*":
            op2 := stack.Pop()
            op1 := stack.Pop()
            stack.Push(op1 * op2)
        case "/":
            op2 := stack.Pop()
            op1 := stack.Pop()
            stack.Push(op1 / op2)
        default:
            num, _ := strconv.Atoi(token)
            stack.Push(num)
        }
    }
    return stack.Pop()
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

// Global variable to prevent compiler optimizations
var result int


var benchmarkTests = []Test{
	{[]string{"1"}, 1},
	{[]string{"1", "2", "+"}, 3},
	{[]string{"1", "2", "+", "3", "*", "4", "-"}, 5},
	{[]string{"2", "1", "+", "3", "*"}, 9},
	{[]string{"4", "13", "5", "/", "+"}, 6},
	{[]string{"10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"}, 22},
}

func Benchmark_evalPRN(b *testing.B) {
	var r int
	for i := 0; i < b.N; i++ {
		for _, test := range benchmarkTests {
			r = evalRPN(test.tokens)
		}
	}
	result = r
}
func Benchmark_evalRPNFunc(b *testing.B) {
	var r int
	for i := 0; i < b.N; i++ {
		for _, test := range benchmarkTests {
			r = evalRPNFunc(test.tokens)
		}
	}
	result = r
}
func Benchmark_evalRPNFastc(b *testing.B) {
	var r int
	for i := 0; i < b.N; i++ {
		for _, test := range benchmarkTests {
			r = evalRPNFast(test.tokens)
		}
	}
	result = r
}