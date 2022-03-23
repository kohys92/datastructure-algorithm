# Given the root node of a binary search tree and two integers low and high, return the sum of values of all nodes
# with a value in the inclusive range [low, high].
#
#
# Example 1:
#
#
# Input: root = [10,5,15,3,7,null,18], low = 7, high = 15
# Output: 32
# Explanation: Nodes 7, 10, and 15 are in the range [7, 15]. 7 + 10 + 15 = 32.
# Example 2:
#
#
# Input: root = [10,5,15,3,7,13,18,1,null,6], low = 6, high = 10
# Output: 23
# Explanation: Nodes 6, 7, and 10 are in the range [6, 10]. 6 + 7 + 10 = 23.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Iterative Implementation
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        sum = 0
        stack = [root]

        while stack:
            node = stack.pop()

            if node:
                if low <= node.val <= high:
                    sum += node.val
                if low < node.val:
                    stack.append(node.left)
                if node.val < high:
                    stack.append(node.right)
        return sum


# Recursive Implementation
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:

        # DFS 메서드를 만든다
        def dfs(node):
            # 처음 최상단의 노드를 확인한다
            if node:
                # 최상단 노드값이 low 보다 크거나 high 보다 낮으면 sum에 더해준다
                if low <= node.val <= high:
                    self.sum += node.val
                # 최상단의 노드값이 low 보다 크다면 왼쪽으로 탐색한다
                if low < node.val:
                    dfs(node.left)
                # 최상단의 노드값이 high 보다 작다면 오른쪽으로 탐색한다
                if node.val < high:
                    dfs(node.right)

                # 처음 sum 은 0으로 정해준다

        self.sum = 0
        # DFS 재귀 함수를 호출한다
        dfs(root)
        return self.sum