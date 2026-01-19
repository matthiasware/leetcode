package main

import (
	"fmt"
	"strconv"
	"strings"
)

/*
Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.

Idea:
- for each string encode the length of its characters / bytes
- in order to encode numbers, we need to follow each length hint with a delimiter, e.g. :

this solution could possibly be improved by using fixed 4 byte header
*/

type Solution struct{}

const Delimiter = ':'

func (s *Solution) Encode(strs []string) string {
	var sb strings.Builder
	for _, str := range strs {
		sb.WriteString(strconv.Itoa(len(str)))
		sb.WriteRune(Delimiter)
		sb.WriteString(str)
	}
	return sb.String()
}

func (s *Solution) Decode(encoded string) []string {
	result := []string{}
	for i := 0; i < len(encoded); {
		j := i
		for {
			if encoded[j] == Delimiter {
				break
			}
			j++
		}
		subLenBytes := encoded[i:j]
		strLenBytes, _ := strconv.Atoi(subLenBytes)

		begin := j + 1
		end := begin + strLenBytes
		str := encoded[begin:end]
		result = append(result, str)
		i = end
	}
	return result
}

func main() {
	// strs := []string{""}
	// strs := []string{"a"}
	// strs := []string{"aa"}
	strs := []string{"a", "bc", "d"}
	// strs := []string{"we","say",":","yes","!@#$%^&*()"}
	s := Solution{}
	fmt.Println(strs)
	enc := s.Encode(strs)
	fmt.Println(enc)
	dec := s.Decode(enc)
	fmt.Println(dec)
}
