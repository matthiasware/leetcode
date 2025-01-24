package main

func removeDuplicates(nums []int) int {
	nShifts := 0
	for i := 1; i < len(nums); i++ {
		if nums[i] == nums[i-1] {
			nShifts += 1
			continue
		}
		if nShifts > 0 {
			nums[i-nShifts] = nums[i]
		}
	}
	return len(nums) - nShifts
}
