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
        node1 = ListNode(1)
        node2 = ListNode(4)
        node3 = ListNode(3)
        node4 = ListNode(2)
        node5 = ListNode(5)

        node1.next = node2
        node2.next = node3
        node3.next = node4
        node4.next = node5

        result = partition_list(node1, 3)

        self.assertEqual(result.val, 1)
        self.assertEqual(result.next.val, 2)
        self.assertEqual(result.next.next.val, 4)
        self.assertEqual(result.next.next.next.val, 5)
        self.assertEqual(result.next.next.next.next, None)

    def test_all_before(self):
        node1 = ListNode(1)
        node2 = ListNode(1)
        node3 = ListNode(1)

        node1.next = node2
        node2.next = node3

        result = partition_list(node1, 2)

        self.assertEqual(result.val, 1)
        self.assertEqual(result.next.val, 1)
        self.assertEqual(result.next.next.val, 1)
        self.assertEqual(result.next.next.next, None)

    def test_all_after(self):
        node1 = ListNode(4)
        node2 = ListNode(5)
        node3 = ListNode(5)

        node1.next = node2
        node2.next = node3

        result = partition_list(node1, 3)

        self.assertEqual(result.val, 4)
        self.assertEqual(result.next.val, 5)
        self.assertEqual(result.next.next.val, 5)
        self.assertEqual(result.next.next.next, None)

    def test_empty_list(self):
        result = partition_list(None, 3)

        self.assertEqual(result, None)

if __name__ == "__main__":
    unittest.main()