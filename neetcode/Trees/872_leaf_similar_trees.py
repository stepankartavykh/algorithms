from neetcode import TreeNode, create_binary_tree_structure


class Solution:
    @staticmethod
    def get_lowest_values(root: TreeNode | None) -> list[int]:
        if not root:
            return []
        values = []

        def f(node):
            if not node:
                return
            if node.left is None and node.right is None:
                values.append(node.val)
            f(node.left)
            f(node.right)

        f(root)
        return values

    def leaf_similar(self, root1: TreeNode | None, root2: TreeNode | None) -> bool:
        vals1 = self.get_lowest_values(root1)
        vals2 = self.get_lowest_values(root2)

        if len(vals1) != len(vals2):
            return False
        for f, s in zip(vals1, vals2):
            if f != s:
                return False
        return True


if __name__ == '__main__':
    first_values = [1, 2, 3]
    second_values = [1, 3, 2]
    print(Solution().leaf_similar(create_binary_tree_structure(first_values),
                                  create_binary_tree_structure(second_values)))
