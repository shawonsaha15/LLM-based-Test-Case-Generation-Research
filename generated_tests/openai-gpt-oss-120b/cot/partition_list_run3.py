import unittest

class TestPartitionList(unittest.TestCase):
    def list_to_linked(self, values):
        """Helper to convert a Python list to a linked list."""
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
        self.assertIsNone(partition_list(None, 5))

    def test_single_element_less(self):
        head = self.list_to_linked([1])
        new_head = partition_list(head, 5)
        self.assertEqual(self.linked_to_list(new_head), [1])

    def test_single_element_equal(self):
        head = self.list_to_linked([5])
        new_head = partition_list(head, 5)
        self.assertEqual(self.linked_to_list(new_head), [5])

    def test_single_element_greater(self):
        head = self.list_to_linked([10])
        new_head = partition_list(head, 5)
        self.assertEqual(self.linked_to_list(new_head), [10])

    def test_all_less(self):
        values = [1, 2, 3, 4]
        head = self.list_to_linked(values)
        new_head = partition_list(head, 10)
        self.assertEqual(self.linked_to_list(new_head), values)

    def test_all_greater_or_equal(self):
        values = [10, 9, 8, 7]
        head = self.list_to_linked(values)
        new_head = partition_list(head, 5)
        self.assertEqual(self.linked_to_list(new_head), values)

    def test_mixed_values(self):
        values = [1, 4, 3, 2, 5, 2]
        expected = [1, 4, 3, 2, 5, 2]  # after partition with x=3 -> [1,2,2,4,3,5]
        head = self.list_to_linked(values)
        new_head = partition_list(head, 3)
        self.assertEqual(self.linked_to_list(new_head), [1, 2, 2, 4, 3, 5])

    def test_preserve_relative_order(self):
        values = [3, 5, 8, 5, 10, 2, 1]
        head = self.list_to_linked(values)
        new_head = partition_list(head, 5)
        # Nodes <5 keep original order: 3,2,1 ; Nodes >=5 keep original order:5,8,5,10
        self.assertEqual(self.linked_to_list(new_head), [3, 2, 1, 5, 8, 5, 10])

    def test_x_boundary(self):
        values = [5, 1, 5, 2, 5, 3]
        head = self.list_to_linked(values)
        new_head = partition_list(head, 5)
        # Values <5: 1,2,3 ; Values >=5:5,5,5
        self.assertEqual(self.linked_to_list(new_head), [1, 2, 3, 5, 5, 5])

    def test_large_list(self):
        values = list(range(1000, 0, -1))  # 1000..1
        head = self.list_to_linked(values)
        new_head = partition_list(head, 500)
        result = self.linked_to_list(new_head)
        # Verify partition property
        pivot_index = next(i for i, v in enumerate(result) if v >= 500)
        self.assertTrue(all(v < 500 for v in result[:pivot_index]))
        self.assertTrue(all(v >= 500 for v in result[pivot_index:]))

    def test_invalid_x_type(self):
        head = self.list_to_linked([1, 2, 3])
        with self.assertRaises(TypeError):
            partition_list(head, "a")

    def test_invalid_head_type(self):
        with self.assertRaises(AttributeError):
            partition_list([1, 2, 3], 2)