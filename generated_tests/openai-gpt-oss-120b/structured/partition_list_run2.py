import unittest

class TestPartitionList(unittest.TestCase):
    """Test suite for the partition_list function."""

    # Helper methods ---------------------------------------------------------
    def _list_to_linked(self, values):
        """Arrange: Convert a Python list to a linked list of ListNode."""
        dummy = ListNode(0)
        current = dummy
        for val in values:
            current.next = ListNode(val)
            current = current.next
        return dummy.next

    def _linked_to_list(self, head):
        """Assert: Convert a linked list back to a Python list."""
        result = []
        current = head
        while current:
            result.append(current.val)
            current = current.next
        return result

    # Normal case ------------------------------------------------------------
    def test_normal_mixed_values(self):
        # Arrange
        head = self._list_to_linked([1, 4, 3, 2, 5, 2])
        x = 3

        # Act
        new_head = partition_list(head, x)

        # Assert
        self.assertEqual(self._linked_to_list(new_head), [1, 2, 2, 4, 3, 5])

    # Boundary cases ---------------------------------------------------------
    def test_all_nodes_less_than_x(self):
        # Arrange
        head = self._list_to_linked([1, 2, 2])
        x = 5

        # Act
        new_head = partition_list(head, x)

        # Assert
        self.assertEqual(self._linked_to_list(new_head), [1, 2, 2])

    def test_all_nodes_greater_or_equal_x(self):
        # Arrange
        head = self._list_to_linked([5, 6, 7])
        x = 5

        # Act
        new_head = partition_list(head, x)

        # Assert
        self.assertEqual(self._linked_to_list(new_head), [5, 6, 7])

    def test_empty_list(self):
        # Arrange
        head = None
        x = 1

        # Act
        new_head = partition_list(head, x)

        # Assert
        self.assertIsNone(new_head)

    def test_single_node_less_than_x(self):
        # Arrange
        head = self._list_to_linked([0])
        x = 1

        # Act
        new_head = partition_list(head, x)

        # Assert
        self.assertEqual(self._linked_to_list(new_head), [0])

    def test_single_node_equal_to_x(self):
        # Arrange
        head = self._list_to_linked([3])
        x = 3

        # Act
        new_head = partition_list(head, x)

        # Assert
        self.assertEqual(self._linked_to_list(new_head), [3])

    def test_duplicate_values_around_x(self):
        # Arrange
        head = self._list_to_linked([2, 2, 3, 3, 1, 1])
        x = 2

        # Act
        new_head = partition_list(head, x)

        # Assert
        self.assertEqual(self._linked_to_list(new_head), [1, 1, 2, 2, 3, 3])

    # Invalid input cases ----------------------------------------------------
    def test_invalid_head_type_raises_attribute_error(self):
        # Arrange
        head = 123  # Not a ListNode
        x = 2

        # Act & Assert
        with self.assertRaises(AttributeError):
            partition_list(head, x)

    def test_invalid_x_type_raises_type_error(self):
        # Arrange
        head = self._list_to_linked([1, 2, 3])
        x = "a"  # Non‑int comparator

        # Act & Assert
        with self.assertRaises(TypeError):
            partition_list(head, x)