import unittest

class TestPartitionList(unittest.TestCase):

    def list_to_array(self, head):
        """Helper to convert linked list to array for easy assertion."""
        result = []
        current = head
        while current:
            result.append(current.val)
            current = current.next
        return result

    def array_to_list(self, arr):
        """Helper to convert array to linked list."""
        if not arr:
            return None
        head = ListNode(arr[0])
        current = head
        for val in arr[1:]:
            current.next = ListNode(val)
            current = current.next
        return head

    # Normal cases
    def test_normal_case_mixed_values(self):
        # Arrange
        head = self.array_to_list([1, 4, 3, 2, 5, 2])
        x = 3
        # Act
        result = partition_list(head, x)
        # Assert
        self.assertEqual(self.list_to_array(result), [1, 2, 2, 4, 3, 5])

    def test_normal_case_all_less_than_x(self):
        # Arrange
        head = self.array_to_list([1, 2, 3])
        x = 5
        # Act
        result = partition_list(head, x)
        # Assert
        self.assertEqual(self.list_to_array(result), [1, 2, 3])

    def test_normal_case_all_greater_or_equal(self):
        # Arrange
        head = self.array_to_list([5, 6, 7])
        x = 5
        # Act
        result = partition_list(head, x)
        # Assert
        self.assertEqual(self.list_to_array(result), [5, 6, 7])

    # Boundary cases
    def test_boundary_empty_list(self):
        # Arrange
        head = None
        x = 3
        # Act
        result = partition_list(head, x)
        # Assert
        self.assertIsNone(result)

    def test_boundary_single_node_less_than_x(self):
        # Arrange
        head = self.array_to_list([2])
        x = 3
        # Act
        result = partition_list(head, x)
        # Assert
        self.assertEqual(self.list_to_array(result), [2])

    def test_boundary_single_node_greater_or_equal(self):
        # Arrange
        head = self.array_to_list([4])
        x = 3
        # Act
        result = partition_list(head, x)
        # Assert
        self.assertEqual(self.list_to_array(result), [4])

    def test_boundary_duplicate_values(self):
        # Arrange
        head = self.array_to_list([3, 3, 3])
        x = 3
        # Act
        result = partition_list(head, x)
        # Assert
        self.assertEqual(self.list_to_array(result), [3, 3, 3])

    def test_boundary_negative_values(self):
        # Arrange
        head = self.array_to_list([-1, -3, 2, 0])
        x = -1
        # Act
        result = partition_list(head, x)
        # Assert
        self.assertEqual(self.list_to_array(result), [-3, -1, 2, 0])

    # Invalid inputs (handled gracefully by function)
    def test_invalid_x_zero(self):
        # Arrange
        head = self.array_to_list([1, -1, 0, 2])
        x = 0
        # Act
        result = partition_list(head, x)
        # Assert
        self.assertEqual(self.list_to_array(result), [-1, 1, 0, 2])

    def test_invalid_x_negative(self):
        # Arrange
        head = self.array_to_list([1, 2, 3])
        x = -10
        # Act
        result = partition_list(head, x)
        # Assert
        self.assertEqual(self.list_to_array(result), [1, 2, 3])