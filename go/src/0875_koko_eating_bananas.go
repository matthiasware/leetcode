/*
Koko Eating Bananas
You are given an integer array piles where piles[i] is the number of bananas in the ith pile. You are also given an integer h, which represents the number of hours you have to eat all the bananas.

You may decide your bananas-per-hour eating rate of k. Each hour, you may choose a pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, you may finish eating the pile but you can not eat from another pile in the same hour.

Return the minimum integer k such that you can eat all the bananas within h hours.

Example 1:
Input: piles = [1,4,3,2], h = 9
Output: 2

Explanation: With an eating rate of 2, you can eat the bananas in 6 hours. With an eating rate of 1, you would need 10 hours to eat all the bananas (which exceeds h=9), thus the minimum eating rate is 2.

Example 2:
Input: piles = [25,10,23,4], h = 4

Output: 25
Constraints:
1 <= piles.length <= 1,000
piles.length <= h <= 1,000,000
1 <= piles[i] <= 1,000,000,000

Recommended Time & Space Complexity
You should aim for a solution with O(nlogm) time and O(1) space, where n is the size of the input array, and m is the maximum value in the array.


*/

package main

import (
	"fmt"
	// "math"
	"slices"
)

func minEatingSpeedNaive(piles []int, h int) int {
	for k := 1; ; k++ {
		hours := 0
		// check whether k works
		for _, height := range piles {
			// integer equicalent of math.Ceil
			//  e.g. 11 / 4 = (11 + 4 - 1) / 4 = 3
			//  e.g. 12 / 4 = (12 + 4 - 1) / 4 = 3
			hours += (height + k - 1) / k
			if hours > h {
				break
			}
		}
		if hours <= h {
			return k
		}
	}
}

func minEatingSpeed(piles []int, h int) int {
	/*
		Binary serach on the rate
	*/
	l := 1
	r := slices.Max(piles)
	for l < r {
		// Pick a candidate rate and check if this works
		rate := (l + r) / 2
		curHours := 0
		for _, height := range piles {
			curHours += (height + rate - 1) / rate
			if curHours > h {
				break
			}
		}
		fmt.Printf("l=%5d r=%5d rate=%5d curHours=%5d hours=%5d\n", l, r, rate, curHours, h)
		if curHours <= h {
			// This rate works, but maybe we kann go solwer
			r = rate
		} else {
			// Too slow, thus we need to increase the rate
			l = rate + 1
		}
	}
	// when l == r, we found the rate
	return l
}

func main() {
	// piles := []int{9,3,1,11}
	// h := 7
	// piles := []int{1,4,3,2}
	// h := 9
	// piles := []int{312884470}
	// h := 312884469
	piles := []int{3, 6, 7, 11}
	h := 8
	fmt.Println("ACT:", minEatingSpeed(piles, h))
	fmt.Println("EXP:", minEatingSpeedNaive(piles, h))
}
