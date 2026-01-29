/*
go test -bench=. -benchmem 0150_reverse_polish_notation_test.go
*/

package main

import (
	"fmt"
	"math/rand"
	"sort"
	"testing"
)

// Generates Testing Data
type DataGenerator struct {
	rng *rand.Rand
}

func NewDataGenerator(seed int64) *DataGenerator {
	return &DataGenerator{rng: rand.New(rand.NewSource(seed))}
}

func (dg *DataGenerator) CreateSortedSlice(size int) []int {
	slice := make([]int, size)
	for i := 0; i<size; i++{
		slice[i] = dg.rng.Intn(size * 10)
	}
	sort.Ints(slice)
	return slice
}


func search(nums []int, target int) int {
	// 0,1,2,3,4 target = 1
	// l   m   r
	// 	
	// l r	m=l
	//   r  r=l=m
	l := 0
	r := len(nums) - 1
	for l <= r {
		m := l + (r - l) / 2
		if nums[m] == target {
			return m
		} else if nums[m] < target {
			l = m + 1
		} else {
			r = m - 1
		}
	}
	return -1
}

func searchOpt1(nums []int, target int) int {
	// Idea: remove all possiblities except one
	// reduce the number of branches and single exit
	// uint, why use it?
	//    - int division performs arithmetic shift to preserve sign bit
	//    - uint division performs logical shift which is faster  	 	 	
    n := uint(len(nums))
    l := uint(0)
    r := n
    
    for l < r {
        m := l + (r-l)/2
        if nums[m] < target {
            l = m + 1
        } else {
            r = m
        }
    }
    if l < n && nums[l] == target {
        return int(l)
    }
    return -1
}

func BenchmarkBinarySearch(b *testing.B){
	sizes := []int{100, 1000}
	for _, size := range sizes {
		gen := NewDataGenerator(42)
		data := gen.CreateSortedSlice(size)
		target := data[size/2]
		
		b.Run(fmt.Sprintf("Size-%d", size), func(b *testing.B) {
			b.ResetTimer()
			for i := 0; i < b.N; i++ {
				search(data, target)
			}
		})
	}
}

func BenchmarkBinarySearchOpt1(b *testing.B){
	sizes := []int{100, 1000}
	for _, size := range sizes {
		gen := NewDataGenerator(42)
		data := gen.CreateSortedSlice(size)
		target := data[size/2]
		
		b.Run(fmt.Sprintf("Size-%d", size), func(b *testing.B) {
			b.ResetTimer()
			for i := 0; i < b.N; i++ {
				searchOpt1(data, target)
			}
		})
	}
}
