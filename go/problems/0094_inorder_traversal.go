package main

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

func main() {
	root := TreeNode{1,
		&TreeNode{2, nil, nil},
		&TreeNode{3, nil, nil},
	}
	inorderTraversal(&root)
}
