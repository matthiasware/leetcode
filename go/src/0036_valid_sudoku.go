/*
36. Valid Sudoku
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.

Constraints:
- board.length == 9
- board[i].length == 9
- board[i][j] is a digit 1-9 or '.'.

Recommended Time & Space Complexity
You should aim for a solution as good or better than O(n^2) time and O(n^2) space, where n is the number of rows in the square grid.
*/

package main

import (
	"fmt"
)

func checkAndMark(nums *[9]bool, val byte) bool {
	if val == '.'{
		return true
	}
	// actually we would convert via intVal := int(val - '0')
	// however we would than need to lookup via nums[intVal - 1]
	// so we try to be more efficient here 	
	intVal := int(val - '1')
	if nums[intVal] {
		return false
	}
	nums[intVal] = true
	return true
}

func isValidSudoku(board [][]byte) bool {
	// row wise
	for r:=0; r<9;r++ {
		nums := [9]bool{}
		for c:=0;c<9;c++{
			if !checkAndMark(&nums, board[r][c]){
				return false
			}
		}
	}
	// col wise
	for c:=0; c<9;c++ {
		nums := [9]bool{}
		for r:=0;r<9;r++{
			if !checkAndMark(&nums, board[r][c]){
				return false
			}
		}
	}
	// cell wise
	for r := 0; r<3; r++{
		for c :=0; c<3; c++ {
			nums := [9]bool{}
			for i := r * 3; i < r*3 + 3; i++{
				for j := c * 3; j<c*3+3; j++ {
					if !checkAndMark(&nums, board[i][j]){
						return false
					}
				}
			}
		}
	}
	return true	 	
}

func main(){
 	board := [][]byte{
    	{'1', '2', '.', '.', '3', '.', '.', '.', '.'},
    	{'4', '.', '.', '5', '.', '.', '.', '.', '.'},
    	{'.', '9', '8', '.', '.', '.', '.', '.', '3'},
    	{'5', '.', '.', '.', '6', '.', '.', '.', '4'},
    	{'.', '.', '.', '8', '.', '3', '.', '.', '5'},
    	{'7', '.', '.', '.', '2', '.', '.', '.', '6'},
    	{'.', '.', '.', '.', '.', '.', '2', '.', '.'},
    	{'.', '.', '.', '4', '1', '9', '.', '.', '8'},
    	{'.', '.', '.', '.', '8', '.', '.', '7', '9'},
	}
	res := isValidSudoku(board)
	fmt.Println(res)
}