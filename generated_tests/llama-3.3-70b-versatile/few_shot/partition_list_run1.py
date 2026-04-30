class TestPartitionList(unittest.TestCase):
    def test_all_elements_less_than_x(self):
        head = ListNode(1, ListNode(2, ListNode(3)))
        result = partition_list(head, 4)
        expected = [1, 2, 3]
        current = result
        for val in expected:
            self.assertEqual(current.val, val)
            current = current.next
        self.assertIsNone(current)

    def test_all_elements_greater_than_x(self):
        head = ListNode(1, ListNode(2, ListNode(3)))
        result = partition_list(head, 0)
        expected = [1, 2, 3]
        current = result
        for val in expected:
            self.assertEqual(current.val, val)
            current = current.next
        self.assertIsNone(current)

    def test_mixed_elements(self):
        head = ListNode(1, ListNode(4, ListNode(3, ListNode(2, ListNode(5)))))
        result = partition_list(head, 3)
        expected = [1, 2, 4, 3, 5]
        current = result
        for val in expected:
            self.assertEqual(current.val, val)
            current = current.next
        self.assertIsNone(current)

    def test_empty_list(self):
        result = partition_list(None, 3)
        self.assertIsNone(result)

    def test_single_element_list(self):
        head = ListNode(1)
        result = partition_list(head, 3)
        self.assertEqual(result.val, 1)
        self.assertIsNone(result.next)

    def test_partition_at_head(self):
        head = ListNode(4, ListNode(1, ListNode(2, ListNode(3))))
        result = partition_list(head, 3)
        expected = [1, 2, 4, 3]
        current = result
        for val in expected:
            self.assertEqual(current.val, val)
            current = current.next
        self.assertIsNone(current)