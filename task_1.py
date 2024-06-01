from typing import Any, List, Optional, Tuple


class ListNode:
    def __init__(self, value: Any = 0, next_node: Optional['ListNode'] = None):
        self.value = value
        self.next_node = next_node


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value: Any) -> None:
        if not self.head:
            self.head = ListNode(value)
        else:
            current = self.head
            while current.next_node:
                current = current.next_node
            current.next_node = ListNode(value)

    def delete(self, value: Any) -> None:
        if not self.head:
            return
        if self.head.value == value:
            self.head = self.head.next_node
            return
        current = self.head
        while current.next_node:
            if current.next_node.value == value:
                current.next_node = current.next_node.next_node
                return
            current = current.next_node

    def to_list(self) -> List[Any]:
        result = []
        current = self.head
        while current:
            result.append(current.value)
            current = current.next_node
        return result

    @classmethod
    def from_list(cls, values: List[Any]) -> 'LinkedList':
        linked_list = cls()
        for value in values:
            linked_list.append(value)
        return linked_list

    def print_list(self) -> None:
        current = self.head
        while current:
            print(current.value, end=' -> ')
            current = current.next_node
        print('None')

    def reverse(self) -> None:
        prev = None
        current = self.head
        while current:
            next_node = current.next_node
            current.next_node = prev
            prev = current
            current = next_node
        self.head = prev

    def merge(self, left: Optional[ListNode], right: Optional[ListNode]) -> Optional[ListNode]:
        if not left:
            return right
        if not right:
            return left
        if left.value < right.value:
            left.next_node = self.merge(left.next_node, right)
            return left
        right.next_node = self.merge(left, right.next_node)
        return right

    def merge_sort(self) -> None:
        if not self.head or not self.head.next_node:
            return
        left, right = self.split_list()
        left.merge_sort()
        right.merge_sort()
        self.head = self.merge(left.head, right.head)

    def split_list(self) -> Tuple['LinkedList']:
        slow = self.head
        fast = self.head
        prev = None
        while fast and fast.next_node:
            prev = slow
            slow = slow.next_node
            fast = fast.next_node.next_node
        prev.next_node = None
        left = LinkedList()
        left.head = self.head
        right = LinkedList()
        right.head = slow
        return left, right


if __name__ == "__main__":
    linked_list = LinkedList.from_list([2, 1, 3, 5, 4, 6])
    linked_list.print_list()
    linked_list.reverse()
    linked_list.print_list()
    linked_list.merge_sort()
    linked_list.print_list()
    linked_list2 = LinkedList.from_list([8, 7, 9, 11, 10, 12])
    linked_list2.merge_sort()
    linked_list2.print_list()
    linked_list.merge(linked_list.head, linked_list2.head)
    linked_list.print_list()
