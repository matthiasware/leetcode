/*
go test -bench=. -benchmem 0150_reverse_polish_notation_test.go
*/

package main

import (
	"fmt"
	"math/rand"
	"testing"
)

type DataGenerator struct{
	rng *rand.Rand
}

func NewDataGenerator(seed int64) *DataGenerator {
	return &DataGenerator{rng:rand.New(rand.NewSource(seed))}
}

func (dg *DataGenerator) Generate(rows, cols int) [][]int {
	data := make([]int, rows * cols)
	counter := 0
	for i:=0; i < len(data); {
		if dg.rng.Intn(3) == 1 {
			data[i] = counter
			i++
		}
		counter++
	}
	matrix := make([][]int, rows)
	for i := 0; i < rows; i++ {
		start := i * cols
		end := start + cols
		matrix[i] = data[start:end]
	}
	return matrix
}

func (dg *DataGenerator) GenerateTarget(minTarget, maxTarget int) int {
	return minTarget + dg.rng.Intn(maxTarget - minTarget)
}


func searchMatrix(matrix [][]int, target int) bool {	
	l, r := 0, len(matrix) - 1
	for l <= r {
		m := l + (r - l) / 2
 		innerArray := matrix[m]
 		if target >= innerArray[0] && target <= innerArray[len(innerArray) - 1] {
			// search inner array
			l, r = 0, len(innerArray) - 1
			for l <= r {
				m := l + (r - l) / 2
				if target == innerArray[m] {
					return true
				} else if target < innerArray[m] {
					r = m - 1
				} else {
					l = m + 1
				}
			}			
			return false
 		} else if target < innerArray[0] {
 			r = m - 1
 		} else {
 			l = m + 1
 		}
	}
	return false
}

var result bool

func BenchmarkSearch(b *testing.B) {
	sizes := []int{200, 400, 800}
	for _, size := range sizes {
		gen := NewDataGenerator(42)
		data := gen.Generate(size, size)
		
		dataMin := data[0][0]
		lastRow := data[len(data)-1]
		dataMax := lastRow[len(lastRow)-1]

		// pre-generate targets to avoid branch predictor bias
		targets := make([]int, 1000) 
		for i := 0; i < 1000; i++ {
			targets[i] = gen.GenerateTarget(dataMin, dataMax)
		}

		b.Run(fmt.Sprintf("Size-%d", size), func(b *testing.B) {
			b.ResetTimer()
			for i := 0; i < b.N; i++ {
				// Use modulo to cycle through our pre-generated targets
				result = searchMatrix(data, targets[i%1000])
			}
		})
	}
}