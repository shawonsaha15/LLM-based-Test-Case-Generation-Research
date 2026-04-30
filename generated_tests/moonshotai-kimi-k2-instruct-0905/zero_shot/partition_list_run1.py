import unittest

class TestPartitionList(unittest.TestCase):

    def list_to_array(self, head):
        arr = []
        while head:
            arr.append(head.val)
            head = head.next
        return arr

    def array_to_list(self, arr):
        dummy = ListNode(0)
        current = dummy
        for val in arr:
            current.next = ListNode(val)
            current = current.next
        return dummy.next

    def test_empty_list(self):
        self.assertIsNone(partition_list(None, 1))

    def test_single_node_less_than_x(self):
        head = self.array_to_list([1])
        result = partition_list(head, 2)
        self.assertEqual(self.list_to_array(result), [1])

    def test_single_node_greater_equal_x(self):
        head = self.array_to_list([2])
        result = partition_list(head, 2)
        self.assertEqual(self.list_to_array(result), [2])

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
        self.assertEqual(self.list_to_array(result), [1, 2, 2, 4, 3, 5])

    def test_duplicates_around_x(self):
        head = self.array_to_list([3, 3, 3])
        result = partition_list(head, 3)
        self.assertEqual(self.list_to_array(result), [3, 3, 3])

    def test_negative_values(self):
        head = self.array_to_list([-1, 4, 0, 3, 2, -2])
        result = partition_list(head, 2)
        self.assertEqual(self.list_to_array(result), [-1, 0, -2, 4, 3, 2])