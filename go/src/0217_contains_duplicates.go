package main

import (
	"fmt"
	"slices"
)

func containsDuplicate(nums []int) bool {
	slices.Sort(nums)
	for i := 0; i <= len(nums)-2; i++ {
		if nums[i] == nums[i+1] {
			return true
		}
	}
	return false
}

type Set struct {
	items map[int]struct{}
}

func NewSet() *Set {
	return &Set{items: make(map[int]struct{}),}
}

func (set *Set) Add(item int){
	set.items[item] = struct{}{}
}

func (set *Set) Contains(item int) bool{
	_, ok := set.items[item]
	return ok
}

func (set *Set) Length() int {
	return len(set.items)
}

func constainsDuplicate_hash(nums []int) bool{
	s := NewSet()
	for _, n := range nums {
		if s.Contains(n){
			return true
		}
		s.Add(n)
		fmt.Println(s)
	}
	return false
}


func main() {
	fmt.Println(constainsDuplicate_hash([]int{0,1,2}))
}
