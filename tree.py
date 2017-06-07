
INT_MIN = 4294967296
INT_MAX = -4294967296


class Node:

    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def insert(self, val):
        if val <= self.data:
            if self.left is None:
                self.left = Node(val)
            else:
                self.left.insert(val)
        else:
            if self.right is None:
                self.right = Node(val)
            else:
                self.right.insert(val)

    def contains(self, val):
        if val == self.data:
            return True
        elif val < self.data:
            if self.left is None:
                return False
            else:
                return self.left.contains(val)
        else:
            if self.right is None:
                return False
            else:
                return self.right.contains(val)

    def print_in_order(self):
        if self.left:
            self.left.print_in_order()
        print(self.data)
        if self.right:
            self.right.print_in_order()

    def print_in_pre_order(self):
        print(self.data)
        if self.left:
            self.left.print_in_pre_order()
        if self.right:
            self.right.print_in_order()

    # def print_in_post_order(self):
    #     if self.left:
    #         self.left.print_in_post_order()

def tree_max_height(tree):
    if tree is None:
        return 0
    else:
        left = tree_max_height(tree.left)
        right = tree_max_height(tree.left)
        return 1 + (left if left >= right else right)


def equal_trees(tree1, tree2):
    if tree1 is None and tree2 is None:
        return True
    elif type(tree1) != type(tree2):
        return False
    elif tree1.data != tree2.data:
        return False
    else:
        return equal_trees(tree1.left, tree2.left) and equal_trees(tree1.right, tree2.right)


def find_largest(tree):
    if tree is None:
        return 0
    else:
        left = find_largest(tree.left)
        right = find_largest(tree.right)
        maximum = left if left > right else right
        maximum = tree.data if tree.data > maximum else maximum
    return maximum


def mobile(tree1, tree2):
    if tree1 is None or tree2 is None:
        return tree1 == tree2
    elif tree1.data != tree2.data:
        return 0
    else:
        print("recursion")
        return (mobile(tree1.left, tree2.left) and mobile(tree1.right, tree2.right)) or \
               (mobile(tree1.left, tree2.right) and mobile(tree1.right, tree2.left))


def check_binary_search_tree_(node):
    return (isBSTUtil(node, INT_MIN, INT_MAX))


# Return true if the given tree is a BST and its values
# >= min and <= max
def isBSTUtil(node, mini, maxi):

    # An empty tree is BST
    if node is None:
        return True

    # False if this node violates min/max constraint
    if node.data < mini or node.data > maxi:
        return False

    # Otherwise check the subtrees recursively
    # tightening the min or max constraint
    return (isBSTUtil(node.left, mini, node.data - 1) and
            isBSTUtil(node.right, node.data + 1, maxi))


tree = Node(4)
tree.insert(2)
tree.insert(5)
tree.insert(7)
tree.insert(1)
tree.insert(6)
tree.insert(3)

test = Node(21)
test.insert(2)
test.insert(7)
test.insert(11)
test.insert(0)

print(test.data)
print(test.left.data)
print(test.left.left.data)
print(test.left.right.data)
print(test.left.right.right.data)


tree2 = Node(4)
tree2.insert(2)
tree2.insert(5)
tree2.insert(7)
tree2.insert(1)
tree2.insert(6)
tree2.insert(3)
tree2.insert(8)

mirror = Node(8)
mirror.insert(4)
mirror.insert(12)

mirror2 = Node(8)
mirror2.insert(12)
mirror2.insert(4)

mirror3 = Node(8)
mirror3.left = Node(4)
mirror3.right = Node(12)

mirror4 = Node(8)
mirror4.left = Node(12)
mirror4.left.left = Node(24)

print(check_binary_search_tree_(tree))
print(check_binary_search_tree_(tree2))
print(check_binary_search_tree_(mirror))
print(check_binary_search_tree_(mirror2))
print(check_binary_search_tree_(mirror3))
print(check_binary_search_tree_(mirror4))

# print(mobile(mirror3, mirror4))

# print(equal_trees(tree, tree2))

# print(find_largest(tree))

# print(tree.contains(15))
# print(tree.data)
#
# tree.print_in_order()
# tree.print_in_pre_order()

# print(tree_max_height(tree))