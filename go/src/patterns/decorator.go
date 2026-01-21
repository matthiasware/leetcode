package main

import (
	"fmt"
	"time"
)

type ExecuteFunc func(string)

func SimpleExecute(msg string){
	fmt.Println(msg)
}

func WithTimer(fn ExecuteFunc) ExecuteFunc {
	return func(s string) {
		start := time.Now()
		fn(s)
		fmt.Printf("Took %v\n", time.Since(start))
	}
}

func main(){
	SimpleExecute("Bla")
	decorated := WithTimer(SimpleExecute)
	decorated("bla")
	
}