// go test -bench=. -benchmem 0121_best_time_to_buy_and_sell_stocks_test.go

package main

import (
	"math/rand/v2"
	"testing"
)

func getRandomSlice(n, maxInt int) []int {
	res := make([]int, n)
	for i := range res {
		res[i] = rand.IntN(maxInt)
	}
	return res
}

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

var testSlices [][]int

func init() {
	testSlices = make([][]int, 10)
	for i := 0; i < 10; i++ {
		testSlices[i] = getRandomSlice(10000, 5000)
	}
}

func Benchmark_Naive(b *testing.B) {
	i := 0
	for b.Loop() {
		maxProfitNaive(testSlices[i%10])
		i++
	}
}

func Benchmark_Better(b *testing.B) {
	i := 0
	for b.Loop() {
		maxProfit(testSlices[i%10])
		i++
	}
}

func Benchmark_Opt(b *testing.B) {
	i := 0
	for b.Loop() {
		maxProfitOpt(testSlices[i%10])
		i++
	}
}
