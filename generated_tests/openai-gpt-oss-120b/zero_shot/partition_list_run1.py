import unittest

class TestPartitionList(unittest.TestCase):
    def list_to_linked(self, values):
        """Helper to convert a Python list to a linked list of ListNode."""
        dummy = ListNode(0)
        current = dummy
        for v in values:
            node = ListNode(v)
            current.next = node
            current = node
        return dummy.next

    def linked_to_list(self, head):
        """Helper to convert a linked list back to a Python list."""
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
        result = partition_list(head, 10)
        self.assertEqual(self.linked_to_list(result), [1, 2, 3])

    def test_all_nodes_greater_or_equal_x(self):
        head = self.list_to_linked([5, 6, 7])
        result = partition_list(head, 5)
        self.assertEqual(self.linked_to_list(result), [5, 6, 7])

    def test_mixed_nodes(self):
        head = self.list_to_linked([1, 4, 3, 2, 5, 2])
        result = partition_list(head, 3)
        # Expected order: nodes <3 keep original relative order, then nodes >=3 keep original relative order
        self.assertEqual(self.linked_to_list(result), [1, 2, 2, 4, 3, 5])

    def test_single_node_less(self):
        head = self.list_to_linked([2])
        result = partition_list(head, 3)
        self.assertEqual(self.linked_to_list(result), [2])

    def test_single_node_equal(self):
        head = self.list_to_linked([3])
        result = partition_list(head, 3)
        self.assertEqual(self.linked_to_list(result), [3])

    def test_single_node_greater(self):
        head = self.list_to_linked([5])
        result = partition_list(head, 3)
        self.assertEqual(self.linked_to_list(result), [5])

    def test_preserves_relative_order(self):
        # Nodes less than x: 2, 1 (original order)
        # Nodes >= x: 4, 3 (original order)
        head = self.list_to_linked([2, 4, 1, 3])
        result = partition_list(head, 3)
        self.assertEqual(self.linked_to_list(result), [2, 1, 4, 3])

    def test_multiple_equal_to_x(self):
        head = self.list_to_linked([3, 1, 2, 3, 4])
        result = partition_list(head, 3)
        # Nodes <3: 1,2 ; Nodes >=3: 3,3,4 (preserve order)
        self.assertEqual(self.linked_to_list(result), [1, 2, 3, 3, 4])