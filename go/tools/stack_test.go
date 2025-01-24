package tools

import (
	"testing"
)

func TestPushInt(t *testing.T) {
	stack := NewStack[int]()
	item := 1251
	stack.Push(item)
	if len(stack.Data) != 1 {
		t.Errorf("stack.Data does not contain 1 element")
	}
	if stack.Data[0] != item {
		t.Errorf("stack.Data does not contain %v element", item)
	}
}

func TestPushString(t *testing.T) {
	stack := NewStack[string]()
	i1 := "A"
	stack.Push(i1)
	i2 := "B"
	stack.Push(i2)

	if len(stack.Data) != 2 {
		t.Errorf("stack.Data does not contain 2 elements")
	}
	if stack.Data[0] != i1 {
		t.Errorf("stack.Data does not contain %v element", i1)
	}
	if stack.Data[1] != i2 {
		t.Errorf("stack.Data does not contain %v element", i2)
	}
}

func TestLen(t *testing.T) {
	stack := NewStack[int]()
	for range 10 {
		stack.Push(1)
	}
	if stack.Len() != 10 {
		t.Errorf("stack.Len does not contain 10 elements")
	}
	stack = NewStack[int]()
	stack.Push(1)
	if stack.Len() != 1 {
		t.Errorf("stack.Len does not contain 1 element")
	}
	stack = NewStack[int]()
	if stack.Len() != 0 {
		t.Errorf("stack.Len does not contain 0 element")
	}
}

func TestPeek(t *testing.T) {
	stack := NewStack[int]()
	exp := 13
	stack.Push(exp)
	act := stack.Peek()
	if act != exp {
		t.Errorf("stack.Peek does not contain %v element", exp)
	}
	stack.Push(123)
	stack.Push(456)
	stack.Push(exp)
	act = stack.Peek()
	if act != exp {
		t.Errorf("stack.Peek does not contain %v element", exp)
	}

}

func TestPop(t *testing.T) {
	stack := NewStack[int]()
	stack.Push(1)
	item := stack.Pop()
	if item != 1 {
		t.Errorf("stack.Pop does not contain 1 element")
	}
	if stack.Len() != 0 {
		t.Errorf("stack.Pop does not contain 0 elements")
	}
	stack.Push(1)
	stack.Push(2)
	stack.Push(3)
	item = stack.Pop()
	if item != 3 {
		t.Errorf("stack.Pop does not contain 3 elements")
	}
	if stack.Len() != 2 {
		t.Errorf("stack.Pop does not contain 2 elements")
	}

}
