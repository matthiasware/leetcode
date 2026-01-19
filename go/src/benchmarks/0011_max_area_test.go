package main

import (
	"math/rand"
	"testing"
)

func MaxAreaLocal(heights []int) int {
	l, r := 0, len(heights)-1
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

func MaxAreaDirect(heights []int) int {
	l, r := 0, len(heights)-1
	var res int
	for l < r {
		volume := min(heights[l], heights[r]) * (r - l)
		res = max(res, volume)
		if heights[l] < heights[r] {
			l++
		} else {
			r--
		}
	}
	return res
}

var input []int

func init() {
	size := 100_000
	input = make([]int, size)
	for i := 0; i < size; i++ {
		input[i] = rand.Intn(1000)
	}
}

func BenchmarkMaxAreaLocal(b *testing.B) {
	for b.Loop() {
		MaxAreaLocal(input)
	}
}
func BenchmarkMaxAreaDirect(b *testing.B) {
	for b.Loop() {
		MaxAreaDirect(input)
	}
}
