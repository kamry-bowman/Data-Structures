from collections import deque, namedtuple


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
  after this node. Note that this node could already
  have a next node it is point to."""

    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
  before this node. Note that this node could already
  have a previous node it is point to."""

    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
  accordingly, effectively deleting this ListNode."""

    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node

    def add_to_head(self, value):

        if self.head:
            old_head = self.head
            old_head.insert_before(value)

            self.head = self.head.prev
        else:
            self.head = ListNode(value)
            self.tail = self.head

    def remove_from_head(self):
        if self.head:
            # handle list of length 1
            if self.head == self.tail:
                head = self.head
                self.head = None
                self.tail = None
                return head.value
            # else handle length > 1 list
            else:
                old_head = self.head
                self.head = old_head.next
                old_head.delete()
                return old_head.value
        else:
            return None

    def add_to_tail(self, value):
        if self.tail:
            self.tail.insert_after(value)
            self.tail = self.tail.next

        else:
            new_node = ListNode(value)
            self.head = new_node
            self.tail = new_node

    def remove_from_tail(self):
        # ensure tail exists
        if self.tail:

            old_tail = self.tail
            # handle length 1 list
            if self.tail == self.head:
                self.tail = None
                self.head = None
                return old_tail.value
            # else handle length > 1 list
            else:
                self.tail = old_tail.prev
                old_tail.delete()
            return old_tail.value
        else:
            return None

    def move_to_front(self, node):
        if isinstance(node, ListNode) and node != self.head:
            self.delete(node)
            self.add_to_head(node.value)

    def move_to_end(self, node):
        if isinstance(node, ListNode) and node != self.tail:
            self.delete(node)
            self.add_to_tail(node.value)

    def delete(self, node):
        if isinstance(node, ListNode):
            if self.tail is node:
                self.remove_from_tail()
            elif self.head is node:
                self.remove_from_head()
            else:
                return node.delete()
        else:
            return None

    def get_max(self):
        max = self.head
        current = self.head
        while current:
            if max.value < current.value:
                max = current
            current = current.next
        return max.value if max else None


KeyVal = namedtuple('KeyVal', ['key', 'value'])


class LRUCache:
    def __init__(self, limit=10):
        self.limit = limit
        self.length = 0
        self.links = {}
        self.history = DoublyLinkedList()

    """
  Retrieves the value associated with the given key. Also
  needs to move the key-value pair to the top of the order
  such that the pair is considered most-recently used.
  Returns the value associated with the key or None if the
  key-value pair doesn't exist in the cache.
  """

    def get(self, key):
        link = self.links.get(key)
        if link is not None:
            self.history.move_to_front(link)
            return link.value.value
        else:
            return None

    """
  Adds the given key-value pair to the cache. The newly-
  added pair should be considered the most-recently used
  entry in the cache. If the cache is already at max capacity
  before this entry is added, then the oldest entry in the
  cache needs to be removed to make room. Additionally, in the
  case that the key already exists in the cache, we simply
  want to overwrite the old value associated with the key with
  the newly-specified value.
  """

    def set(self, key, value):
        link = self.links.get(key)
        if link is not None:
            self.history.move_to_front(link)
            link.value = KeyVal(key=key, value=value)

        else:
            self.history.add_to_head(KeyVal(key=key, value=value))
            self.links[key] = self.history.head

            if self.length < self.limit:
                self.length += 1

            else:
                # delete oldest link history entries, and use
                # key to delete same from links
                outgoing = self.history.remove_from_tail()
                del self.links[outgoing.key]
