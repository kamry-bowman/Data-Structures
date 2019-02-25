import unittest


class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next


class Stack:
    def __init__(self):
        self.head = None

    def push(self, value):
        if self.head:
            new_node = Node(value, self.head)
            self.head = new_node
        else:
            self.head = Node(value)

    def pop(self):
        if self.head:
            old_head = self.head
            self.head = old_head.next
            return old_head.value
        else:
            return None

    def peek(self):
        return self.head.value if self.head else None


class TestStack (unittest.TestCase):

    def test_proper_stack_behavior(self):
        example = Stack()
        self.assertEqual(example.pop(), None)
        example.push(1)
        example.push(2)
        self.assertEqual(example.pop(), 2)
        example.push(3)
        example.push(4)
        self.assertEqual(example.pop(), 4)
        self.assertEqual(example.pop(), 3)
        self.assertEqual(example.pop(), 1)
        self.assertEqual(example.pop(), None)


if __name__ == '__main__':
    unittest.main()
