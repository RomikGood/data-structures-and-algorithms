from .bst import BinaryTree

def find_common_values():
    tree_a = BinaryTree()
    tree_b = BinaryTree()

    output = []
    hash_table = {}

    def collect_values(node):
        if node.right:
            collect_values(node.right)
        if node.left:
            collect_values(node.left)
        hash_table[node.value] = 1
    
    def compare_values(node):
        if node.right:
            collect_values(node.right)
        if node.left:
            collect_values(node.left)
        if node.value in hash_table:
            output.append(node.value)

    collect_values(tree_a.root)
    compare_values(tree_b.root)

    return output