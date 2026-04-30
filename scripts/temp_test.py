from functions.partition_list import partition_list

import unittest

class TestPartitionList(unittest.TestCase):
    def list_to_linked(self, values):
        """Convert a Python list to a linked list of ListNode."""
        dummy = ListNode(0)
        current = dummy
        for v in values:
            current.next = ListNode(v)
            current = current.next
        return dummy.next

    def linked_to_list(self, head):
        """Convert a linked list of ListNode back to a Python list."""
        result = []
        current = head
        while current:
            result.append(current.val)
            current = current.next
        return result

    def test_empty_list(self):
        head = None
        result = partition_list(head, 5)
        self.assertIsNone(result)

    def test_all_less_than_x(self):
        head = self.list_to_linked([1, 2, 3])
        result = partition_list(head, 5)
        self.assertEqual(self.linked_to_list(result), [1, 2, 3])

    def test_all_greater_or_equal_x(self):
        head = self.list_to_linked([5, 6, 7])
        result = partition_list(head, 5)
        self.assertEqual(self.linked_to_list(result), [5, 6, 7])

    def test_mixed_values(self):
        head = self.list_to_linked([1, 4, 3, 2, 5, 2])
        result = partition_list(head, 3)
        self.assertEqual(self.linked_to_list(result), [1, 2, 2, 4, 3, 5])

    def test_duplicates_around_x(self):
        head = self.list_to_linked([3, 3, 2, 1])
        result = partition_list(head, 3)
        self.assertEqual(self.linked_to_list(result), [2, 1, 3, 3])

    def test_single_node_less(self):
        head = self.list_to_linked([1])
        result = partition_list(head, 2)
        self.assertEqual(self.linked_to_list(result), [1])

    def test_single_node_greater_or_equal(self):
        head = self.list_to_linked([3])
        result = partition_list(head, 2)
        self.assertEqual(self.linked_to_list(result), [3])

    def test_preserves_relative_order(self):
        head = self.list_to_linked([2, 1, 3, 2, 4, 1])
        result = partition_list(head, 3)
        # Nodes < 3: 2,1,2,1 (original order)
        # Nodes >=3: 3,4 (original order)
        self.assertEqual(self.linked_to_list(result), [2, 1, 2, 1, 3, 4])