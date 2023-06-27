#!/usr/bin/python3
"""
This module defines Node and SinglyLinkedList classes, creating a singly-linked 
list data structure. Each node in the list contains integer data and reference 
to the next node.
"""


class Node:
    """
    A node in a singly-linked list. Contains integer data and reference to the 
    next node.
    """

    def __init__(self, data, next_node=None):
        """Initialize a new Node with data and next_node."""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Retrieve the data of the Node."""
        return self.__data

    @data.setter
    def data(self, value):
        """Set data with validation."""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Retrieve the next_node of the Node."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Set next_node with validation."""
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """
    A singly-linked list, which is a collection of Nodes that are connected in 
    a sequential manner. The list has a head node, and each node points to the 
    next node in the list. 
    """

    def __init__(self):
        """Initialize an empty SinglyLinkedList."""
        self.__head = None

    def sorted_insert(self, value):
        """Insert a new Node in sorted position (increasing order)."""
        new_node = Node(value)
        if self.__head is None or self.__head.data >= new_node.data:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            current = self.__head
            while current.next_node is not None and current.next_node.data < new_node.data:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node

    def __str__(self):
        """Print the entire list, one node number per line."""
        current = self.__head
        nodes = []
        while current is not None:
            nodes.append(str(current.data))
            current = current.next_node
        return "\n".join(nodes)
