import unittest

class TestPartitionList(unittest.TestCase):
    def build_linked_list(self, values):
        """Helper to create a linked list from a Python list."""
        dummy = ListNode(0)
        current = dummy
        for v in values:
            current.next = ListNode(v)
            current = current.next
        return dummy.next

    def linked_list_to_list(self, head):
        """Helper to convert a linked list back to a Python list."""
        result = []
        while head:
            result.append(head.val)
            head = head.next
        return result

    def test_mixed_values(self):
        head = self.build_linked_list([1, 4, 3, 2, 5, 2])
        new_head = partition_list(head, 3)
        self.assertEqual(self.linked_list_to_list(new_head), [1, 2, 2, 4, 3, 5])

    def test_all_less_than_x(self):
        head = self.build_linked_list([1, 2, 2])
        new_head = partition_list(head, 3)
        self.assertEqual(self.linked_list_to_list(new_head), [1, 2, 2])

    def test_all_greater_or_equal_x(self):
        head = self.build_linked_list([3, 4, 5])
        new_head = partition_list(head, 3)
        self.assertEqual(self.linked_list_to_list(new_head), [3, 4, 5])

    def test_empty_list(self):
        new_head = partition_list(None, 5)
        self.assertIsNone(new_head)

    def test_single_node_less(self):
        head = self.build_linked_list([1])
        new_head = partition_list(head, 2)
        self.assertEqual(self.linked_list_to_list(new_head), [1])

    def test_single_node_greater_or_equal(self):
        head = self.build_linked_list([5])
        new_head = partition_list(head, 3)
        self.assertEqual(self.linked_list_to_list(new_head), [5])

    def test_duplicates_around_pivot(self):
        head = self.build_linked_list([2, 2, 3, 3, 1, 4])
        new_head = partition_list(head, 3)
        self.assertEqual(self.linked_list_to_list(new_head), [2, 2, 1, 3, 3, 4])