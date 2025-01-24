package main

import "fmt"

func strStr(heystack string, needle string) int {
	/*
			Time: O(m*n)
			Memo: O(1)
		Since we only use roman lower letters, we could also simplify it.
	*/
	for i, _ := range heystack {
		if i+len(needle) > len(heystack) {
			break
		}
		if heystack[i:i+len(needle)] == needle {
			return i
		}
	}
	return -1
}

func main() {
	heystack := "höllo"
	needle := "lo"
	fmt.Println(strStr(heystack, needle))
	for i, v := range heystack {
		fmt.Println(i, v, heystack[i:len(heystack)], len(heystack))

	}
}
