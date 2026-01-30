/*
Binary Search

You are given an array of distinct integers nums, sorted in ascending order, and an integer target.
Implement a function to search for target within nums. If it exists, then return its index, otherwise, return -1.
Your solution must run in  O(log n) time.

Example 1:
Input: nums = [-1,0,2,4,6,8], target = 4
Output: 3

Example 2:
Input: nums = [-1,0,2,4,6,8], target = 3
Output: -1

Constraints:
1 <= nums.length <= 10000.
-10000 < nums[i], target < 10000
All the integers in nums are unique.

Recommended Time & Space Complexity
You should aim for a solution with O(logn) time and O(1) space, where n is the size of the input array.

*/

package main

import "fmt"

func search(nums []int, target int) int {
	// 0,1,2,3,4 target = 1
	// l   m   r
	// 	
	// l r	m=l
	//   r  r=l=m
	l := 0
	r := len(nums) - 1
	for l <= r {
		m := l + (r - l) / 2
		if nums[m] == target {
			return m
		} else if nums[m] < target {
			l = m + 1
		} else {
			r = m - 1
		}
	}
	return -1
}


func main(){
	// nums := []int{-1,0,3,5,9,12}
	nums := []int{0,1,2,3,4}
	target := 1
	fmt.Println(search(nums, target))
}