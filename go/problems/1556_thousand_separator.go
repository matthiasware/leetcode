package main

import (
	"fmt"
	"strconv"
)

func thousandSeparator(n int) string {
	var res []rune

	strN := strconv.Itoa(n)
	for i, r := range strN {
		res = append(res, r)

		pos := len(strN) - i - 1
		if pos%3 == 0 && pos > 0 {
			res = append(res, '.')
		}
	}

	return string(res)
}

func main() {
	fmt.Println(thousandSeparator(1))
	fmt.Println(thousandSeparator(10))
	fmt.Println(thousandSeparator(100))
	fmt.Println(thousandSeparator(1000))
	fmt.Println(thousandSeparator(10000))
	fmt.Println(thousandSeparator(100000))
	fmt.Println(thousandSeparator(1000000))
}
