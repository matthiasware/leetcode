package main

import "fmt"

func romanToInt(s string) int {
	symMap := map[rune]int{
		'I': 1,
		'V': 5,
		'X': 10,
		'L': 50,
		'C': 100,
		'D': 500,
		'M': 1000,
	}
	runes := []rune(s)
	prev := symMap[runes[len(runes)-1]]
	result := prev
	for i := len(runes) - 2; i >= 0; i-- {
		r := runes[i]
		v := symMap[r]
		if v < prev {
			result -= v
		} else {
			result += v
		}
		prev = v
	}
	return result
}

func main() {
	roman := romanToInt("MCMXCIV")
	fmt.Println(roman)
}
