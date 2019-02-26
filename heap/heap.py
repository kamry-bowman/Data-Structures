class Heap:
    def __init__(self):
        self.storage = []

    def insert(self, value):
        self.storage.append(value)
        self._bubble_up(len(self.storage) - 1)

    def delete(self):
        end = self.storage.pop()
        if self.storage:
            deleted = self.storage[0]
            self.storage[0] = end
            self._sift_down(0)
            return deleted
        else:
            return end

    def get_max(self):
        if not self.storage:
            return None
        else:
            return self.storage[0]

    def get_size(self):
        return len(self.storage)

    def _bubble_up(self, index):
        if index > 0:
            storage = self.storage
            parent_index = (index - 1) // 2

            if storage[index] > storage[parent_index]:
                storage[index], storage[parent_index] = storage[parent_index], storage[index]
                if parent_index > 0:
                    self._bubble_up(parent_index)

    def _sift_down(self, index):
        storage = self.storage
        l_child_i = index * 2 + 1
        value = storage[index]
        try:
            l_child_val = storage[l_child_i]
        except IndexError:
            l_child_val = None
        r_child_i = index * 2 + 2
        try:
            r_child_val = storage[r_child_i]
        except IndexError:
            r_child_val = None

        # figure out if left or right is greater
        if not r_child_val or l_child_val >= r_child_val:
            greatest_child_i, greatest_child_val = l_child_i, l_child_val
        else:
            greatest_child_i, greatest_child_val = r_child_i, r_child_val

        # figure out if value is left than lower than the greater of its children
        if greatest_child_val is not None and value <= greatest_child_val:
            storage[index], storage[greatest_child_i] = storage[greatest_child_i], storage[index]

            # continue sift if child isn't terminal
            if greatest_child_i < len(storage) - 1:
                self._sift_down(greatest_child_i)


heap = Heap()
heap.insert(6)
heap.insert(8)
heap.insert(10)
heap.insert(9)
heap.insert(1)
heap.insert(9)
heap.insert(9)
heap.insert(5)
print(heap.get_size())
print(heap.get_max())
heap.delete()
print(heap.get_size())
print(heap.get_max())
heap.delete()
print(heap.get_size())
print(heap.get_max())
