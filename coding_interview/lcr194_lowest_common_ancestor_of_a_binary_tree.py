"""
https://leetcode.cn/problems/er-cha-shu-de-zui-jin-gong-gong-zu-xian-lcof/description/?envType=study-plan-v2&envId=coding-interviews

https://leetcode.cn/problems/lowest-common-ancestor-of-a-binary-tree/

"""


from data_structure.binary_tree import TreeNode

class Solution:

    def __init__(self):
        self.res = None

    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        self.lowestCommonAncestor_2(root, p, q)

        return self.res
    
    def lowestCommonAncestor_2(self, root, p, q):
        if not root:
            return False
        
        left = self.lowestCommonAncestor_2(root.left, p, q)
        right = self.lowestCommonAncestor_2(root.right, p, q)

        if (left and right) or ((root.val == p.val or root.val == q.val) and (left or right)):
            self.res = root
        
        return left or right or (root.val == p.val or root.val == q.val)

    def lowestCommonAncestor_1(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root:
            return None
        if (root == p) or (root == q):
            return root
        
        left = self.lowestCommonAncestor_1(root.left, p, q)
        right = self.lowestCommonAncestor_1(root.right, p, q)

        if left and right:
            return root
        
        return left or right

def main():
    values = [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]
    root, nodes = TreeNode.from_list(values, with_nodes=True)
    p = nodes[1]
    q = nodes[-1]

    TreeNode.print_tree(root)

    sln = Solution()
    res = sln.lowestCommonAncestor(root, p, q)
    print(res.val)


if __name__ == "__main__":
    main()