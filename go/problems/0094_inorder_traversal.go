package main

import (
	"fmt"
	"leetcode/tools"
)

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func inorderTraversal(root *TreeNode) []int {
	result := []int{}
	inorderTraversalRec(root, &result)
	return result
}

func inorderTraversalRec(node *TreeNode, result *[]int) {
	if node == nil {
		return
	}
	inorderTraversalRec(node.Left, result)
	*result = append(*result, node.Val)
	inorderTraversalRec(node.Right, result)
}

func inorderTraversalIterative(root *TreeNode) []int {
	result := []int{}
	stack := tools.NewStack[*TreeNode]()
	node := root

	for node != nil || !stack.Empty() {
		for node != nil {
			stack.Push(node)
			node = node.Left
		}
		node = stack.Pop()
		result = append(result, node.Val)
		node = node.Right
	}

	return result
}

func main() {
	root := TreeNode{1,
		&TreeNode{2, nil, nil},
		&TreeNode{3, nil, nil},
	}
	res := inorderTraversalIterative(&root)
	fmt.Println(res)
}
