"""
https://leetcode.cn/problems/er-cha-sou-suo-shu-de-zui-jin-gong-gong-zu-xian-lcof/description/?envType=study-plan-v2&envId=coding-interviews

https://leetcode.cn/problems/lowest-common-ancestor-of-a-binary-search-tree/
"""

from data_structure.binary_tree import TreeNode


class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        while root:
            # 如果p,q在root的同侧，则root转到p,q所在的一侧
            if (root.val < p.val) and (root.val < q.val):
                root = root.right
            elif (root.val > p.val) and (root.val > q.val):
                root = root.left
            else: # 如果p,q分别在root的两侧，root就是p,q的最近公共祖先
                return root
        
        return None


def main():
    values = [6, 2, 8, 0, 4, 7, 9, None, None, 3, 5]
    root, nodes = TreeNode.from_list(values, with_nodes=True)
    p = nodes[1]
    q = nodes[2]
    TreeNode.print_tree(root)

    sln = Solution()
    res = sln.lowestCommonAncestor(root, p, q)
    print(res.val)
    

if __name__ == "__main__":
    main()


