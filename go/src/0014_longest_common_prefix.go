package main

import "fmt"

func maxCommonPrefixLength(s1 string, s2 string) int {
	mcpl := 0
	for i := 0; i < len(s1); i++ {
		if i >= len(s2) {
			break
		}
		if s1[i] != s2[i] {
			break
		}
		mcpl += 1
	}
	return mcpl
}

func longestCommonPrefix_complex(strs []string) string {
	template := strs[0]
	minPrefix := len(template)

	for _, str := range strs[1:] {
		minPrefix = min(minPrefix, maxCommonPrefixLength(template, str))
	}

	return template[0:minPrefix]
}

func longestCommonPrefix(strs []string) string {
	p := strs[0]
	for _, s := range strs[1:] {
		i := 0
		for ; i < len(s) && i < len(p) && p[i] == s[i]; i++ {
		}
		p = p[:i]
	}
	return p
}

func main() {
	fmt.Println(longestCommonPrefix([]string{"flower", "flow", "floght"}))
	fmt.Println(longestCommonPrefix([]string{"abc", "b"}))
}
