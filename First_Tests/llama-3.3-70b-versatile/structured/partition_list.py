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
    def test_normal_cases(self):
        head = ListNode(1, ListNode(4, ListNode(3, ListNode(2, ListNode(5, ListNode(2))))))
        result = partition_list(head, 3)
        self.assertEqual(result.val, 1)
        self.assertEqual(result.next.val, 2)
        self.assertEqual(result.next.next.val, 2)
        self.assertEqual(result.next.next.next.val, 4)
        self.assertEqual(result.next.next.next.next.val, 3)
        self.assertEqual(result.next.next.next.next.next.val, 5)

    def test_edge_cases(self):
        head = ListNode(1)
        result = partition_list(head, 0)
        self.assertEqual(result.val, 1)
        self.assertIsNone(result.next)

        head = ListNode(1, ListNode(2))
        result = partition_list(head, 1)
        self.assertEqual(result.val, 1)
        self.assertEqual(result.next.val, 2)
        self.assertIsNone(result.next.next)

    def test_invalid_inputs(self):
        head = None
        result = partition_list(head, 5)
        self.assertIsNone(result)

        head = ListNode(1, ListNode(2, ListNode(3)))
        result = partition_list(head, None)
        with self.assertRaises(TypeError):
            partition_list(head, None)

if __name__ == "__main__":
    unittest.main()