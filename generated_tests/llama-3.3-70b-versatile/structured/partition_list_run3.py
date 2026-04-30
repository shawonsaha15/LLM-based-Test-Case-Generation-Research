class TestPartitionList(unittest.TestCase):
    def test_normal_case(self):
        # Arrange
        head = ListNode(1, ListNode(4, ListNode(3, ListNode(2, ListNode(5, ListNode(2))))))
        x = 3

        # Act
        result = partition_list(head, x)

        # Assert
        expected = [1, 2, 2, 4, 3, 5]
        current = result
        for val in expected:
            self.assertEqual(current.val, val)
            current = current.next
        self.assertIsNone(current)

    def test_boundary_case_equal(self):
        # Arrange
        head = ListNode(1, ListNode(4, ListNode(3, ListNode(2, ListNode(5, ListNode(2))))))
        x = 1

        # Act
        result = partition_list(head, x)

        # Assert
        expected = [1, 4, 3, 2, 5, 2]
        current = result
        for val in expected:
            self.assertEqual(current.val, val)
            current = current.next
        self.assertIsNone(current)

    def test_boundary_case_greater(self):
        # Arrange
        head = ListNode(1, ListNode(4, ListNode(3, ListNode(2, ListNode(5, ListNode(2))))))
        x = 6

        # Act
        result = partition_list(head, x)

        # Assert
        expected = [1, 4, 3, 2, 5, 2]
        current = result
        for val in expected:
            self.assertEqual(current.val, val)
            current = current.next
        self.assertIsNone(current)

    def test_invalid_input_head_none(self):
        # Arrange
        head = None
        x = 3

        # Act
        result = partition_list(head, x)

        # Assert
        self.assertIsNone(result)

    def test_invalid_input_x_none(self):
        # Arrange
        head = ListNode(1, ListNode(4, ListNode(3, ListNode(2, ListNode(5, ListNode(2))))))
        x = None

        # Act and Assert
        with self.assertRaises(TypeError):
            partition_list(head, x)

    def test_single_node(self):
        # Arrange
        head = ListNode(1)
        x = 3

        # Act
        result = partition_list(head, x)

        # Assert
        self.assertEqual(result.val, 1)
        self.assertIsNone(result.next)

    def test_all_nodes_greater_than_x(self):
        # Arrange
        head = ListNode(4, ListNode(5, ListNode(6)))
        x = 3

        # Act
        result = partition_list(head, x)

        # Assert
        expected = [4, 5, 6]
        current = result
        for val in expected:
            self.assertEqual(current.val, val)
            current = current.next
        self.assertIsNone(current)

    def test_all_nodes_less_than_x(self):
        # Arrange
        head = ListNode(1, ListNode(2, ListNode(3)))
        x = 4

        # Act
        result = partition_list(head, x)

        # Assert
        expected = [1, 2, 3]
        current = result
        for val in expected:
            self.assertEqual(current.val, val)
            current = current.next
        self.assertIsNone(current)