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
            return str(root.val) + '[' + self.serialize(root.left) + '][]'
        return str(root.val) + f'[{self.serialize(root.left)}][{self.serialize(root.right)}]'

    def deserialize(self, data: str) -> TreeNode | None:
        # TODO - recursive? Find element and brackets '[' and ']' and then create left and right nodes?
        if data == '':
            return None
        first_opening_bracket = data.find('[')
        if first_opening_bracket == -1:
            return TreeNode(int(data))
        head_value = int(data[:first_opening_bracket])
        diff = 0
        flag = False
        count_pairs = 0
        end_index = None
        for index in range(first_opening_bracket + 1, len(data)):
            if data[index] == ']' and index == first_opening_bracket + 1:
                end_index = index
                break
            elif data[index] == '[':
                flag = True
                diff += 1
            elif data[index] == ']' and count_pairs == 0:
                end_index = index
                break
            elif data[index] == ']':
                diff -= 1
            if flag is True and diff == 0:
                count_pairs += 1
            if count_pairs == 2:
                end_index = index
                break
        result_tree = TreeNode(val=head_value)
        left_node = self.deserialize(data[first_opening_bracket + 1:end_index + 1])
        right_node = self.deserialize(data[end_index + 2:len(data) - 1])
        result_tree.left = left_node
        result_tree.right = right_node
        return result_tree


if __name__ == '__main__':
    # tree = create_binary_tree_structure([13, 2345, 31, None, 12, 4, 5])
    # tree = create_binary_tree_structure([13, 2345, 31, 1111, 12, 4])
    tree = create_binary_tree_structure([1, 2, 3, 4, 5])
    codec = Codec()
    print(codec.serialize(tree))
    same_tree = codec.deserialize(codec.serialize(tree))
    print_binary_tree_structure(same_tree)
