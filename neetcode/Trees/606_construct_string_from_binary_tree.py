from typing import Optional

from neetcode.Trees import TreeNode, create_binary_tree_structure

def tree2str(root: Optional[TreeNode]) -> str:
    pass


if __name__ == "__main__":
    tr = create_binary_tree_structure([1, 2, 3, 4])
    print(tree2str(tr))
    