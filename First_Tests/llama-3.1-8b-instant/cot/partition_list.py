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

    def test_normal_input(self):
        node1 = ListNode(1)
        node2 = ListNode(4)
        node3 = ListNode(3)
        node4 = ListNode(2)
        node5 = ListNode(5)
        node1.next = node2
        node2.next = node3
        node3.next = node4
        node4.next = node5

        expected = ListNode(1)
        expected.next = ListNode(2)
        expected.next.next = ListNode(4)
        expected.next.next.next = ListNode(5)
        expected.next.next.next.next = ListNode(3)

        result = partition_list(node1, 3)
        self.assertEqual(result.val, 1)
        self.assertEqual(result.next.val, 2)
        self.assertEqual(result.next.next.val, 4)
        self.assertEqual(result.next.next.next.val, 5)
        self.assertEqual(result.next.next.next.next.val, 3)

    def test_edge_case_empty_list(self):
        self.assertIsNone(partition_list(None, 5))

    def test_edge_case_single_node(self):
        node = ListNode(5)
        self.assertEqual(partition_list(node, 3).val, 5)

    def test_invalid_input_non_integer(self):
        with self.assertRaises(TypeError):
            partition_list(ListNode(1), 'a')

    def test_invalid_input_negative_integer(self):
        with self.assertRaises(TypeError):
            partition_list(ListNode(1), -5)

    def test_invalid_input_non_integer_x(self):
        with self.assertRaises(TypeError):
            partition_list(ListNode(1), 5.5)

    def test_invalid_input_non_integer_head(self):
        with self.assertRaises(TypeError):
            partition_list('a', 5)

    def test_invalid_input_none_head(self):
        with self.assertRaises(TypeError):
            partition_list(None, 5)

if __name__ == '__main__':
    unittest.main()