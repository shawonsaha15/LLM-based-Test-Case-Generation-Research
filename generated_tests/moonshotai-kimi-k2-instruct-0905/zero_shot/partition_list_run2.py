import unittest


class TestPartitionList(unittest.TestCase):

    def list_to_array(self, head):
        """Convert linked list to Python list for easy comparison."""
        result = []
        while head:
            result.append(head.val)
            head = head.next
        return result

    def array_to_list(self, arr):
        """Convert Python list to linked list."""
        if not arr:
            return None
        head = ListNode(arr[0])
        current = head
        for val in arr[1:]:
            current.next = ListNode(val)
            current = current.next
        return head

    def test_empty_list(self):
        self.assertIsNone(partition_list(None, 3))

    def test_single_node_less_than_x(self):
        head = self.array_to_list([1])
        result = partition_list(head, 2)
        self.assertEqual(self.list_to_array(result), [1])

    def test_single_node_greater_equal_x(self):
        head = self.array_to_list([3])
        result = partition_list(head, 3)
        self.assertEqual(self.list_to_array(result), [3])

    def test_all_less_than_x(self):
        head = self.array_to_list([1, 2, 3])
        result = partition_list(head, 5)
        self.assertEqual(self.list_to_array(result), [1, 2, 3])

    def test_all_greater_equal_x(self):
        head = self.array_to_list([5, 6, 7])
        result = partition_list(head, 5)
        self.assertEqual(self.list_to_array(result), [5, 6, 7])

    def test_mixed_values(self):
        head = self.array_to_list([1, 4, 3, 2, 5, 2])
        result = partition_list(head, 3)
        # All nodes < 3 should come before nodes >= 3, preserving relative order
        self.assertEqual(self.list_to_array(result), [1, 2, 2, 4, 3, 5])

    def test_duplicates_around_x(self):
        head = self.array_to_list([3, 3, 3])
        result = partition_list(head, 3)
        self.assertEqual(self.list_to_array(result), [3, 3, 3])

    def test_large_x(self):
        head = self.array_to_list([10, 20, 30])
        result = partition_list(head, 100)
        self.assertEqual(self.list_to_array(result), [10, 20, 30])

    def test_small_x(self):
        head = self.array_to_list([10, 20, 30])
        result = partition_list(head, 1)
        self.assertEqual(self.list_to_array(result), [10, 20, 30])

    def test_head_becomes_none(self):
        # All nodes >= x, and x is smaller than all values
        head = self.array_to_list([5, 6, 7])
        result = partition_list(head, 1)
        self.assertEqual(self.list_to_array(result), [5, 6, 7])

    def test_head_remains_same(self):
        # All nodes < x
        head = self.array_to_list([1, 2, 3])
        result = partition_list(head, 10)
        self.assertEqual(self.list_to_array(result), [1, 2, 3])

    def test_negative_values(self):
        head = self.array_to_list([-1, -2, 3, 4, -5])
        result = partition_list(head, 0)
        self.assertEqual(self.list_to_array(result), [-1, -2, -5, 3, 4])