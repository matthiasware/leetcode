/*
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49

Input: height = [1,1]
Output: 1

Input: height = [1,7,2,5,4,7,3,6]
Output: 36

Input: height = [2,2,2]
Output: 4

Recommended Time & Space Complexity:
You should aim for a solution with O(n) time and O(1) space, where n is the size of the input array.

Constraints:
n == height.length
2 <= n <= 105
0 <= height[i] <= 104
*/

package main

import "fmt"

func maxArea(heights []int) int {
	l,r := 0, len(heights) - 1
	var res int
	for l < r {
		hl := heights[l]
		hr := heights[r]
		volume := min(hl, hr) * (r - l)
		res = max(res, volume)
		if hl < hr {
			l++
		} else {
			r--
		}
	}
	return res
}

func main(){
	// heights := []int{1,8,6,2,5,4,8,3,7}
	heights := []int{1,2,2,4}
	fmt.Println(maxArea(heights))
}