/*
Search a 2D Matrix
You are given an m x n 2-D integer array matrix and an integer target.

Each row in matrix is sorted in non-decreasing order.
The first integer of every row is greater than the last integer of the previous row.
Return true if target exists within matrix or false otherwise.

Can you write a solution that runs in O(log(m * n)) time?

Example 1:
Input: matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]], target = 10
Output: true

Example 2:
Input: matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]], target = 15
Output: false

Constraints:
m == matrix.length
n == matrix[i].length
1 <= m, n <= 100
-10000 <= matrix[i][j], target <= 10000

Recommended Time & Space Complexity
You should aim for a solution with O(log(m * n)) time and O(1) space, where m is the number of rows and n is the number of columns in the matrix.
*/

package main

import "fmt"


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

func main(){
	matrix := [][]int{
		{1,2,4,8},
		{10,11,12,13},
		{14,20,30,40},
	}
	target := 35
	fmt.Println(searchMatrix(matrix, target))
}