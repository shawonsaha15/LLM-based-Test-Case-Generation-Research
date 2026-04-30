import unittest

class TestPartitionList(unittest.TestCase):
    def _list_to_linked(self, values):
        """Helper to convert a Python list to a linked list."""
        dummy = ListNode(0)
        current = dummy
        for v in values:
            node = ListNode(v)
            current.next = node
            current = node
        return dummy.next

    def _linked_to_list(self, head):
        """Helper to convert a linked list back to a Python list."""
        result = []
        current = head
        while current:
            result.append(current.val)
            current = current.next
        return result

    def test_normal_case(self):
        # Arrange
        input_vals = [1, 4, 3, 2, 5, 2]
        x = 3
        head = self._list_to_linked(input_vals)
        expected_vals = [1, 2, 2, 4, 3, 5]

        # Act
        result_head = partition_list(head, x)

        # Assert
        self.assertEqual(self._linked_to_list(result_head), expected_vals)

    def test_boundary_empty_list(self):
        # Arrange
        head = None
        x = 1
        expected = None

        # Act
        result = partition_list(head, x)

        # Assert
        self.assertIs(result, expected)

    def test_boundary_single_node_less(self):
        # Arrange
        head = self._list_to_linked([0])
        x = 5
        expected = [0]

        # Act
        result_head = partition_list(head, x)

        # Assert
        self.assertEqual(self._linked_to_list(result_head), expected)

    def test_boundary_single_node_greater_or_equal(self):
        # Arrange
        head = self._list_to_linked([10])
        x = 5
        expected = [10]

        # Act
        result_head = partition_list(head, x)

        # Assert
        self.assertEqual(self._linked_to_list(result_head), expected)

    def test_boundary_all_nodes_less(self):
        # Arrange
        input_vals = [1, 2, 2]
        x = 3
        head = self._list_to_linked(input_vals)
        expected = [1, 2, 2]

        # Act
        result_head = partition_list(head, x)

        # Assert
        self.assertEqual(self._linked_to_list(result_head), expected)

    def test_boundary_all_nodes_greater_or_equal(self):
        # Arrange
        input_vals = [4, 5, 6]
        x = 4
        head = self._list_to_linked(input_vals)
        expected = [4, 5, 6]

        # Act
        result_head = partition_list(head, x)

        # Assert
        self.assertEqual(self._linked_to_list(result_head), expected)

    def test_invalid_x_type(self):
        # Arrange
        head = self._list_to_linked([1, 2, 3])
        x = "2"  # invalid type

        # Act & Assert
        with self.assertRaises(TypeError):
            partition_list(head, x)

    def test_invalid_head_type(self):
        # Arrange
        head = "not_a_node"
        x = 2

        # Act & Assert
        with self.assertRaises(AttributeError):
            partition_list(head, x)