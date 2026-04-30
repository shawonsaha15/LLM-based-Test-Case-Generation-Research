class ListNode:
    def __init__(self, val: int = 0, next: 'ListNode' = None):
        self.val = val
        self.next = next


def partition_list(head: ListNode, x: int) -> ListNode:
    before_head = ListNode(0)
    after_head = ListNode(0)

    before = before_head
    after = after_head

    current = head

    while current:
        if current.val < x:
            before.next = current
            before = current
        else:
            after.next = current
            after = current
        current = current.next

    after.next = None
    before.next = after_head.next

    return before_head.next

import unittest

def build_linked_list(values):
    dummy = ListNode(0)
    current = dummy
    for v in values:
        node = ListNode(v)
        current.next = node
        current = node
    return dummy.next

def linked_list_to_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

class TestPartitionList(unittest.TestCase):
    def test_empty(self):
        self.assertIsNone(partition_list(None, 5))

    def test_single_node_less(self):
        head = build_linked_list([1])
        new_head = partition_list(head, 2)
        self.assertEqual(linked_list_to_list(new_head), [1])

    def test_single_node_greater(self):
        head = build_linked_list([3])
        new_head = partition_list(head, 2)
        self.assertEqual(linked_list_to_list(new_head), [3])

    def test_all_less(self):
        head = build_linked_list([1, 2, 0])
        new_head = partition_list(head, 5)
        self.assertEqual(linked_list_to_list(new_head), [1, 2, 0])

    def test_all_greater_equal(self):
        head = build_linked_list([5, 6, 7])
        new_head = partition_list(head, 5)
        self.assertEqual(linked_list_to_list(new_head), [5, 6, 7])

    def test_mixed(self):
        head = build_linked_list([1, 4, 3, 2, 5, 2])
        new_head = partition_list(head, 3)
        self.assertEqual(linked_list_to_list(new_head), [1, 2, 2, 4, 3, 5])

    def test_invalid_x_type(self):
        head = build_linked_list([1, 2, 3])
        with self.assertRaises(TypeError):
            partition_list(head, "2")

    def test_invalid_head_type(self):
        with self.assertRaises(AttributeError):
            partition_list(123, 2)

if __name__ == "__main__":
    unittest.main()