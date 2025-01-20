// https://leetcode.com/problems/count-pairs-of-similar-strings/
package main

import (
	"fmt"
)

type RuneOccurrence [26]rune

func similarPairs(words []string) int {
	// Idea: Represent string by 1-hot vector of rune occurences
	//       Track frequencies of similar strings on map
	//		 Calculate the number of similar strings from map
	// Complexity: let b be the number of strings and m be the number of chars per string
	// 		Time: O(n*m)
	// 		Memo: O(n) ~ O(1)
	occurrence := make(map[RuneOccurrence]int)
	for _, word := range words {
		runeOccurrence := RuneOccurrence{}
		for _, c := range word {
			runeOccurrence[c-97] = 1
		}
		val, _ := occurrence[runeOccurrence]
		occurrence[runeOccurrence] = val + 1
	}
	nPairs := 0
	for _, n := range occurrence {
		if n >= 2 {
			nPairs += n * (n - 1) / 2
		}
	}
	return nPairs
}

type Test struct {
	strings  []string
	expected int
}

func main() {
	tests := []Test{
		Test{[]string{"a"}, 0},
		Test{[]string{"a", "aa"}, 1},
		Test{[]string{"aba", "aabb", "abcd", "bac", "aabc"}, 2},
		Test{[]string{"aabb", "ab", "ba"}, 3},
		Test{[]string{"nba", "cba", "dba"}, 0},
	}
	for _, test := range tests {
		act := similarPairs(test.strings)
		exp := test.expected
		fmt.Println(act, exp)
	}
}
