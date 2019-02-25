class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        target = 'left' if value <= self.value else 'right'
        target_val = getattr(self, target)
        if target_val is None:
            setattr(self, target, value)
        else:
            target_val.insert(value)

    def contains(self, target):
        pass

    def get_max(self):
        pass
