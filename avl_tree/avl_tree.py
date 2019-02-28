"""
Node class to keep track of
the data internal to individual nodes
"""


class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


"""
A tree class to keep track of things like the
balance factor and the rebalancing logic
"""


class AVLTree:
    def __init__(self, node=None):
        self.node = node
        # init height to -1 because of 0-indexing
        self.height = -1
        self.balance = 0

        """
  Display the whole tree. Uses recursive def.
  """

    def display(self, level=0, pref=''):
        self.update_height()  # Update height before balancing
        self.update_balance()

        if self.node != None:
            print('-' * level * 2, pref, self.node.key, "[" + str(self.height) + ":" + str(
                self.balance) + "]", 'L' if self.is_leaf() else ' ')
            if self.node.left != None:
                self.node.left.display(level + 1, '<')
            if self.node.right != None:
                self.node.right.display(level + 1, '>')

        """
  Computes the maximum number of levels there are
  in the tree
  """

    def update_height(self):
        if self.node is None:
            self.height = -1
        else:
            left_height = -1
            right_height = -1
            if self.node.left is not None:
                left_height = self.node.left.update_height()
            if self.node.right is not None:
                right_height = self.node.right.update_height()
            self.height = 1 + max(left_height, right_height)

        return self.height

        """
  Updates the balance factor on the AVLTree class
  """

    def update_balance(self):
        if self.node:
            if self.node.left:
                left_height = self.node.left.update_height()
            else:
                left_height = -1

            if self.node.right:
                right_height = self.node.right.update_height()
            else:
                right_height = -1

            self.balance = left_height - right_height
        return self.balance

        """
  Perform a left rotation, making the right child of this
  node the parent and making the old parent the left child
  of the new parent. 
  """

    def _left_rotate(self):
        if self.node.left:
            old_parent = self.node
            old_right_child = self.node.right
            old_left_child_of_right_child = getattr(
                old_right_child.node.left, 'node', None)

            self.node = old_right_child.node

            # catch error in case node.left is still None, not yet ATLTree
            try:
                self.node.left.node = old_parent
            except AttributeError:
                self.node.left = AVLTree(old_parent)

            # Need to make a new node with key, otherwise reusing the old node will
            # have old left and right pointers which are no longer accurate
            self.node.left.node.right.node = Node(
                old_left_child_of_right_child.key) if old_left_child_of_right_child is not None else None
        else:
            old_parent = self.node
            self.node = self.node.right.node
            self.insert(old_parent.key)

        """
  Perform a right rotation, making the left child of this
  node the parent and making the old parent the right child
  of the new parent. 
  """

    def _right_rotate(self):
        if self.node.right:
            old_parent = self.node
            old_left_child = self.node.left
            old_right_child_of_left_child = getattr(
                old_left_child.node.right, 'node', None)

            self.node = old_left_child.node

            # catch error in case node.right is still None, not yet ATLTree
            try:
                self.node.right.node = old_parent
            except AttributeError:
                self.node.right = AVLTree(old_parent)

            # Need to make a new node with key, otherwise reusing the old node will
            # have old left and right pointers which are no longer accurate
            self.node.right.node.left.node = Node(
                old_right_child_of_left_child.key) if old_right_child_of_left_child is not None else None

        else:
            old_parent = self.node
            self.node = self.node.left.node
            self.insert(old_parent.key)

        """
  Sets in motion the rebalancing logic to ensure the
  tree is balanced such that the balance factor is
  1 or -1
  """

    def rebalance(self):
        balance = self.update_balance()

        if balance > 1:
            # check if double rotation is needed
            if self.node.left and self.node.left.update_balance() < 0:
                self.node.left._left_rotate()
            self._right_rotate()

        elif balance < -1:
            # check if double rotation is needed
            if self.node.right and self.node.right.update_balance() > 0:
                self.node.right._right_rotate()
            self._left_rotate()

        """
  Uses the same insertion logic as a binary search tree
  after the value is inserted, we need to check to see
  if we need to rebalance
  """

    def insert(self, key):
        if not self.node:
            self.node = Node(key)
        else:
            if key <= self.node.key:
                if self.node.left:
                    self.node.left.insert(key)
                else:
                    self.node.left = AVLTree(Node(key))
            else:
                if self.node.right:
                    self.node.right.insert(key)
                else:
                    self.node.right = AVLTree(Node(key))
            self.rebalance()

    def is_leaf(self):
        return self.node.left is None and self.node.right is None


example = AVLTree()
example.insert(3)
example.insert(4)
example.insert(5)
example.insert(7)
example.insert(8)
example.insert(9)
example.insert(-5)
example.insert(-8)
example.insert(1)
example.insert(-12)
example.display()
