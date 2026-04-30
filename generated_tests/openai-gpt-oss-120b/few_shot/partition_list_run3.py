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

    def test_mixed_values(self):
        head = self.list_to_linked([1, 4, 3, 2, 5, 2])
        new_head = partition_list(head, 3)
        self.assertEqual(self.linked_to_list(new_head), [1, 2, 2, 4, 3, 5])

    def test_all_less_than_x(self):
        head = self.list_to_linked([1, 2, 2])
        new_head = partition_list(head, 3)
        self.assertEqual(self.linked_to_list(new_head), [1, 2, 2])

    def test_all_greater_or_equal_x(self):
        head = self.list_to_linked([3, 4, 5])
        new_head = partition_list(head, 3)
        self.assertEqual(self.linked_to_list(new_head), [3, 4, 5])

    def test_empty_list(self):
        new_head = partition_list(None, 1)
        self.assertIsNone(new_head)

    def test_single_node_less_than_x(self):
        head = self.list_to_linked([1])
        new_head = partition_list(head, 2)
        self.assertEqual(self.linked_to_list(new_head), [1])

    def test_single_node_equal_to_x(self):
        head = self.list_to_linked([2])
        new_head = partition_list(head, 2)
        self.assertEqual(self.linked_to_list(new_head), [2])

    def test_preserves_relative_order(self):
        # Nodes less than x should keep original order, same for >= x
        head = self.list_to_linked([5, 1, 4, 3, 2, 6])
        new_head = partition_list(head, 4)
        # less than 4: 1,3,2 (original order)
        # >=4: 5,4,6 (original order)
        self.assertEqual(self.linked_to_list(new_head), [1, 3, 2, 5, 4, 6])