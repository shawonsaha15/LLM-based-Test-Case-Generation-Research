import unittest

class TestPartitionList(unittest.TestCase):
    def linked_list_to_list(self, head):
        result = []
        current = head
        while current:
            result.append(current.val)
            current = current.next
        return result

    def list_to_linked_list(self, lst):
        if not lst:
            return None
        head = ListNode(lst[0])
        current = head
        for val in lst[1:]:
            current.next = ListNode(val)
            current = current.next
        return head

    def test_normal_case(self):
        head = self.list_to_linked_list([1, 4, 3, 2, 5, 2])
        result = partition_list(head, 3)
        self.assertEqual(self.linked_list_to_list(result), [1, 2, 2, 4, 3, 5])

    def test_all_less_than_x(self):
        head = self.list_to_linked_list([1, 2, 3])
        result = partition_list(head, 4)
        self.assertEqual(self.linked_list_to_list(result), [1, 2, 3])

    def test_all_greater_or_equal_to_x(self):
        head = self.list_to_linked_list([4, 5, 6])
        result = partition_list(head, 4)
        self.assertEqual(self.linked_list_to_list(result), [4, 5, 6])

    def test_empty_list(self):
        result = partition_list(None, 3)
        self.assertIsNone(result)

    def test_single_node_less_than_x(self):
        head = ListNode(1)
        result = partition_list(head, 2)
        self.assertEqual(self.linked_list_to_list(result), [1])

    def test_single_node_greater_or_equal_to_x(self):
        head = ListNode(2)
        result = partition_list(head, 2)
        self.assertEqual(self.linked_list_to_list(result), [2])

    def test_duplicate_values(self):
        head = self.list_to_linked_list([2, 2, 2])
        result = partition_list(head, 2)
        self.assertEqual(self.linked_list_to_list(result), [2, 2, 2])

    def test_negative_values(self):
        head = self.list_to_linked_list([-1, -3, 2, 0])
        result = partition_list(head, -2)
        self.assertEqual(self.linked_list_to_list(result), [-3, -1, 2, 0])

    def test_large_values(self):
        head = self.list_to_linked_list([1000, 2000, 1500])
        result = partition_list(head, 1500)
        self.assertEqual(self.linked_list_to_list(result), [1000, 2000, 1500])

    def test_maintains_relative_order(self):
        head = self.list_to_linked_list([3, 1, 4, 2, 5])
        result = partition_list(head, 3)
        self.assertEqual(self.linked_list_to_list(result), [1, 2, 3, 4, 5])