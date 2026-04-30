class TestPartitionList(unittest.TestCase):

    def test_normal_input(self):
        # Create a linked list: 1 -> 4 -> 3 -> 2 -> 5 -> 2
        head = ListNode(1)
        head.next = ListNode(4)
        head.next.next = ListNode(3)
        head.next.next.next = ListNode(2)
        head.next.next.next.next = ListNode(5)
        head.next.next.next.next.next = ListNode(2)

        # Partition the list with x = 3
        result = partition_list(head, 3)

        # Expected output: 1 -> 2 -> 2 -> 4 -> 3 -> 5
        expected = ListNode(1)
        expected.next = ListNode(2)
        expected.next.next = ListNode(2)
        expected.next.next.next = ListNode(4)
        expected.next.next.next.next = ListNode(3)
        expected.next.next.next.next.next = ListNode(5)

        # Compare the result with the expected output
        while result and expected:
            self.assertEqual(result.val, expected.val)
            result = result.next
            expected = expected.next
        self.assertIsNone(result)
        self.assertIsNone(expected)

    def test_empty_input(self):
        # Test with an empty linked list
        self.assertIsNone(partition_list(None, 5))

    def test_single_node(self):
        # Test with a single node linked list
        head = ListNode(5)
        result = partition_list(head, 3)
        self.assertEqual(result.val, 5)

    def test_all_nodes_less_than_x(self):
        # Create a linked list: 1 -> 2 -> 3
        head = ListNode(1)
        head.next = ListNode(2)
        head.next.next = ListNode(3)

        # Partition the list with x = 4
        result = partition_list(head, 4)

        # Expected output: 1 -> 2 -> 3
        expected = ListNode(1)
        expected.next = ListNode(2)
        expected.next.next = ListNode(3)

        # Compare the result with the expected output
        while result and expected:
            self.assertEqual(result.val, expected.val)
            result = result.next
            expected = expected.next
        self.assertIsNone(result)
        self.assertIsNone(expected)

    def test_all_nodes_greater_than_x(self):
        # Create a linked list: 5 -> 6 -> 7
        head = ListNode(5)
        head.next = ListNode(6)
        head.next.next = ListNode(7)

        # Partition the list with x = 3
        result = partition_list(head, 3)

        # Expected output: 5 -> 6 -> 7
        expected = ListNode(5)
        expected.next = ListNode(6)
        expected.next.next = ListNode(7)

        # Compare the result with the expected output
        while result and expected:
            self.assertEqual(result.val, expected.val)
            result = result.next
            expected = expected.next
        self.assertIsNone(result)
        self.assertIsNone(expected)

    def test_x_zero(self):
        # Create a linked list: 1 -> 2 -> 3
        head = ListNode(1)
        head.next = ListNode(2)
        head.next.next = ListNode(3)

        # Partition the list with x = 0
        result = partition_list(head, 0)

        # Expected output: 1 -> 2 -> 3
        expected = ListNode(1)
        expected.next = ListNode(2)
        expected.next.next = ListNode(3)

        # Compare the result with the expected output
        while result and expected:
            self.assertEqual(result.val, expected.val)
            result = result.next
            expected = expected.next
        self.assertIsNone(result)
        self.assertIsNone(expected)

    def test_x_large(self):
        # Create a linked list: 1 -> 2 -> 3
        head = ListNode(1)
        head.next = ListNode(2)
        head.next.next = ListNode(3)

        # Partition the list with x = 10
        result = partition_list(head, 10)

        # Expected output: 1 -> 2 -> 3
        expected = ListNode(1)
        expected.next = ListNode(2)
        expected.next.next = ListNode(3)

        # Compare the result with the expected output
        while result and expected:
            self.assertEqual(result.val, expected.val)
            result = result.next
            expected = expected.next
        self.assertIsNone(result)
        self.assertIsNone(expected)

    def test_invalid_input(self):
        # Test with invalid input (None as x)
        with self.assertRaises(TypeError):
            partition_list(ListNode(5), None)

    def test_large_input(self):
        # Create a large linked list
        head = ListNode(1)
        current = head
        for i in range(2, 1001):
            current.next = ListNode(i)
            current = current.next

        # Partition the list with x = 500
        result = partition_list(head, 500)

        # Count the number of nodes less than 500
        count = 0
        current = result
        while current and current.val < 500:
            count += 1
            current = current.next

        # Check if the number of nodes less than 500 is correct
        self.assertEqual(count, 499)