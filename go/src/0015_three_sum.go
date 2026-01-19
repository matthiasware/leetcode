/*
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] where nums[i] + nums[j] + nums[k] == 0, and the indices i, j and k are all distinct.

The output should not contain any duplicate triplets. You may return the output and the triplets in any order.

Example 1:
Input: nums = [-1,0,1,2,-1,-4]

Output: [[-1,-1,2],[-1,0,1]]
Explanation:
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].

Example 2:
Input: nums = [0,1,1]

Output: []
Explanation: The only possible triplet does not sum up to 0.

Example 3:
Input: nums = [0,0,0]

Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.

Constraints:

3 <= nums.length <= 1000
-10^5 <= nums[i] <= 10^5


Recommended Time & Space Complexity
You should aim for a solution with O(n^2) time and O(1) space, where n is the size of the input array.
*/

package main

import (
	"fmt"
	"sort"
)

func threeSum(nums []int) [][]int {
	/*
	Time O(n^3)
	Space O(m) where m is the number of triplets
	*/
	resMap := map[[3]int]struct{}{}
	sort.Ints(nums)
	for i:=0; i<len(nums) - 2; i++ {
		for j:=i+1; j < len(nums) - 1; j++{
			for k:=j; k < len(nums); k++ {
				if nums[i] + nums[j] + nums[k] == 0 {
					resMap[[3]int{nums[i], nums[j], nums[k]}] = struct{}{}
				}
			}
		}
	}
	res := [][]int{}
	for k, _ := range resMap {
		res = append(res, []int{k[0], k[1], k[2]})
	}
	return res
}




func main(){
	nums := []int{-1,0,1,2,-1,-4}
	fmt.Println(threeSum(nums))
}