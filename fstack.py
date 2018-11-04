from collections import deque
from stack import Stack


class FancyStack(Stack):
    """Extends the basic Stack providing additional operations."""

    def __init__(self):
        super().__init__()

    def duplicate(self):
        """The top item is popped, and then pushed again (twice),
        so that an additional copy of the former top item is now on top,
        with the original below it.
        """
        top_item = super().pop()
        super().push(top_item)
        super().push(top_item)

    def peek(self):
        """The topmost item is inspected (or returned),
        but the stack pointer and stack size does not change
        (meaning the item remains on the stack).
        """
        return self.items[len(self.items)-1]

    def swap(self):
        """The two topmost items on the stack exchange places."""
        self.items[-1], self.items[-2] = self.items[-2], self.items[-1]

    def rotate(self, n, direction):
        """The n topmost items are moved on the stack in a rotating fashion."""
        d = deque(self.items[-n:])
        d.rotate(1 if direction is 'r' else -1)
        self.items = self.items[:-n] + list(d)

    def get_types(self):
        """Returns all unique object types within the stack."""
        return set([type(i) for i in self.items])
