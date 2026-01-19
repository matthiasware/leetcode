/*
Given an array of integers nums, return the length of the longest consecutive sequence of elements that can be formed.

A consecutive sequence is a sequence of elements in which each element is exactly 1 greater than the previous element. The elements do not have to be consecutive in the original array.

You must write an algorithm that runs in O(n) time.

Example 1:

Input: nums = [2,20,4,10,3,4,5]

Output: 4
Explanation: The longest consecutive sequence is [2, 3, 4, 5].

Example 2:

Input: nums = [0,3,2,5,4,6,1,1]

Output: 7

Constraints:
0 <= nums.length <= 1000
-10^9 <= nums[i] <= 10^9

1,3,4,2

1,5,3,4
1
3,4,5

1,5,4,6,2
1,2
4,5,6

Idea:
- store all elements in a set
- calculate length of sequence starting only from beggings
- a number is the beginning of a sequence, if number - 1 is not part of the set


*/

package main

import (
	"fmt"
	"sort"
)

func longestConsecutiveNaive(nums []int) int {
	// Time:   O(n log n)
	// Memory: O(1)
	if len(nums) == 0 {
		return 0
	}
	if len(nums) == 1 {
		return 1
	}
	sort.Ints(nums)
	longest := 1
	current := 1
	for i := 1; i < len(nums); i++ {
		if nums[i] == nums[i-1]+1 {
			current++
		} else {
			current = 1
		}
		longest = max(longest, current)
	}
	return longest
}

func longestConsecutive(nums []int) int {
	// Time O(n)
	// Memory O(n)
	// Idea: convert to
	//	- convert nums to set
	// 	- only calculculate length starting from beginning of sequcene
	//  - num is beginning is num-1 is not part of set
	set := make(map[int]struct{})
	for _, num := range nums {
		set[num] = struct{}{}
	}
	longest := 0
	for num, _ := range set {
		if _, ok := set[num-1]; ok {
			continue
		}
		length := 1
		for {
			if _, ok := set[num+length]; ok {
				length++
			} else {
				break
			}
		}
		longest = max(longest, length)

	}
	return longest
}

func main() {
	// nums := []int{100,4,200,1,3,2}
	// nums := []int{1,3,4,6,7,8}
	nums := []int{1}
	fmt.Println(longestConsecutive(nums))
}
