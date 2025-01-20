package main

import (
	"fmt"
	"leetcode/tools"
)

func main() {
	stack := tools.New[int]()
	stack.Push(1)
	fmt.Println(stack)
}
