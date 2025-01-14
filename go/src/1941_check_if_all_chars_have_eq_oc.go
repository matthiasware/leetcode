package main

import "fmt"

func areOccurrencesEqual(s string) bool {
	runeCount := make(map[rune]int)
	for _, r := range s {
		runeCount[r]++
	}
	var firstRune rune
	for _, c := range s {
		firstRune = c
		break
	}
	firstRuneCount := runeCount[firstRune]
	for _, count := range runeCount {
		if count != firstRuneCount {
			return false
		}
	}
	return true
}

func main() {
	type test struct {
		s        string
		expected bool
	}
	tests := []test{
		{"a", true},
		{"ab", true},
		{"abc", true},
		{"aba", false},
		{"abacbc", true},
		{"aaabb", false},
	}
	for _, t := range tests {
		act := areOccurrencesEqual(t.s)
		fmt.Println(t.s, t.expected, act)
	}

}
