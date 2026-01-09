/*
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
The test cases are generated such that the answer is always unique.

Example 1:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:
Input: nums = [1], k = 1
Output: [1]

Example 3:
Input: nums = [1,2,1,2,1,2,3,1,3,2], k = 2
Output: [1,2]

You should aim for a solution with O(n) time and O(n) space, where n is the size of the input array.
*/

package main


import (
	"fmt"
	"slices"
)

func topKFrequentNaive(nums []int, k int ) []int {
	// n ... len(nums)
	// Time: O(n log n)
	// Space: O(n)

	// calculate frequencies 	
	freqs := map[int]int{}
	
	for _, n := range nums {
		freqs[n]++
	}
	// sort keys 	
	keys := make([]int, 0, len(freqs))
	for k := range freqs {
		keys = append(keys, k)
	}
	
	slices.SortFunc(keys, func(a, b int) int {
		return freqs[b] - freqs[a]
	})
	// return tok k 	
	return keys[:k]
}

func topKFrequent(nums []int, k int) []int {
	// calculate counts
	counts := make(map[int]int)
	for _, n := range nums {
		counts[n]++
	}
	// bucketize counts
	buckets := make([][]int, len(nums) + 1)
	for k, v := range counts {
		buckets[v] = append(buckets[v], k)
	}
	// // go through buckets until we got k elements	
	result := make([]int, 0, k)
	for i := len(buckets) - 1; i >= 0; i-- {
		for _, num := range buckets[i]{
			result = append(result, num)
			if len(result) == k {
				return result
			}
		}
	}
	return result
}


func main() {
	nums := []int{1,2,1,2,1,2,3,1,3,2}
	k := 2
	fmt.Println(topKFrequent(nums, k))
}