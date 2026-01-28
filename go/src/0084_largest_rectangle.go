/*
84. Largest Rectangle in Histogram
Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.

Example 1:
Input: heights = [7,1,7,2,2,4]
Output: 8

Example 2:
Input: heights = [1,3,7]
Output: 7

Constraints:
1 <= heights.length <= 1000.
0 <= heights[i] <= 1000

Recommended Time & Space Complexity
You should aim for a solution with O(n) time and O(n) space, where n is the size of the input array.
*/

package main

import "fmt"

func largestRectangleArea(heights []int) int {
	maxArea := 0
	// 1. Add a 0 to the end to force all remaining bars off the stack at the end
	heights = append(heights, 0)
	
	// 2. Start with -1 on the stack to act as a universal left boundary
	stack := []int{-1}

	for i, h := range heights {
		// 3. While current height is shorter than the bar at stack top, pop and calculate
		for len(stack) > 1 && h < heights[stack[len(stack)-1]] {
			topIdx := stack[len(stack)-1]
			stack = stack[:len(stack)-1]
			
			// Height of the bar we just popped
			height := heights[topIdx]
			
			// Width is (current index) - (new stack top) - 1
			width := i - stack[len(stack)-1] - 1
			
			if area := height * width; area > maxArea {
				maxArea = area
			}
		}
		// 4. Always push the current index
		stack = append(stack, i)
	}

	return maxArea
} 
type Test struct {
	heights []int
	area    int
}

func main() {
	tests := []Test{
		Test{[]int{3}, 3},
		Test{[]int{1, 2, 7}, 7},
		Test{[]int{1, 2, 7, 2, 2}, 8},
		// Test{[]int{1,2,7,2,2,1,1,1,1}, 9}
		// Test{[]int{7,1,7,2,2,4}, 8},
	}
	for _, test := range tests {
		act := largestRectangleArea(test.heights)
		var col string
		if act == test.area {
			col = "\033[32m"
		} else {
			col = "\033[31m"
		}
		fmt.Printf("%v act: %3d exp: %3d heights=%v\n", col, act, test.area, test.heights)
	}
}
