from node import Node
from typing import Any


class LinkedList:
    _root: Node | None

    def __init__(self, _node: Node | None = None):
        self._root = _node

    def append(self, value: Any) -> None:
        new_node = Node(value)
        new_node.next_node = self._root
        self._root = new_node

    def pop(self) -> Any:
        # (1) make the root's next node the new root
        # (2) return the root node's value

        if self._root is None:
            raise IndexError("Popping from an empty list")

        value = self._root.value
        self._root = self._root.next_node
        return value

    def to_list(self) -> list:
        if self._root is None:
            return []

        current_node = self._root

        value_list = []

        while current_node.next_node is not None:
            value_list.append(current_node.value)
            current_node = current_node.next_node

        return value_list
