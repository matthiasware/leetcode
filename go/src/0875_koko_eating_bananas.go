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
	// "slices"
)

func minEatingSpeed(piles []int, h int) int {	 	
	for k := 1;; k++{
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

func main(){
	piles := []int{9,3,1,11}
	h := 7
	fmt.Println(minEatingSpeed(piles, h))
}