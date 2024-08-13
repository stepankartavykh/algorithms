from neetcode import TreeNode, create_binary_tree_structure, print_binary_tree_structure


class Codec:

    def serialize(self, root: TreeNode) -> str:
        # TODO what are other ways to encode tree structure in string?
        if not root:
            return ''
        if not root.left and not root.right:
            return str(root.val)
        if not root.left:
            return str(root.val) + '[][' + self.serialize(root.right) + ']'
        if not root.right:
            return str(root.val) + '[' + self.serialize(root.left) + ']'
        return str(root.val) + f'[{self.serialize(root.left)}][{self.serialize(root.right)}]'

    def deserialize(self, data: str) -> TreeNode:
        # TODO - recursive? Find element and brackets '[' and ']' and then create left and right nodes?
        if data == '':
            return TreeNode()
        elements = data.split('[')
        stack = []
        result_tree = TreeNode(val=int(elements[0]))
        current_node = result_tree
        for element in elements[1:]:
            if ']' not in element:
                pass

        return result_tree


if __name__ == '__main__':
    tree = create_binary_tree_structure([13, 2345, 31, None, 12, 4, 5])
    codec = Codec()
    print(codec.serialize(tree))
    same_tree = codec.deserialize(codec.serialize(tree))
    print_binary_tree_structure(same_tree)
