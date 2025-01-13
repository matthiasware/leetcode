package main

import "fmt"

func threeConsecutiveOdds(arr []int) bool {
	ncs := 0
	for _, n := range arr {
		if n&1 == 1 {
			ncs++
		} else {
			ncs = 0
		}
		if ncs == 3 {
			return true
		}
	}
	return false
}

func main() {
	r := threeConsecutiveOdds([]int{1, 2, 1, 1})
	fmt.Println(r)
	r = threeConsecutiveOdds([]int{2, 6, 4, 1})
	fmt.Println(r)
	r = threeConsecutiveOdds([]int{1, 2, 34, 3, 4, 5, 7, 23, 12})
	fmt.Println(r)
}
