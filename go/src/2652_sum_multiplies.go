package main

import "fmt"

func sumOfMultiples_naive(n int) int {
	// 3 5 7 | 9 (11) (13) 15 (17) (19) 21 (23) 25
	res := 0
	for i := 3; i <= n; i += 1 {
		if i%3 == 0 || i%5 == 0 || i%7 == 0 {
			res += i
		}
	}
	return res
}

func f(x int, k int) int {
	return x * k * (k + 1) / 2
}

func sumOfMultiples(n int) int {
	a := f(3, n/3) + f(5, n/5) + f(7, n/7)
	b := f(15, n/15) + f(21, n/21) + f(35, n/35)
	c := f(105, n/105)

	return a - b + c
}

func main() {
	type test struct {
		input  int
		expect int
	}

	var tests = []test{
		test{input: 7, expect: 21},
		test{input: 10, expect: 40},
		test{input: 9, expect: 30},
	}
	for _, t := range tests {
		actual := sumOfMultiples(t.input)
		fmt.Printf("Input: %d, Actual: %d Expected: %d\n", t.input, actual, t.expect)
	}

	fmt.Println(10 / 3)
}
