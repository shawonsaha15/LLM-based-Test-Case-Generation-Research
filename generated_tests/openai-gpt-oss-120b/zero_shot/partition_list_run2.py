import unittest

class TestPartitionList(unittest.TestCase):
    def list_to_linked(self, values):
        """Convert a Python list to a linked list of ListNode."""
        dummy = ListNode(0)
        current = dummy
        for val in values:
            node = ListNode(val)
            current.next = node
            current = node
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

    def test_all_nodes_less_than_x(self):
        head = self.list_to_linked([1, 2, 3])
        result = partition_list(head, 5)
        self.assertEqual(self.linked_to_list(result), [1, 2, 3])

    def test_all_nodes_greater_or_equal_x(self):
        head = self.list_to_linked([5, 6, 7])
        result = partition_list(head, 5)
        self.assertEqual(self.linked_to_list(result), [5, 6, 7])

    def test_mixed_nodes(self):
        head = self.list_to_linked([1, 4, 3, 2, 5, 2])
        result = partition_list(head, 3)
        # Expected: nodes <3 preserve order (1,2,2), then nodes >=3 preserve order (4,3,5)
        self.assertEqual(self.linked_to_list(result), [1, 2, 2, 4, 3, 5])

    def test_single_node_less(self):
        head = self.list_to_linked([1])
        result = partition_list(head, 2)
        self.assertEqual(self.linked_to_list(result), [1])

    def test_single_node_greater_or_equal(self):
        head = self.list_to_linked([3])
        result = partition_list(head, 2)
        self.assertEqual(self.linked_to_list(result), [3])

    def test_duplicates_and_equal_to_x(self):
        head = self.list_to_linked([2, 1, 2, 3, 2, 4])
        result = partition_list(head, 2)
        # Nodes <2: [1]; Nodes >=2: [2,2,3,2,4] preserving original order
        self.assertEqual(self.linked_to_list(result), [1, 2, 2, 3, 2, 4])

    def test_preserve_original_relative_order(self):
        # Complex case to ensure stability within partitions
        original = [3, 5, 8, 5, 10, 2, 1]
        head = self.list_to_linked(original)
        result = partition_list(head, 5)
        # Nodes <5: [3,2,1]; Nodes >=5: [5,8,5,10] preserving order
        expected = [3, 2, 1, 5, 8, 5, 10]
        self.assertEqual(self.linked_to_list(result), expected)