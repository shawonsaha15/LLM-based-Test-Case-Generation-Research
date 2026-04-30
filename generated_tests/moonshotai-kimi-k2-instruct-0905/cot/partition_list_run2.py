import unittest

class TestPartitionList(unittest.TestCase):

    def list_to_array(self, head):
        result = []
        current = head
        while current:
            result.append(current.val)
            current = current.next
        return result

    def array_to_list(self, arr):
        if not arr:
            return None
        head = ListNode(arr[0])
        current = head
        for val in arr[1:]:
            current.next = ListNode(val)
            current = current.next
        return head

    def test_normal_case(self):
        head = self.array_to_list([1, 4, 3, 2, 5, 2])
        x = 3
        result = partition_list(head, x)
        self.assertEqual(self.list_to_array(result), [1, 2, 2, 4, 3, 5])

    def test_all_less_than_x(self):
        head = self.array_to_list([1, 2, 2])
        x = 3
        result = partition_list(head, x)
        self.assertEqual(self.list_to_array(result), [1, 2, 2])

    def test_all_greater_or_equal_to_x(self):
        head = self.array_to_list([4, 5, 6])
        x = 3
        result = partition_list(head, x)
        self.assertEqual(self.list_to_array(result), [4, 5, 6])

    def test_empty_list(self):
        head = None
        x = 3
        result = partition_list(head, x)
        self.assertIsNone(result)

    def test_single_node_less_than_x(self):
        head = self.array_to_list([1])
        x = 3
        result = partition_list(head, x)
        self.assertEqual(self.list_to_array(result), [1])

    def test_single_node_greater_or_equal_to_x(self):
        head = self.array_to_list([4])
        x = 3
        result = partition_list(head, x)
        self.assertEqual(self.list_to_array(result), [4])

    def test_duplicate_values(self):
        head = self.array_to_list([1, 1, 1])
        x = 1
        result = partition_list(head, x)
        self.assertEqual(self.list_to_array(result), [1, 1, 1])

    def test_negative_values(self):
        head = self.array_to_list([-1, -4, 3, -2, 5, 2])
        x = 0
        result = partition_list(head, x)
        self.assertEqual(self.list_to_array(result), [-1, -4, -2, 3, 5, 2])

    def test_large_values(self):
        head = self.array_to_list([1000000, 1, 2000000])
        x = 1500000
        result = partition_list(head, x)
        self.assertEqual(self.list_to_array(result), [1000000, 1, 2000000])

    def test_zero_in_list(self):
        head = self.array_to_list([0, 1, -1])
        x = 0
        result = partition_list(head, x)
        self.assertEqual(self.list_to_array(result), [-1, 0, 1])

    def test_x_equal_to_node_value(self):
        head = self.array_to_list([3, 3, 3])
        x = 3
        result = partition_list(head, x)
        self.assertEqual(self.list_to_array(result), [3, 3, 3])

    def test_mixed_order(self):
        head = self.array_to_list([5, 1, 3, 2, 4])
        x = 3
        result = partition_list(head, x)
        self.assertEqual(self.list_to_array(result), [1, 2, 5, 3, 4])