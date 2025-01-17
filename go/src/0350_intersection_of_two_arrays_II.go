package main

import (
	"fmt"
	"reflect"
	"slices"
)

func intersect(nums1 []int, nums2 []int) []int {
	intersection := []int{}
	slices.Sort(nums1)
	slices.Sort(nums2)
	for i1, i2 := 0, 0; i1 < len(nums1) && i2 < len(nums2); {
		n1 := nums1[i1]
		n2 := nums2[i2]
		if n1 == n2 {
			intersection = append(intersection, n1)
			i1++
			i2++
		} else if n1 < n2 {
			i1++
		} else {
			i2++
		}
	}
	return intersection
}
func main() {
	type Test struct {
		nums1 []int
		nums2 []int
		exp   []int
	}
	tests := []Test{
		Test{[]int{1, 2, 2, 1}, []int{2, 2}, []int{2, 2}},
		Test{[]int{4, 9, 5}, []int{9, 4, 9, 8, 4}, []int{9, 4}},
	}
	for _, t := range tests {
		act := intersect(t.nums1, t.nums2)
		slices.Sort(act)
		slices.Sort(t.exp)
		if !reflect.DeepEqual(act, t.exp) {
			fmt.Printf("%v != %v\n", act, t.exp)
		}
	}
}
