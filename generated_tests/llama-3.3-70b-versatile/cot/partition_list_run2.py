class TestPartitionList:
    def test_normal_case(self):
        # Create a linked list: 1 -> 4 -> 3 -> 2 -> 5 -> 2
        head = ListNode(1)
        head.next = ListNode(4)
        head.next.next = ListNode(3)
        head.next.next.next = ListNode(2)
        head.next.next.next.next = ListNode(5)
        head.next.next.next.next.next = ListNode(2)

        # Partition the list with x = 3
        result = partition_list(head, 3)

        # Expected result: 1 -> 2 -> 2 -> 4 -> 3 -> 5
        expected = ListNode(1)
        expected.next = ListNode(2)
        expected.next.next = ListNode(2)
        expected.next.next.next = ListNode(4)
        expected.next.next.next.next = ListNode(3)
        expected.next.next.next.next.next = ListNode(5)

        # Compare the result with the expected result
        while result and expected:
            assert result.val == expected.val
            result = result.next
            expected = expected.next
        assert result is None and expected is None

    def test_empty_list(self):
        # Partition an empty list
        result = partition_list(None, 5)
        assert result is None

    def test_single_element_list(self):
        # Create a linked list with a single element: 5
        head = ListNode(5)

        # Partition the list with x = 3
        result = partition_list(head, 3)

        # Expected result: 5
        expected = ListNode(5)

        # Compare the result with the expected result
        assert result.val == expected.val
        assert result.next is None

    def test_all_elements_less_than_x(self):
        # Create a linked list: 1 -> 2 -> 3
        head = ListNode(1)
        head.next = ListNode(2)
        head.next.next = ListNode(3)

        # Partition the list with x = 5
        result = partition_list(head, 5)

        # Expected result: 1 -> 2 -> 3
        expected = ListNode(1)
        expected.next = ListNode(2)
        expected.next.next = ListNode(3)

        # Compare the result with the expected result
        while result and expected:
            assert result.val == expected.val
            result = result.next
            expected = expected.next
        assert result is None and expected is None

    def test_all_elements_greater_than_x(self):
        # Create a linked list: 5 -> 6 -> 7
        head = ListNode(5)
        head.next = ListNode(6)
        head.next.next = ListNode(7)

        # Partition the list with x = 3
        result = partition_list(head, 3)

        # Expected result: 5 -> 6 -> 7
        expected = ListNode(5)
        expected.next = ListNode(6)
        expected.next.next = ListNode(7)

        # Compare the result with the expected result
        while result and expected:
            assert result.val == expected.val
            result = result.next
            expected = expected.next
        assert result is None and expected is None

    def test_x_is_none(self):
        # Create a linked list: 1 -> 2 -> 3
        head = ListNode(1)
        head.next = ListNode(2)
        head.next.next = ListNode(3)

        # Partition the list with x = None
        with assert_raises(TypeError):
            partition_list(head, None)

    def test_head_is_none(self):
        # Partition an empty list
        result = partition_list(None, 5)
        assert result is None