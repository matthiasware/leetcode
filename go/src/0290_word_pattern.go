package main

import (
	"fmt"
	"strings"
)

func wordPattern(pattern string, s string) bool {
	ptos := make(map[byte]string)
	stop := make(map[string]byte)
	words := strings.Fields(s)
	if len(words) != len(pattern) {
		return false
	}
	for i := range len(pattern) {
		word := words[i]
		p := pattern[i]

		if valString, exists := ptos[p]; exists && valString != word {
			return false
		}
		if valPat, exists := stop[word]; exists && valPat != p {
			return false
		}
		ptos[p] = word
		stop[word] = p
	}
	return true
}

func main() {
	type Test struct {
		pat string
		str string
		exp bool
	}
	tests := []Test{
		//{"a", "dog", true},
		//{"ab", "cat dog", true},
		//{"abb", "cat dog dog", true},
		//{"abb", "cat dog cat", false},
		//{"abba", "dog cat cat dog", true},
		//{"abba", "dog cat cat duck", false},
		{"abba", "dog dog dog dog", false},
	}
	for _, test := range tests {
		act := wordPattern(test.pat, test.str)
		if act != test.exp {
			fmt.Println(test.str, test.pat, test.exp, act)
		}
	}
}
