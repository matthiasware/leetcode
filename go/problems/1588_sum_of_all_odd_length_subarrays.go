package main

import (
	"fmt"
)

/*
For array for len we have
l=1, n=1 -> [1]
			 1
l=2, n=2 -> [1], [2]
			 1    1
l=3, n=4 -> [1], [2], [3]
			[1,   2,   3]
   			 2,   2,   2
l=4, n=6- > [1], [2], [3], [4]
			[1,   2,   3]
				  [2,  3,   4]

			2     3    3    2
l=5, n=9 -> [1], [2], [3], [4], [5]
			[1,   2,   3]
				 [2,   3,   4]
					   [3,  4,   5]
			[1,   2,    3,  4,   5]
			3     4     5   4    3

l=6, n=..
[1], [2], [3], [4], [5] [6]
[1,   2,   3]
     [2,   3,   4]
          [3,   4,   5]
               [4,   5,  6]
[1,   2,    3,  4,   5]
     [2,    3,  4,   5,   6]
3     5     6   6    5    3

l=7, n=..
[1], [2], [3], [4], [5], [6], [ ]
[1,   2,   3]
     [2,   3,   4]
          [3,   4,   5]
               [4,   5,   6]
					 [5,  6,   7]
[1,   2,   3,   4,   5]
     [2,   3,   4,   5,   6]
          [3,   4,   5,   6,   7]
[1,   2,   3,   4,   5,   6,   7]
 4    6    8    8    8    6    4


1: 1,1,2,2,3,3,4
2:   1,2,3,4,5,6
3:     2,3,5,6,8
4:       2,4,6,8
5:         3,5,8
6:           3,6
7:             4

USE THIS SERIES:
1: 1,1,2,2,3,3,4  (+0,+1)
2: 1,2,3,4,5,6    (+1,+1)
3: 2,3,5,6,8      (+1,+2)
4: 2,4,6,8        (+2,+2)
5: 3,5,8          (+2,+3)
6: 3,6            (+3,+3)
7: 4              (+3,+4)
*/

func sum(slice []int) int {
	var total int // Initialize the zero value for the type
	for _, value := range slice {
		total += value
	}
	return total
}

func sumOddLengthSubarrays(arr []int) int {
	// Brute force
	// Calculate the length of each subarray
	res := 0
	for l := 1; l <= len(arr); l += 2 {
		for i := 0; i < (len(arr) - l + 1); i++ {
			sa := arr[i : i+l]
			res += sum(sa)
		}
	}
	return res
}

type test struct {
	arr []int
	sum int
}

func main() {
	tests := []test{
		test{[]int{2}, 2},
		test{[]int{1, 2}, 3},
		test{[]int{10, 11, 12}, 66},
		//test{[]int{1, 4, 2, 5, 3}, 58},
	}
	for _, t := range tests {
		exp := t.sum
		act := sumOddLengthSubarrays(t.arr)
		fmt.Println("Result:", exp, act)
	}
}
