import unittest

class TestPartitionList(unittest.TestCase):
    def list_to_linked(self, values):
        """Convert a Python list to a linked list of ListNode."""
        dummy = ListNode(0)
        current = dummy
        for v in values:
            node = ListNode(v)
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

    def test_all_less(self):
        values = [1, 2, 3, 4]
        head = self.list_to_linked(values)
        result = partition_list(head, 10)
        self.assertEqual(self.linked_to_list(result), values)

    def test_all_greater_or_equal(self):
        values = [10, 12, 15]
        head = self.list_to_linked(values)
        result = partition_list(head, 5)
        self.assertEqual(self.linked_to_list(result), values)

    def test_mixed_values(self):
        values = [3, 5, 8, 5, 10, 2, 1]
        expected = [3, 2, 1, 5, 8, 5, 10]  # preserve original order within partitions
        head = self.list_to_linked(values)
        result = partition_list(head, 5)
        self.assertEqual(self.linked_to_list(result), expected)

        # Ensure the last node points to None (no cycles)
        current = result
        while current and current.next:
            current = current.next
        self.assertIsNone(current.next)

    def test_single_node_less(self):
        head = self.list_to_linked([1])
        result = partition_list(head, 2)
        self.assertEqual(self.linked_to_list(result), [1])

    def test_single_node_greater_or_equal(self):
        head = self.list_to_linked([5])
        result = partition_list(head, 3)
        self.assertEqual(self.linked_to_list(result), [5])

    def test_duplicates_equal_x(self):
        values = [2, 3, 3, 2, 4, 3]
        expected = [2, 2, 3, 3, 4, 3]  # values <3 first, then >=3 preserving order
        head = self.list_to_linked(values)
        result = partition_list(head, 3)
        self.assertEqual(self.linked_to_list(result), expected)

    def test_negative_values(self):
        values = [-1, -4, 0, -2, 3]
        expected = [-1, -4, -2, 0, 3]  # x = 0, negatives first, then 0 and positives
        head = self.list_to_linked(values)
        result = partition_list(head, 0)
        self.assertEqual(self.linked_to_list(result), expected)

    def test_large_list(self):
        values = list(range(1000, 0, -1))  # 1000 down to 1
        x = 500
        head = self.list_to_linked(values)
        result = partition_list(head, x)
        result_list = self.linked_to_list(result)

        # All values < x should appear before any >= x
        split_index = next(i for i, v in enumerate(result_list) if v >= x)
        self.assertTrue(all(v < x for v in result_list[:split_index]))
        self.assertTrue(all(v >= x for v in result_list[split_index:]))

        # Preserve relative order within each partition
        expected_before = [v for v in values if v < x]
        expected_after = [v for v in values if v >= x]
        self.assertEqual(result_list, expected_before + expected_after)

    def test_invalid_input(self):
        with self.assertRaises(AttributeError):
            partition_list(123, 5)  # non-ListNode head should raise AttributeError

        with self.assertRaises(AttributeError):
            partition_list("not a node", 5)  # non-ListNode head

        # x can be any integer; passing non-int should raise TypeError during comparison
        head = self.list_to_linked([1, 2, 3])
        with self.assertRaises(TypeError):
            partition_list(head, "a")