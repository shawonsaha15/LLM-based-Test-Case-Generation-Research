import unittest


class TestPartitionList(unittest.TestCase):
    def list_to_array(self, head):
        """Convert linked list to array for easy comparison."""
        result = []
        current = head
        while current:
            result.append(current.val)
            current = current.next
        return result

    def array_to_list(self, arr):
        """Convert array to linked list."""
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
        head = self.array_to_list([1, 2, 2, 1])
        x = 3
        # Act
        result = partition_list(head, x)
        # Assert
        self.assertEqual(self.list_to_array(result), [1, 2, 2, 1])

    def test_normal_case_all_greater_or_equal_to_x(self):
        # Arrange
        head = self.array_to_list([4, 5, 6])
        x = 3
        # Act
        result = partition_list(head, x)
        # Assert
        self.assertEqual(self.list_to_array(result), [4, 5, 6])

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
        head = self.array_to_list([1])
        x = 2
        # Act
        result = partition_list(head, x)
        # Assert
        self.assertEqual(self.list_to_array(result), [1])

    def test_boundary_single_node_greater_or_equal_to_x(self):
        # Arrange
        head = self.array_to_list([2])
        x = 2
        # Act
        result = partition_list(head, x)
        # Assert
        self.assertEqual(self.list_to_array(result), [2])

    def test_boundary_two_nodes_already_partitioned(self):
        # Arrange
        head = self.array_to_list([1, 4])
        x = 3
        # Act
        result = partition_list(head, x)
        # Assert
        self.assertEqual(self.list_to_array(result), [1, 4])

    def test_boundary_two_nodes_reverse_partition(self):
        # Arrange
        head = self.array_to_list([4, 1])
        x = 3
        # Act
        result = partition_list(head, x)
        # Assert
        self.assertEqual(self.list_to_array(result), [1, 4])

    def test_boundary_duplicates_around_x(self):
        # Arrange
        head = self.array_to_list([3, 3, 3])
        x = 3
        # Act
        result = partition_list(head, x)
        # Assert
        self.assertEqual(self.list_to_array(result), [3, 3, 3])

    def test_boundary_negative_values(self):
        # Arrange
        head = self.array_to_list([-2, 5, -1, 3, 0])
        x = 0
        # Act
        result = partition_list(head, x)
        # Assert
        self.assertEqual(self.list_to_array(result), [-2, -1, 5, 3, 0])