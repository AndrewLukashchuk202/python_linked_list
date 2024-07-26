from __future__ import annotations
from typing import Optional


class Node:
    _value: str
    _next_node: Optional[Node]

    def __init__(self,
                 value,
                 _next_node=None):
        self._value = value
        self._next_node = _next_node

    @property
    def value(self) -> str:
        return self._value

    @value.setter
    def value(self, value: str):
        self._value = value

    @property
    def next_node(self):
        return self._next_node

    @next_node.setter
    def next_node(self, node: Node):
        self._next_node = node

    # not necessarymypy to use type hinting for default functions
    def __repr__(self) -> str:
        class_name = self.__class__.__name__
        return f"{class_name}({self._value!r}, {self._next_node!r})"

    def __str__(self):
        return f"Node: {self._value}"


if __name__ == '__main__':
    node = Node(42, Node(24))
    print(node)
