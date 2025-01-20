package main

import (
	"fmt"
	"strconv"
)

func isPalindrome_pointer(x int) bool {
	// Space O(1)
	// Time  O(n)
	xString := strconv.Itoa(x)
	for i := 0; i < len(xString)/2; i++ {
		l := xString[i]
		r := xString[len(xString)-1-i]
		if l != r {
			return false
		}
	}
	return true
}

func isPalindrome(num int) bool {
	// Space O(1)
	// Time O(n)
	// however way faster than the other version
	if num < 0 {
		return false
	}
	reversed := 0
	x := num
	for x != 0 {
		reversed = 10*reversed + x%10
		x = x / 10
	}
	return num == reversed
}

func main() {
	x := 1221
	fmt.Println(isPalindrome(x))
	fmt.Println(isPalindrome_pointer(x))
}
