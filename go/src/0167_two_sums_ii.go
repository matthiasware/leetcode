/*
Given an array of integers numbers that is sorted in non-decreasing order.

Return the indices (1-indexed) of two numbers, [index1, index2], such that they add up to a given target number target and index1 < index2. Note that index1 and index2 cannot be equal, therefore you may not use the same element twice.

There will always be exactly one valid solution.

Your solution must use O(1) additional space.

Example 1:
Input: numbers = [1,2,3,4], target = 3

Output: [1,2]
Explanation:
The sum of 1 and 2 is 3. Since we are assuming a 1-indexed array, index1 = 1, index2 = 2. We return [1, 2].

Example 2:
Input: numbers = [1,3,4,5], target = 7
Output: [2,3]

Constraints:

2 <= numbers.length <= 1000
-1000 <= numbers[i] <= 1000
-1000 <= target <= 1000


Recommended Time & Space Complexity
You should aim for a solution with O(n) time and O(1) space, where n is the size of the input array.
*/

package main

import "fmt"

func twoSum(numbers []int, target int) []int {
	left := 0
	right := len(numbers) - 1
	for left < right {
		sum := numbers[left] + numbers[right]
		if sum < target {
			left++
		} else if sum > target {
			right--
		} else {
			break
		}
	}
	return []int{left + 1, right + 1}
}

func main() {
	// numbers := []int{2,7,11,15}
	// target := 9
	numbers := []int{1, 2, 3, 4}
	target := 3
	fmt.Println(twoSum(numbers, target))
}
