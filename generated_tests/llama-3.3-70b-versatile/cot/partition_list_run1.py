class TestPartitionList:
    def test_normal_case(self):
        # Create a linked list: 1 -> 4 -> 3 -> 2 -> 5 -> 2
        head = ListNode(1)
        head.next = ListNode(4)
        head.next.next = ListNode(3)
        head.next.next.next = ListNode(2)
        head.next.next.next.next = ListNode(5)
        head.next.next.next.next.next = ListNode(2)

        # Partition the list at x = 3
        result = partition_list(head, 3)

        # Expected output: 1 -> 2 -> 2 -> 4 -> 3 -> 5
        expected = ListNode(1)
        expected.next = ListNode(2)
        expected.next.next = ListNode(2)
        expected.next.next.next = ListNode(4)
        expected.next.next.next.next = ListNode(3)
        expected.next.next.next.next.next = ListNode(5)

        while result and expected:
            assert result.val == expected.val
            result = result.next
            expected = expected.next
        assert result is None and expected is None

    def test_empty_list(self):
        assert partition_list(None, 5) is None

    def test_single_node_list(self):
        head = ListNode(1)
        result = partition_list(head, 5)
        assert result.val == 1
        assert result.next is None

    def test_x_zero(self):
        head = ListNode(1)
        head.next = ListNode(4)
        head.next.next = ListNode(3)
        result = partition_list(head, 0)
        assert result.val == 1
        assert result.next.val == 4
        assert result.next.next.val == 3
        assert result.next.next.next is None

    def test_x_large(self):
        head = ListNode(1)
        head.next = ListNode(4)
        head.next.next = ListNode(3)
        result = partition_list(head, 10)
        assert result.val == 1
        assert result.next.val == 4
        assert result.next.next.val == 3
        assert result.next.next.next is None

    def test_x_equal_to_node_value(self):
        head = ListNode(1)
        head.next = ListNode(4)
        head.next.next = ListNode(3)
        result = partition_list(head, 3)
        assert result.val == 1
        assert result.next is None
        assert result.next is None

    def test_all_nodes_less_than_x(self):
        head = ListNode(1)
        head.next = ListNode(2)
        head.next.next = ListNode(3)
        result = partition_list(head, 10)
        assert result.val == 1
        assert result.next.val == 2
        assert result.next.next.val == 3
        assert result.next.next.next is None

    def test_all_nodes_greater_than_x(self):
        head = ListNode(5)
        head.next = ListNode(6)
        head.next.next = ListNode(7)
        result = partition_list(head, 3)
        assert result is None
        assert result is None

    def test_x_negative(self):
        head = ListNode(1)
        head.next = ListNode(4)
        head.next.next = ListNode(3)
        result = partition_list(head, -1)
        assert result.val == 1
        assert result.next.val == 4
        assert result.next.next.val == 3
        assert result.next.next.next is None