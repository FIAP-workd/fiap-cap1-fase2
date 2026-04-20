from __future__ import annotations
from typing import Any, Optional

EMPTY_VALUE_NODE = '__EMPTY_NODE_VALUE__'

class Node:
    def __init__(self, value):
        self.value = value
        self.next: Optional[Node] = None

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
    
    @property
    def get_count(self):
        return self._count

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


    @staticmethod
    def findMidle(head):
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow


    @staticmethod
    def mergeTwoLists(l1, l2):
        head = Node(EMPTY_VALUE_NODE)
        tail = head

        while l1 and l2:
            if l1.value.prioridade < l2.value.prioridade:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        tail.next = l1 or l2
        return head.next

    def merge_sort(self, header=None):
        if not header or not header.next:
            return header
    
        middle = self.findMidle(header)
        afterMiddle = middle.next
        middle.next = None

        left = self.merge_sort(header)
        right = self.merge_sort(afterMiddle)

        sorted_list = self.mergeTwoLists(left, right)
        return sorted_list
    
    def display(self):
        """Mostra todos os valores da fila sem removê-los"""
        if not self.first or self.first.value == EMPTY_VALUE_NODE:
            print("Fila vazia")
            return
        
        current = self.first
        values = []
        
        while current and current.value != EMPTY_VALUE_NODE:
            values.append(current.value)
            current = current.next
        
        print(" -> ".join(str(v) for v in values))
        

