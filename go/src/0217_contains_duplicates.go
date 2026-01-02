package main

import (
	"fmt"
	"slices"
)

func containsDuplicate(nums []int) bool {
	slices.Sort(nums)
	for i := 0; i <= len(nums)-2; i++ {
		if nums[i] == nums[i+1] {
			return true
		}
	}
	return false
}


func main() {
	fmt.Println(containsDuplicate([]int{0,0}))
}
