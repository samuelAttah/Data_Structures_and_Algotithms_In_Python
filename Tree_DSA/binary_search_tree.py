class BinarySearchTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, value):
        if self.data == value:
            return

        if value < self.data:
            if self.left:
                self.left.add_child(value)
            else:
                self.left = BinarySearchTree(value)

        if value > self.data:
            if self.right:
                self.right.add_child(value)
            else:
                self.right = BinarySearchTree(value)

    def in_order_traversal(self):
        elements = []

        if self.left:
            elements += self.left.in_order_traversal()

        elements.append(self.data)

        if self.right:
            elements += self.right.in_order_traversal()

        return elements

    def pre_order_traversal(self):
        elements = []

        elements.append(self.data)

        if self.left:
            elements += self.left.pre_order_traversal()

        if self.right:
            elements += self.right.pre_order_traversal()

        return elements

    def post_order_traversal(self):
        elements = []

        if self.left:
            elements += self.left.post_order_traversal()

        if self.right:
            elements += self.right.post_order_traversal()

        elements.append(self.data)

        return elements

    def find_min(self):
        if self.left == None:
            return self.data

        if self.left:
            return self.left.find_min()

    def find_max(self):
        if self.right == None:
            return self.data

        if self.right:
            return self.right.find_max()

    def calculate_sum(self):
        total = 0

        if self.data:
            total += self.data

        if self.right:
            total += self.right.calculate_sum()

        if self.left:
            total += self.left.calculate_sum()

        return total

    def delete(self, value):
        if value < self.data:
            # check the left subtree
            if self.left:
                self.left = self.left.delete(value)
        elif value > self.data:
            # check the right subtree
            if self.right:
                self.right = self.right.delete(value)

        else:
            if self.left is None and self.right is None:
                return None
            if self.left is None:
                return self.right
            if self.right is None:
                return self.right

            min_val = self.right.find_min()
            self.data = min_val
            self.right = self.right.delete(min_val)

        return self


def build_tree(elements):
    root_node = BinarySearchTree(elements[0])

    for i in range(1, len(elements)):
        root_node.add_child(elements[i])

    return root_node


tree_list = [19, 78, 3, 15, 27, 4, 20, 18, 22, 13, 95, 30]

numbers_tree = build_tree(tree_list)
print(numbers_tree.in_order_traversal())
