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

class TestPartitionList(unittest.TestCase):
    def test_basic(self):
        # Create a list: 1 -> 4 -> 3 -> 2 -> 5 -> 2
        head = ListNode(1)
        head.next = ListNode(4)
        head.next.next = ListNode(3)
        head.next.next.next = ListNode(2)
        head.next.next.next.next = ListNode(5)
        head.next.next.next.next.next = ListNode(2)

        result = partition_list(head, 3)
        self.assertEqual(result.val, 1)
        self.assertEqual(result.next.val, 2)
        self.assertEqual(result.next.next.val, 2)
        self.assertEqual(result.next.next.next.val, 4)
        self.assertEqual(result.next.next.next.next.val, 3)
        self.assertEqual(result.next.next.next.next.next.val, 5)

    def test_edge(self):
        # Create a list: 1
        head = ListNode(1)

        result = partition_list(head, 0)
        self.assertEqual(result.val, 1)

        result = partition_list(head, 1)
        self.assertEqual(result.val, 1)

        result = partition_list(head, 2)
        self.assertEqual(result.val, 1)

    def test_empty(self):
        result = partition_list(None, 0)
        self.assertIsNone(result)

    def test_all_less(self):
        # Create a list: 1 -> 2 -> 3
        head = ListNode(1)
        head.next = ListNode(2)
        head.next.next = ListNode(3)

        result = partition_list(head, 4)
        self.assertEqual(result.val, 1)
        self.assertEqual(result.next.val, 2)
        self.assertEqual(result.next.next.val, 3)

    def test_all_greater(self):
        # Create a list: 4 -> 5 -> 6
        head = ListNode(4)
        head.next = ListNode(5)
        head.next.next = ListNode(6)

        result = partition_list(head, 3)
        self.assertEqual(result.val, 4)
        self.assertEqual(result.next.val, 5)
        self.assertEqual(result.next.next.val, 6)

if __name__ == "__main__":
    unittest.main()