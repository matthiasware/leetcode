/*
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.

Input: height = [4,2,0,3,2,5]
Output: 9

Constraints:

n == height.length
1 <= n <= 2 * 104
0 <= height[i] <= 105

Recommended Time & Space Complexity
You should aim for a solution as good or better than O(n) time and O(n) space, where n is the size of the input array.
*/

package main

import (
	"fmt"
)

func trap_prefix_suffix(height []int) int {
	prefix_max := make([]int, len(height))
	suffix_max := make([]int, len(height))
	
	for i:=1;i<len(height);i++{
		prefix_max[i] = max(prefix_max[i-1], height[i-1])
	}
	for i:=len(height)-2;i>=0;i--{
		suffix_max[i] = max(suffix_max[i+1], height[i+1])
	}
	res := 0
	for i:=0;i<len(height);i++{
		res += max(min(prefix_max[i], suffix_max[i]) - height[i],0)
	}
	
	return res
}

func trap(height []int) int {
	if len(height) < 2 {
		return 0
	}
	left, right := 0, len(height) - 1
	leftMax, rightMax := height[left], height[right]
	res := 0
	
	for left < right {
		if leftMax < rightMax{
			left++
			leftMax = max(leftMax, height[left])
			res += leftMax - height[left]
		} else {
			right--
			rightMax = max(rightMax, height[right])
			res += rightMax - height[right]
		}
	}
	return res
	
	return 0
}



func main(){
	height := []int{4,2,0,3,2,5}
	height = []int{0,1,0,2,1,0,1,3,2,1,2,1}
	res := trap(height)
	fmt.Println(res)
}