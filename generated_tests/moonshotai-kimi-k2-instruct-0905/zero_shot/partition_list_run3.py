import unittest

class TestPartitionList(unittest.TestCase):
    def to_list(self, head):
        """Convert linked list to Python list for easy comparison."""
        result = []
        while head:
            result.append(head.val)
            head = head.next
        return result

    def from_list(self, lst):
        """Convert Python list to linked list."""
        dummy = ListNode()
        current = dummy
        for val in lst:
            current.next = ListNode(val)
            current = current.next
        return dummy.next

    def test_empty_list(self):
        self.assertIsNone(partition_list(None, 1))

    def test_single_node_less_than_x(self):
        head = ListNode(1)
        result = partition_list(head, 2)
        self.assertEqual(self.to_list(result), [1])

    def test_single_node_greater_equal_x(self):
        head = ListNode(2)
        result = partition_list(head, 2)
        self.assertEqual(self.to_list(result), [2])

    def test_all_less_than_x(self):
        head = self.from_list([1, 2, 3])
        result = partition_list(head, 5)
        self.assertEqual(self.to_list(result), [1, 2, 3])

    def test_all_greater_equal_x(self):
        head = self.from_list([5, 6, 7])
        result = partition_list(head, 5)
        self.assertEqual(self.to_list(result), [5, 6, 7])

    def test_mixed_values(self):
        head = self.from_list([1, 4, 3, 2, 5, 2])
        result = partition_list(head, 3)
        self.assertEqual(self.to_list(result), [1, 2, 2, 4, 3, 5])

    def test_duplicates(self):
        head = self.from_list([3, 3, 3])
        result = partition_list(head, 3)
        self.assertEqual(self.to_list(result), [3, 3, 3])

    def test_negative_numbers(self):
        head = self.from_list([-1, 4, 0, 3, 2, -2])
        result = partition_list(head, 1)
        self.assertEqual(self.to_list(result), [-1, 0, 2, -2, 4, 3])