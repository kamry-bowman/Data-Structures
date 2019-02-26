from collections import deque


class LRUCache:
    def __init__(self, limit=10):
        self.limit = limit
        self.length = 0
        self.values = {}
        self.history = deque()

    """
  Retrieves the value associated with the given key. Also
  needs to move the key-value pair to the top of the order
  such that the pair is considered most-recently used.
  Returns the value associated with the key or None if the
  key-value pair doesn't exist in the cache. 
  """

    def get(self, key):
        value = self.values.get(key)
        if value is not None:
            history = self.history
            history.remove(key)
            history.append(key)
        return value

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
        old_value = self.get(key)
        self.values[key] = value
        if old_value is None:
            self.history.append(key)
            if len(self.values) > self.limit:
                outgoing = self.history.popleft()
                del self.values[outgoing]
            else:
                self.length += 1
        else:
            history = self.history
            history.remove(key)
            history.append(key)
