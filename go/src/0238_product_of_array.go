/*
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]

Constraints:
- 2 <= nums.length <= 1000
- -20 <= nums[i] <= 20
*/

package main

import "fmt"

func productExceptSelf_ARRAY(nums []int) []int {
	// input  [1,2,3,4]
	// prefix [1,1,2,6]
	// suffix [24,12,4,1]
	// output [24,12,8,6] 		
	res := make([]int, len(nums))
	prefix := make([]int, len(nums))
	prefix[0] = 1
	for i:=1; i<len(nums); i++ {
		prefix[i] = prefix[i-1] * nums[i-1]
	}
	suffix := make([]int, len(nums))
	suffix[len(nums) - 1] = 1
	for i:=len(nums) - 2; i>=0; i--{
		suffix[i] = suffix[i+1] * nums[i+1]
	}
	for i:=0; i<len(nums); i++ {
		res[i] = prefix[i] * suffix[i]
	}
	return res
}

func productExceptSelf_Improved(nums []int) []int {	
	n := len(nums)
	res := make([]int, n)
	prefix := 1
	for i:=0;i<len(nums);i++{
		res[i] = prefix
		prefix *= nums[i]
	}
	suffix := 1
	for i:=n-1;i>=0;i--{
		res[i] *= suffix
		suffix *= nums[i]
	}
	return res
}

func productExceptSelf(nums []int) []int {	
	n := len(nums)
	res := make([]int, n)
	nZeros := 0
	totalNonZero := 1
	for _, n := range nums {
		if n == 0 {
			nZeros++
		} else {
			totalNonZero *= n
		}
	}
	switch nZeros {
		case 0:
			for i, num := range nums {
				res[i] = totalNonZero / num
			}
		case 1:
			for i, num := range nums {
				if num == 0 {
					res[i] = totalNonZero
					break
				}
			}
	}
	return res
}



func main(){
	// nums := []int{1,2,3,4}
	nums := []int{-1,0,1,2,3}
	res := productExceptSelf(nums)
	fmt.Println(res)
}