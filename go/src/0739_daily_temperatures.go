/*
739. Daily Temperatures

Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

Example 1:
Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]

Example 2:
Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]

Example 3:
Input: temperatures = [30,60,90]
Output: [1,1,0]

Constraints:
1 <= temperatures.length <= 105
30 <= temperatures[i] <= 100

Recommended Time & Space Complexity
You should aim for a solution as good or better than O(n) time and O(n) space, where n is the size of the input array.

Naive Solution
*/

package main

import "fmt"

func dailyTemperaturesNaive(temperatures []int) []int {
	// Space: O(1)
	// Time:
	res := make([]int, len(temperatures))
	for i := range len(temperatures) {
		for j := i + 1; j < len(temperatures); j++ {
			if temperatures[j] > temperatures[i] {
				res[i] = j - i
				break
			}
		}
	}
	return res
}

func dailyTemperatures(temperatures []int) []int {
	// Space: O(n)
	// Time: O(n)
	res := make([]int, len(temperatures))
	stack := []int{}
	for i, t := range temperatures {
		for len(stack) > 0 && t > temperatures[stack[len(stack)-1]] {
			stackIdx := stack[len(stack)-1]
			stack = stack[:len(stack)-1]
			res[stackIdx] = i - stackIdx
		}
		stack = append(stack, i)
	}
	return res
}

func main() {
	temps := []int{73, 74, 75, 71, 69, 72, 76, 73}
	fmt.Println(dailyTemperatures(temps))
}
