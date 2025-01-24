package main

func removeElement(nums []int, val int) int {
	/*
		Time: O(n)
		Memo: O(1)
	*/
	nShifts := 0
	for i := 0; i < len(nums); i++ {
		if nums[i] != val {
			nums[i-nShifts] = nums[i]
		} else {
			nShifts++
		}
	}
	return len(nums) - nShifts
}

func main() {

}
