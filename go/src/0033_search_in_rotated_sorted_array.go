/*
33. Search in Rotated Sorted Array

There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly left rotated at an unknown index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be left rotated by 3 indices and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.

 
Example 1:
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

Example 2:
Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1

Example 3:
Input: nums = [1], target = 0
Output: -1
 

Constraints:
1 <= nums.length <= 5000
-104 <= nums[i] <= 104
All values of nums are unique.
nums is an ascending array that is possibly rotated.
-104 <= target <= 104
*/

package main

import "fmt"

func search(nums []int, target int) int {
	//  [1, 0]
	//   l
	//      r
	//   m
 	// Part 1) Find Pivot element
 	//         Pivot is the index of the smallest element
 	l, r := 0, len(nums) - 1
 	for l < r {
 		m := (l + r) / 2
 		if nums[m] > nums[r] {
 			l = m + 1
 		} else {
 			r = m
 		}
 	}
 	// Part 2) Chose subarray
 	pivot := l
 	l, r = 0, len(nums) - 1
 	if target >= nums[pivot] && target <= nums[r] {
 		l = pivot
 	} else {
 		r = pivot - 1
 	}
 	// Part 3) Find target in subarray
 	for l < r {
 		m := (l + r) / 2
 		if nums[m] < target {
 			l = m + 1
 		} else {
 			r = m
 		}
 	}
 	if nums[l] == target {
 		return l
 	}
	return -1
}

type Test struct {
	nums []int
	target int
	result int
}


func main(){
	tests := []Test {
		{[]int{0}, 0, 0},
		{[]int{0}, 1, -1},
		{[]int{0, 1}, 1, 1},
		{[]int{1, 0}, 1, 0},
		{[]int{0,1,3,4}, 1, 1},
		{[]int{0,1,3,4}, -1, -1},
		{[]int{0,1,3,4}, 5, -1},
		{[]int{6,8,0,2,4}, 6, 0},
		{[]int{6,8,0,2,4}, 2, 3},
		{[]int{6,8,0,2,4}, 5, -1},
		{[]int{6,8,0,2,4}, 3, -1},
		{[]int{4,5,6,7,0,1,2}, 0, 4},
		{[]int{4,5,6,7,0,1,2}, 3, -1},
	}
	for _, test := range tests {
		act := search(test.nums, test.target)
		if act != test.result {
			fmt.Printf("\033[31m nums = %v, target = %d exp!=act: %d != %d \033[0m\n", test.nums, test.target, test.result, act)
		} else {
			fmt.Printf("nums = %v, target = %d exp!=act: %d == %d\n", test.nums, test.target, test.result, act)
		}
	}
}