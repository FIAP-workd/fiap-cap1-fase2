from typing import Any

EMPTY_VALUE_NODE = '__EMPTY_NODE_VALUE__'

class Node:
    def __init__(self, value):
        self.value = value
        self.next: Node

    def __repr__(self):
        return f'{self.value}'
    
    def __bool__(self):
        return bool(self.value != EMPTY_VALUE_NODE)
    

class Queue:
    def __init__(self):
        self.first: Node = Node(EMPTY_VALUE_NODE)
        self.last: Node = Node(EMPTY_VALUE_NODE)
        self._count = 0

    def push(self, node_value: Any):
        new_node = Node(node_value)

        if not self.first:
            self.first = new_node

        if not self.last:
            self.last = new_node
        
        else:
            self.last.next = new_node
            self.last = new_node

        self._count += 1

    def pop(self):
        if not self.first:
            raise ValueError("Pop doesn't work in Empty Queue.")
        
        first = self.first
        
        if hasattr(self.first, 'next'):
            self.first = self.first.next
        else:
            self.first = Node(EMPTY_VALUE_NODE)

        self._count -= 1

        return first

    def peek(self):
        return self.first
    
    def __len__(self):
        return self._count
    
    def __bool__(self):
        return bool(self._count)
    
    def __iter__(self):
        return self
    
    def __next__(self):
        try:
            next_value = self.pop()
            return next_value
        except ValueError:
            raise StopIteration