class TestPartitionList(unittest.TestCase):

    def test_normal_case(self):
        # Arrange
        head = ListNode(1, ListNode(4, ListNode(3, ListNode(2, ListNode(5, ListNode(2))))))
        x = 3

        # Act
        result = partition_list(head, x)

        # Assert
        expected = [1, 2, 2, 4, 3, 5]
        actual = []
        current = result
        while current:
            actual.append(current.val)
            current = current.next
        self.assertEqual(actual, expected)

    def test_boundary_case_all_less(self):
        # Arrange
        head = ListNode(1, ListNode(2, ListNode(3)))
        x = 4

        # Act
        result = partition_list(head, x)

        # Assert
        expected = [1, 2, 3]
        actual = []
        current = result
        while current:
            actual.append(current.val)
            current = current.next
        self.assertEqual(actual, expected)

    def test_boundary_case_all_greater(self):
        # Arrange
        head = ListNode(4, ListNode(5, ListNode(6)))
        x = 3

        # Act
        result = partition_list(head, x)

        # Assert
        expected = [4, 5, 6]
        actual = []
        current = result
        while current:
            actual.append(current.val)
            current = current.next
        self.assertEqual(actual, expected)

    def test_invalid_input_none(self):
        # Arrange
        head = None
        x = 3

        # Act
        result = partition_list(head, x)

        # Assert
        self.assertIsNone(result)

    def test_invalid_input_empty_list(self):
        # Arrange
        head = ListNode(0)
        x = 3

        # Act
        result = partition_list(head, x)

        # Assert
        expected = [0]
        actual = []
        current = result
        while current:
            actual.append(current.val)
            current = current.next
        self.assertEqual(actual, expected)

    def test_invalid_input_x_none(self):
        # Arrange
        head = ListNode(1, ListNode(2, ListNode(3)))
        x = None

        # Act and Assert
        with self.assertRaises(TypeError):
            partition_list(head, x)