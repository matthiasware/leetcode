/*
853. Car Fleet
There are n cars at given miles away from the starting mile 0, traveling to reach the mile target.

You are given two integer arrays position and speed, both of length n, where position[i] is the starting mile of the ith car and speed[i] is the speed of the ith car in miles per hour.

A car cannot pass another car, but it can catch up and then travel next to it at the speed of the slower car.

A car fleet is a single car or a group of cars driving next to each other. The speed of the car fleet is the minimum speed of any car in the fleet.

If a car catches up to a car fleet at the mile target, it will still be considered as part of the car fleet.

Return the number of car fleets that will arrive at the destination.

 

Example 1:

Input: target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]

Output: 3

Explanation:
The cars starting at 10 (speed 2) and 8 (speed 4) become a fleet, meeting each other at 12. The fleet forms at target.
The car starting at 0 (speed 1) does not catch up to any other car, so it is a fleet by itself.
The cars starting at 5 (speed 1) and 3 (speed 3) become a fleet, meeting each other at 6. The fleet moves at speed 1 until it reaches target.

Example 2:
Input: target = 10, position = [3], speed = [3]
Output: 1

Explanation:
There is only one car, hence there is only one fleet.

Example 3:
Input: target = 100, position = [0,2,4], speed = [4,2,1]
Output: 1

Explanation:
The cars starting at 0 (speed 4) and 2 (speed 2) become a fleet, meeting each other at 4. The car starting at 4 (speed 1) travels to 5.
Then, the fleet at 4 (speed 2) and the car at position 5 (speed 1) become one fleet, meeting each other at 6. The fleet moves at speed 1 until it reaches target.
 

Constraints:
n == position.length == speed.length
1 <= n <= 105
0 < target <= 106
0 <= position[i] < target
All the values of position are unique.
0 < speed[i] <= 106

Recommended Time & Space Complexity
You should aim for a solution with O(nlogn) time and O(n) space, where n is the size of the input array.
*/

package main

import (
	"fmt"
	"sort"
)

type CarData struct {
	position []int
	speed []int
}

// value receiver might be faster as it won't end up at the heap
func (c CarData) Len() int {return len(c.position)}
func (c CarData) Less(i, j int) bool {return c.position[i] > c.position[j]}
func (c CarData) Swap(i, j int) {
	c.position[i], c.position[j] = c.position[j], c.position[i]
	c.speed[i], c.speed[j] = c.speed[j], c.speed[i]
}


func carFleet(target int, position []int, speed []int) int {
	// Dont start at the beginning at 0, coz for car i to know if it catches car i+1 i would need to know
	// if car i+1 catches up to a car i+x which i dont know at that point in time! 	 
	n := len(position)
	if n == 0 {
		return 0
	}

	carData := CarData{position: position, speed: speed}
	sort.Sort(carData)

	res := 1
	leadTime := float64(target-position[0]) / float64(speed[0])
	for i := 1; i < n; i++ {
		currentTime := float64(target-position[i]) / float64(speed[i])
		if currentTime > leadTime {
			res++
			leadTime = currentTime
		}
	}
	return res
}

func main(){
	// target := 12
	// position := []int{10,8,0,5,3}
	// speed := []int{2,4,1,1,3}
	target := 10
	position := []int{0,2,4}
	speed := []int{2, 3, 1}
	fmt.Println(carFleet(target, position, speed))
	// fmt.Println(position)
	// fmt.Println(speed)
}