class TestPartitionList:
    def test_normal_case(self, partition_list):
        # Arrange
        head = ListNode(1, ListNode(4, ListNode(3, ListNode(2, ListNode(5, ListNode(2))))))
        x = 3

        # Act
        result = partition_list(head, x)

        # Assert
        expected = [1, 2, 2, 4, 3, 5]
        current = result
        for val in expected:
            assert current.val == val
            current = current.next
        assert current is None

    def test_boundary_case_equal(self, partition_list):
        # Arrange
        head = ListNode(1, ListNode(2, ListNode(3)))
        x = 2

        # Act
        result = partition_list(head, x)

        # Assert
        expected = [1, 2, 3]
        current = result
        for val in expected:
            assert current.val == val
            current = current.next
        assert current is None

    def test_boundary_case_less(self, partition_list):
        # Arrange
        head = ListNode(1, ListNode(2, ListNode(3)))
        x = 1

        # Act
        result = partition_list(head, x)

        # Assert
        expected = [1, 2, 3]
        current = result
        for val in expected:
            assert current.val == val
            current = current.next
        assert current is None

    def test_boundary_case_greater(self, partition_list):
        # Arrange
        head = ListNode(1, ListNode(2, ListNode(3)))
        x = 4

        # Act
        result = partition_list(head, x)

        # Assert
        expected = [1, 2, 3]
        current = result
        for val in expected:
            assert current.val == val
            current = current.next
        assert current is None

    def test_invalid_input_empty_list(self, partition_list):
        # Arrange
        head = None
        x = 3

        # Act
        result = partition_list(head, x)

        # Assert
        assert result is None

    def test_invalid_input_single_element_less(self, partition_list):
        # Arrange
        head = ListNode(1)
        x = 3

        # Act
        result = partition_list(head, x)

        # Assert
        expected = [1]
        current = result
        for val in expected:
            assert current.val == val
            current = current.next
        assert current is None

    def test_invalid_input_single_element_greater(self, partition_list):
        # Arrange
        head = ListNode(3)
        x = 1

        # Act
        result = partition_list(head, x)

        # Assert
        expected = [3]
        current = result
        for val in expected:
            assert current.val == val
            current = current.next
        assert current is None