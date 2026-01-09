package main	

import (
	"fmt"
	"slices"
	"maps"
	// "reflect"
)

func isAnagram(s string, t string) bool{
	if len(s) != len(t) {
		return false
	}
	freq := make(map[rune]int)
	for _, r := range s {
		freq[r]++
	}
	for _, r := range t {
		freq[r]--
		if freq[r] < 0 {
			return false
		}
	}
	return true
}

func isAnagramOpt(s string, t string) bool {
	//  abcea -> 2,1,1,0,1 
	// Time O(n+m)
	// Memory: O(1) 		
	if len(s) != len(t) {
		return false
	}
	freq := [26]int{}
	for i := range len(s){
		freq[s[i]- 'a']++
	}
	for i := range len(t){
		freq[t[i] - 'a']--
		if freq[t[i] - 'a'] < 0 {
			return false
		}
	}
	return true
}


func isAnagramMap(s string, t string) bool{
	if len(s) != len(t) {
		return false
	}
	freqS := make(map[rune]int)
	freqT := make(map[rune]int)
	for _, r := range s {
		freqS[r] += 1
	}
	for _, r := range t {
		freqT[r] += 1
	}
	return maps.Equal(freqT, freqS)
}

func isAnagramSort(s string, t string) bool {
	// strings are immutable
	// thus convert to slice of rune
	// if only ASCII we can also convert to bytes
	// Expensive:
	// auxiliary space O(n + m)
	// runtime O(nlogn + nlogm) 	
	sr := []rune(s)
	slices.Sort(sr)
	tr := []rune(t)
	slices.Sort(tr)
	return slices.Equal(sr, tr)
}

type Test struct {
	s string
	t string
	exp bool
}



func main(){
	tests := []Test {
		{"a", "a", true},
		{"a", "aa", false},
		{"abc", "abc", true},
		{"abcd", "dcba", true},
		{"abcd", "abcf", false},
	}
	for _, test := range tests {
		act := isAnagramRepeat(test.s, test.t)
		fmt.Println(test.s, test.t, test.exp, act)
		if act != test.exp {
			panic(fmt.Sprintf("act != exp : %t != %t for s=%s, t=%s", act, test.exp, test.s, test.t))
		}
	}
	
}