package main

import (
	"fmt"
	"strings"
)

func lengthOfLastWord(s string) int {
	chars := []rune(s)

	// remove white space
	i := len(chars) - 1
	for ; i >= 0; i-- {
		if chars[i] != ' ' {
			break
		}
	}
	length := 0
	for ; i >= 0; i-- {
		if chars[i] != ' ' {
			length++
		} else {
			break
		}
	}
	return length
}

func lengthOfLastWord2(s string) int {
	split := strings.Split(s, " ")
	for i := len(split) - 1; i >= 0; i-- {
		if split[i] != " " && split[i] != "" {
			return len(split[i])
		}
	}
	return 0
}

func main() {
	fmt.Println(lengthOfLastWord(" Hello wär "))
}
