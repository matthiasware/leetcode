package main

import "fmt"

type CharCounts [26]int
type AnagramGroup []string

func groupAnagrams(strs []string) [][]string {
	// Idea
	// create frequency reqpresentation of string via char counts
	// use these as keys to a map to slices of group anagrams
	// Time: O(n * k) with n strings of max length k
	// Memory: O(n)
	groupMap := make(map[CharCounts]AnagramGroup)
	for _, str := range strs {
		var key CharCounts
		for i := 0; i < len(str); i++ {
			key[str[i]-'a']++
		}
		// really cool featue: append to nil works
		groupMap[key] = append(groupMap[key], str)
	}

	anagrams := make([][]string, 0, len(groupMap))
	for _, group := range groupMap {
		anagrams = append(anagrams, group)
	}
	return anagrams
}

func main() {
	// strs := []string{"eat","tea","tan","ate","nat","bat"}
	// exp := [][]string {
	// 	{"bat"},
	// 	{"nat","tan"},
	// 	{"ate","eat","tea"},
	// }
	strs := []string{"abc", "bac", "def"}
	// exp := [][]string {
	// 	{"def"},
	// 	{"abc","bac"},
	// }
	fmt.Println(groupAnagrams(strs))

}
