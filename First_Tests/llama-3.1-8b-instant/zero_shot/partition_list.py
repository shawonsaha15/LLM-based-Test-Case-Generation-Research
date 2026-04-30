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
    def test_normal_case(self):
        # Create a linked list: 1 -> 4 -> 3 -> 2 -> 5 -> 2
        head = ListNode(1)
        head.next = ListNode(4)
        head.next.next = ListNode(3)
        head.next.next.next = ListNode(2)
        head.next.next.next.next = ListNode(5)
        head.next.next.next.next.next = ListNode(2)

        # Partition the list at x = 3
        result = partition_list(head, 3)

        # Expected result: 1 -> 2 -> 2 -> 4 -> 3 -> 5
        expected = ListNode(1)
        expected.next = ListNode(2)
        expected.next.next = ListNode(2)
        expected.next.next.next = ListNode(4)
        expected.next.next.next.next = ListNode(3)
        expected.next.next.next.next.next = ListNode(5)

        self.assertEqual(result.val, expected.val)
        self.assertEqual(result.next.val, expected.next.val)
        self.assertEqual(result.next.next.val, expected.next.next.val)
        self.assertEqual(result.next.next.next.val, expected.next.next.next.val)
        self.assertEqual(result.next.next.next.next.val, expected.next.next.next.next.val)
        self.assertEqual(result.next.next.next.next.next.val, expected.next.next.next.next.next.val)

    def test_edge_case_empty_list(self):
        # Create an empty linked list
        head = None

        # Partition the list at x = 3
        result = partition_list(head, 3)

        # Expected result: None
        self.assertIsNone(result)

    def test_edge_case_single_node_list(self):
        # Create a linked list with a single node: 5
        head = ListNode(5)

        # Partition the list at x = 3
        result = partition_list(head, 3)

        # Expected result: 5
        self.assertEqual(result.val, 5)
        self.assertIsNone(result.next)

    def test_edge_case_partition_at_zero(self):
        # Create a linked list: 1 -> 4 -> 3 -> 2 -> 5 -> 2
        head = ListNode(1)
        head.next = ListNode(4)
        head.next.next = ListNode(3)
        head.next.next.next = ListNode(2)
        head.next.next.next.next = ListNode(5)
        head.next.next.next.next.next = ListNode(2)

        # Partition the list at x = 0
        result = partition_list(head, 0)

        # Expected result: 1 -> 2 -> 2 -> 4 -> 3 -> 5
        expected = ListNode(1)
        expected.next = ListNode(2)
        expected.next.next = ListNode(2)
        expected.next.next.next = ListNode(4)
        expected.next.next.next.next = ListNode(3)
        expected.next.next.next.next.next = ListNode(5)

        self.assertEqual(result.val, expected.val)
        self.assertEqual(result.next.val, expected.next.val)
        self.assertEqual(result.next.next.val, expected.next.next.val)
        self.assertEqual(result.next.next.next.val, expected.next.next.next.val)
        self.assertEqual(result.next.next.next.next.val, expected.next.next.next.next.val)
        self.assertEqual(result.next.next.next.next.next.val, expected.next.next.next.next.next.val)

    def test_invalid_input_non_integer_x(self):
        # Create a linked list: 1 -> 4 -> 3 -> 2 -> 5 -> 2
        head = ListNode(1)
        head.next = ListNode(4)
        head.next.next = ListNode(3)
        head.next.next.next = ListNode(2)
        head.next.next.next.next = ListNode(5)
        head.next.next.next.next.next = ListNode(2)

        # Partition the list at x = 3.14
        with self.assertRaises(TypeError):
            partition_list(head, 3.14)

    def test_invalid_input_negative_x(self):
        # Create a linked list: 1 -> 4 -> 3 -> 2 -> 5 -> 2
        head = ListNode(1)
        head.next = ListNode(4)
        head.next.next = ListNode(3)
        head.next.next.next = ListNode(2)
        head.next.next.next.next = ListNode(5)
        head.next.next.next.next.next = ListNode(2)

        # Partition the list at x = -3
        with self.assertRaises(TypeError):
            partition_list(head, -3)

if __name__ == "__main__":
    unittest.main()