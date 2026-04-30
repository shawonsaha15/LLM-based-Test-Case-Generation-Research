import unittest

class PartitionListTest(unittest.TestCase):
    def build_linked(self, values):
        """Helper to create a linked list from a Python list."""
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
        while head:
            result.append(head.val)
            head = head.next
        return result

    def test_empty_list(self):
        head = None
        result = partition_list(head, 5)
        self.assertIsNone(result)

    def test_all_less_than_x(self):
        head = self.build_linked([1, 2, 3])
        result = partition_list(head, 10)
        self.assertEqual(self.linked_to_list(result), [1, 2, 3])

    def test_all_greater_or_equal_to_x(self):
        head = self.build_linked([5, 6, 7])
        result = partition_list(head, 5)
        self.assertEqual(self.linked_to_list(result), [5, 6, 7])

    def test_mixed_values(self):
        head = self.build_linked([1, 4, 3, 2, 5, 2])
        result = partition_list(head, 3)
        # Expected order: nodes <3 keep original order, then nodes >=3 keep original order
        self.assertEqual(self.linked_to_list(result), [1, 2, 2, 4, 3, 5])

    def test_single_node_less(self):
        head = self.build_linked([2])
        result = partition_list(head, 3)
        self.assertEqual(self.linked_to_list(result), [2])

    def test_single_node_equal(self):
        head = self.build_linked([3])
        result = partition_list(head, 3)
        self.assertEqual(self.linked_to_list(result), [3])

    def test_duplicates_around_x(self):
        head = self.build_linked([3, 1, 2, 3, 4, 2])
        result = partition_list(head, 3)
        # Nodes <3: 1,2,2 (preserve order)
        # Nodes >=3: 3,3,4 (preserve order)
        self.assertEqual(self.linked_to_list(result), [1, 2, 2, 3, 3, 4])

    def test_x_not_present(self):
        head = self.build_linked([5, 1, 4, 2])
        result = partition_list(head, 3)
        # Nodes <3: 1,2 ; Nodes >=3: 5,4
        self.assertEqual(self.linked_to_list(result), [1, 2, 5, 4])