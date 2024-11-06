package main

import "fmt"

func maxVowels(s string, k int) int {
	var temp int
	vowels := map[string]bool{"a": true, "e": true, "i": true, "o": true, "u": true}
	res := 0
	for i := 0; i < len(s)-k+1; i++ {
		temp = 0
		for j := 0; j < k; j++ {
			if _, exist := vowels[string(s[i+j])]; exist {
				temp += 1
			}
		}
		res = max(res, temp)
	}
	return res
}

func main() {
	s := "longstring"
	k := 3
	fmt.Printf("res = %d\n", maxVowels(s, k))
}
