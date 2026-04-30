class TestPartitionList(unittest.TestCase):
    def test_partition_list_with_x_in_middle(self):
        # Create linked list: 1 -> 4 -> 3 -> 2 -> 5 -> 2
        head = ListNode(1)
        head.next = ListNode(4)
        head.next.next = ListNode(3)
        head.next.next.next = ListNode(2)
        head.next.next.next.next = ListNode(5)
        head.next.next.next.next.next = ListNode(2)

        result = partition_list(head, 3)
        expected = [1, 2, 2, 4, 3, 5]
        actual = []
        while result:
            actual.append(result.val)
            result = result.next
        self.assertEqual(actual, expected)

    def test_partition_list_with_x_at_head(self):
        # Create linked list: 5 -> 1 -> 2 -> 3 -> 4 -> 5
        head = ListNode(5)
        head.next = ListNode(1)
        head.next.next = ListNode(2)
        head.next.next.next = ListNode(3)
        head.next.next.next.next = ListNode(4)
        head.next.next.next.next.next = ListNode(5)

        result = partition_list(head, 5)
        expected = [1, 2, 3, 4, 5, 5]
        actual = []
        while result:
            actual.append(result.val)
            result = result.next
        self.assertEqual(actual, expected)

    def test_partition_list_with_x_at_tail(self):
        # Create linked list: 1 -> 2 -> 3 -> 4 -> 5
        head = ListNode(1)
        head.next = ListNode(2)
        head.next.next = ListNode(3)
        head.next.next.next = ListNode(4)
        head.next.next.next.next = ListNode(5)

        result = partition_list(head, 6)
        expected = [1, 2, 3, 4, 5]
        actual = []
        while result:
            actual.append(result.val)
            result = result.next
        self.assertEqual(actual, expected)

    def test_partition_list_with_empty_list(self):
        result = partition_list(None, 5)
        self.assertIsNone(result)

    def test_partition_list_with_single_element_list(self):
        head = ListNode(1)
        result = partition_list(head, 5)
        self.assertEqual(result.val, 1)
        self.assertIsNone(result.next)