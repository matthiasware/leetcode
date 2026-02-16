/*
You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Example 1:
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.


Constraints:

1 <= prices.length <= 105
0 <= prices[i] <= 104
*/

package main

import "fmt"

func maxProfitNaive(prices []int) int {
	res := 0
	for i := 0; i < len(prices)-1; i++ {
		for j := i + 1; j < len(prices); j++ {
			res = max(res, prices[j]-prices[i])
		}
	}
	return res
}

func maxProfit(prices []int) int {
	res := 0
	l := 0
	r := 1
	for r < len(prices) {
		if prices[r] > prices[l] {
			res = max(res, prices[r]-prices[l])
		} else {
			l = r
		}
		r++
	}
	return res
}

func main() {
	prices := []int{7, 1, 5, 3, 6, 4}
	// prices = []int{1,2,3,5}
	res := maxProfit(prices)
	fmt.Println(res)
}
