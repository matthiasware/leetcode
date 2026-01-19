/*
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.


Constraints:

1 <= s.length <= 2 * 105
s consists only of printable ASCII characters.
*/

package main

import (
	"fmt"
	"unicode"
)

func isAlphaNum(c rune) bool {
	return unicode.IsLetter(c) || unicode.IsDigit(c)
}

func isPalindrome(s string) bool {
	p1, p2 := 0, len(s)-1
	for p1 < p2 {
		for p1 < p2 && !isAlphaNum(rune(s[p1])) {
			p1++
		}
		for p2 > p1 && !isAlphaNum(rune(s[p2])) {
			p2--
		}
		if unicode.ToLower(rune(s[p1])) != unicode.ToLower(rune(s[p2])) {
			return false
		}
		p1++
		p2--
	}
	return true
}

func main() {
	fmt.Println(isPalindrome("a b a"))
	// fmt.Println(isAlphaNum('!'))
}
