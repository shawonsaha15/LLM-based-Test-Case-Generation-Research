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
        self.assertEqual(linked_list_to_list(partition_list(None, 5)), [])

    def test_all_less(self):
        head = build_linked_list([1, 2, 3])
        result = linked_list_to_list(partition_list(head, 5))
        self.assertEqual(result, [1, 2, 3])

    def test_all_greater_or_equal(self):
        head = build_linked_list([5, 6, 7])
        result = linked_list_to_list(partition_list(head, 5))
        self.assertEqual(result, [5, 6, 7])

    def test_mixed(self):
        head = build_linked_list([1, 4, 3, 2, 5, 2])
        result = linked_list_to_list(partition_list(head, 3))
        self.assertEqual(result, [1, 2, 2, 4, 3, 5])

    def test_duplicates(self):
        head = build_linked_list([3, 1, 2, 3, 4, 2])
        result = linked_list_to_list(partition_list(head, 3))
        self.assertEqual(result, [1, 2, 2, 3, 3, 4])

    def test_x_at_bounds(self):
        head = build_linked_list([2, 1, 3])
        result = linked_list_to_list(partition_list(head, 1))
        self.assertEqual(result, [1, 2, 3])
        head = build_linked_list([2, 1, 3])
        result = linked_list_to_list(partition_list(head, 4))
        self.assertEqual(result, [2, 1, 3])

if __name__ == "__main__":
    unittest.main()