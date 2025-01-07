package main

import (
	"fmt"
	"sort"
)

type Descending []int

func (d Descending) Len() int           { return len(d) }
func (d Descending) Less(i, j int) bool { return d[i] > d[j] } // Reverse order for descending
func (d Descending) Swap(i, j int)      { d[i], d[j] = d[j], d[i] }

func deleteGreatestValue(grid [][]int) int {
	// grid of (n * m)
	// Time: O(n * m log m)
	// Memo: O(1)
	for row_idx := range len(grid) {
		sort.Sort(Descending(grid[row_idx]))
	}
	res := 0
	for col_idx := range len(grid[0]) {
		colMax := 0
		for row_idx := range len(grid) {
			colMax = max(colMax, grid[row_idx][col_idx])
		}
		res += colMax
	}
	return res
}

func main() {
	grid := [][]int{{1, 2, 3}, {4, 5, 6}, {9, 8, 7}}
	r := deleteGreatestValue(grid)
	fmt.Println(r, grid, len(grid))
	a := []int{4, 3, 2, 1}
	fmt.Println(a)
	arr := []int{5, 2, 9, 1, 6, 3}

	// Sorting in descending order
	sort.Sort(Descending(arr))
	fmt.Println("Sorted in descending order:", arr)

	fmt.Println(grid)
	fmt.Println(grid[0:2])

	grid = [][]int{{1, 2, 4}, {3, 3, 1}}
	fmt.Println(deleteGreatestValue(grid))

}
