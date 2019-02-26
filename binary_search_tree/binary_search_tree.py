class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        target = 'left' if value <= self.value else 'right'
        target_val = getattr(self, target)
        if target_val is None:
            setattr(self, target, BinarySearchTree(value))
        else:
            target_val.insert(value)

    def contains(self, target):
        if self.value == target:
            return True
        if target < self.value:
            return self.left and self.left.contains(target)
        else:
            return self.right and self.right.contains(target)

    def get_max(self):
        if self.right is None:
            return self.value
        else:
            return self.right.get_max()
