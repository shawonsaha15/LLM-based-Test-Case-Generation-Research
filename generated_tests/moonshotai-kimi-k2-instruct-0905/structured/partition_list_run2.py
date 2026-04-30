import unittest


class TestPartitionList(unittest.TestCase):

    def list_to_array(self, head):
        """Helper to convert linked list to Python list."""
        arr = []
        current = head
        while current:
            arr.append(current.val)
            current = current.next
        return arr

    def array_to_list(self, arr):
        """Helper to convert Python list to linked list."""
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
        expected = [1, 2, 2, 4, 3, 5]

        # Act
        result = partition_list(head, x)

        # Assert
        self.assertEqual(self.list_to_array(result), expected)

    def test_normal_case_all_less_than_x(self):
        # Arrange
        head = self.array_to_list([1, 2, 3])
        x = 5
        expected = [1, 2, 3]

        # Act
        result = partition_list(head, x)

        # Assert
        self.assertEqual(self.list_to_array(result), expected)

    def test_normal_case_all_greater_or_equal_x(self):
        # Arrange
        head = self.array_to_list([5, 6, 7])
        x = 5
        expected = [5, 6, 7]

        # Act
        result = partition_list(head, x)

        # Assert
        self.assertEqual(self.list_to_array(result), expected)

    # Boundary cases
    def test_boundary_empty_list(self):
        # Arrange
        head = None
        x = 3
        expected = []

        # Act
        result = partition_list(head, x)

        # Assert
        self.assertEqual(self.list_to_array(result), expected)

    def test_boundary_single_node_less_than_x(self):
        # Arrange
        head = self.array_to_list([1])
        x = 2
        expected = [1]

        # Act
        result = partition_list(head, x)

        # Assert
        self.assertEqual(self.list_to_array(result), expected)

    def test_boundary_single_node_greater_or_equal_x(self):
        # Arrange
        head = self.array_to_list([3])
        x = 2
        expected = [3]

        # Act
        result = partition_list(head, x)

        # Assert
        self.assertEqual(self.list_to_array(result), expected)

    def test_boundary_all_equal_to_x(self):
        # Arrange
        head = self.array_to_list([3, 3, 3])
        x = 3
        expected = [3, 3, 3]

        # Act
        result = partition_list(head, x)

        # Assert
        self.assertEqual(self.list_to_array(result), expected)

    def test_boundary_negative_values(self):
        # Arrange
        head = self.array_to_list([-1, -3, 2, 0, 5])
        x = 0
        expected = [-1, -3, 0, 2, 5]

        # Act
        result = partition_list(head, x)

        # Assert
        self.assertEqual(self.list_to_array(result), expected)

    # Invalid inputs (if applicable)
    def test_invalid_negative_x(self):
        # Arrange
        head = self.array_to_list([1, 2, 3])
        x = -5
        expected = [1, 2, 3]

        # Act
        result = partition_list(head, x)

        # Assert
        self.assertEqual(self.list_to_array(result), expected)

    def test_invalid_duplicate_values(self):
        # Arrange
        head = self.array_to_list([2, 2, 2])
        x = 2
        expected = [2, 2, 2]

        # Act
        result = partition_list(head, x)

        # Assert
        self.assertEqual(self.list_to_array(result), expected)