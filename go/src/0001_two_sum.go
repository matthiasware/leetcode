package main

import (
	"fmt"
	"github.com/stretchr/testify/assert"
	"slices"
	"testing"
)

func twoSum_naive(nums []int, target int) []int {
	for i := 0; i < len(nums); i++ {
		m := nums[i]
		for j := i + 1; j < len(nums); j++ {
			n := nums[j]
			if m+n == target {
				return []int{i, j}
			}
		}
	}
	return nil
}

func twoSum_range(nums []int, target int) []int {
	for i, m := range nums {
		for j, n := range nums[i+1:] {
			if m+n == target {
				return []int{i, j + i + 1}
			}
		}
	}
	return nil
}

func twoSum(nums []int, target int) []int {
	valToIdx := make(map[int]int)
	for i, n := range nums {
		m := target - n
		j, ok := valToIdx[m]
		if ok {
			return []int{j, i}
		}
		valToIdx[n] = i
	}
	return nil
}

func TestSlicesEqual(t *testing.T) {
	slice1 := []int{1, 2, 3}
	slice2 := []int{1, 2, 3}

	assert.Equal(t, slice1, slice2, "The slices should be equal")
}

func main() {
	var nums = []int{2, 7, 11, 15}
	target := 9
	expected := []int{0, 1}
	actual := twoSum(nums, target)

	fmt.Println(actual)
	fmt.Println(expected)

	if !slices.Equal(nums, expected) {
		fmt.Println("The slices should be equal")
	}
}
