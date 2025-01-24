package tools

type Stack[T any] struct {
	Data []T
}

func NewStack[T any]() *Stack[T] {
	return &Stack[T]{}
}

func (s *Stack[_]) Len() int {
	return len(s.Data)
}

func (s *Stack[_]) Cap() int {
	return cap(s.Data)
}

func (s *Stack[T]) Peek() T {
	return s.Data[len(s.Data)-1]
}

func (s *Stack[T]) Push(v T) {
	s.Data = append(s.Data, v)
}

func (s *Stack[T]) Pop() T {
	item := s.Data[len(s.Data)-1]
	s.Data = s.Data[:len(s.Data)-1]
	return item
}

func (s *Stack[T]) Empty() bool {
	return len(s.Data) == 0
}
