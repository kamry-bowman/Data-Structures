class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


class Linked_List:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_tail(self, val):
        new_node = Node(val=val)

        if self.tail is not None:
            self.tail.next = new_node
            self.tail = new_node

        else:
            self.head = new_node
            self.tail = new_node

    def remove_head(self):

        if self.head is not None:
            old_head = self.head
            self.head = old_head.next

            if self.tail == old_head:
                self.tail = None

            return old_head.val

        else:
            return None


class Queue:
    def __init__(self):
        self.size = 0
        self.storage = Linked_List()

    def enqueue(self, item):
        self.size += 1
        return self.storage.add_to_tail(item)

    def dequeue(self):
        result = self.storage.remove_head()
        if result is None:
            self.size = 0
        else:
            self.size -= 1
        return result

    def len(self):
        return self.size


example = Queue()
example.enqueue(1)
example.enqueue(2)
print(example.dequeue())
print(example.dequeue())
print(example.dequeue())
