class TestPartitionList(unittest.TestCase):
    def test_partition_with_middle_value(self):
        # Create a linked list: 1 -> 4 -> 3 -> 2 -> 5 -> 2
        head = ListNode(1)
        head.next = ListNode(4)
        head.next.next = ListNode(3)
        head.next.next.next = ListNode(2)
        head.next.next.next.next = ListNode(5)
        head.next.next.next.next.next = ListNode(2)

        result = partition_list(head, 3)

        # Expected result: 1 -> 2 -> 2 -> 4 -> 3 -> 5
        expected = [1, 2, 2, 4, 3, 5]
        actual = []
        current = result
        while current:
            actual.append(current.val)
            current = current.next
        self.assertEqual(actual, expected)

    def test_partition_with_large_value(self):
        # Create a linked list: 1 -> 2 -> 3 -> 4 -> 5
        head = ListNode(1)
        head.next = ListNode(2)
        head.next.next = ListNode(3)
        head.next.next.next = ListNode(4)
        head.next.next.next.next = ListNode(5)

        result = partition_list(head, 6)

        # Expected result: 1 -> 2 -> 3 -> 4 -> 5
        expected = [1, 2, 3, 4, 5]
        actual = []
        current = result
        while current:
            actual.append(current.val)
            current = current.next
        self.assertEqual(actual, expected)

    def test_partition_with_small_value(self):
        # Create a linked list: 1 -> 2 -> 3 -> 4 -> 5
        head = ListNode(1)
        head.next = ListNode(2)
        head.next.next = ListNode(3)
        head.next.next.next = ListNode(4)
        head.next.next.next.next = ListNode(5)

        result = partition_list(head, 0)

        # Expected result: 1 -> 2 -> 3 -> 4 -> 5
        expected = [1, 2, 3, 4, 5]
        actual = []
        current = result
        while current:
            actual.append(current.val)
            current = current.next
        self.assertEqual(actual, expected)

    def test_empty_list(self):
        result = partition_list(None, 5)
        self.assertIsNone(result)

    def test_single_element_list(self):
        head = ListNode(5)
        result = partition_list(head, 3)
        self.assertEqual(result.val, 5)
        self.assertIsNone(result.next)