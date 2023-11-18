from typing import Optional
from neetcode.Trees import create_binary_tree_structure, TreeNode


def diameter_of_binary_tree(root: Optional[TreeNode]) -> int:
    result = 0

    def dfs(r) -> int:
        nonlocal result
        if not r:
            return -1
        left = dfs(r.left)
        right = dfs(r.right)
        result = max(result, 2 + left + right)
        return 1 + max(left, right)

    dfs(root)
    return result


if __name__ == '__main__':
    vals = [1,
            2, 3,
            None, 4, 5, 6,
            None, None, None, None, None, 20, None, None]
    t = create_binary_tree_structure(vals)
    print(diameter_of_binary_tree(t))
