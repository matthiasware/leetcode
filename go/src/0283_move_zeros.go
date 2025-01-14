package main

import (
	"fmt"
	"strings"
)

func switchElements(nums []int, i int, j int) {
	tmp := nums[j]
	nums[j] = nums[i]
	nums[i] = tmp
}
func moveZeroes_naive(nums []int) {
	// Time O(n^2)
	for i := len(nums) - 1; i >= 0; i-- {
		if nums[i] != 0 {
			continue
		}
		for j := i + 1; j < len(nums); j++ {
			if nums[j] == 0 {
				break
			}
			switchElements(nums, j-1, j)
		}
	}
}

func moveZeros(nums []int) {
	/*
		Idea: Partition like quicksort!
		Time: O(n)
		Memo: O(1)
	*/
	left := 0
	for right := 0; right < len(nums); right++ {
		if nums[right] != 0 {
			nums[left], nums[right] = nums[right], nums[left]
			left++
		}
	}
}

func main() {
	type Test struct {
		nums []int
		exp  []int
	}
	tests := []Test{
		Test{[]int{0}, []int{0}},
		Test{[]int{0, 1}, []int{1, 0}},
		Test{[]int{0, 1, 2}, []int{1, 2, 0}},
		Test{[]int{0, 0, 2}, []int{2, 0, 0}},
		Test{[]int{0, 1, 0, 3, 12}, []int{1, 3, 12, 0, 0}},
	}

	for _, t := range tests {
		fmt.Println(t.nums, t.exp)
		moveZeros(t.nums)
		fmt.Println(t.nums)
		fmt.Println(strings.Repeat("-", 10))
	}
}
