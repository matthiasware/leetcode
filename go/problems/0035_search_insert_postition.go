package main

import (
	"fmt"
)

func searchInsert(nums []int, target int) int {
	l := 0
	r := len(nums) - 1
	for l <= r {
		m := l + (r-l)/2
		if nums[m] == target {
			return m
		} else if target > nums[m] {
			l = m + 1
		} else {
			r = m - 1
		}
	}
	return l
}

func main() {
	//fmt.Println(searchInsert([]int{1, 3, 5, 6}, 5))
	fmt.Println(searchInsert([]int{1, 3, 5, 6}, 2))
}
