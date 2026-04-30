class TestPartitionList(unittest.TestCase):

    def test_empty_list(self):
        self.assertIsNone(partition_list(None, 5))

    def test_single_element_less_than_x(self):
        head = ListNode(3)
        result = partition_list(head, 5)
        self.assertEqual(result.val, 3)
        self.assertIsNone(result.next)

    def test_single_element_greater_than_x(self):
        head = ListNode(7)
        result = partition_list(head, 5)
        self.assertEqual(result.val, 7)
        self.assertIsNone(result.next)

    def test_multiple_elements_all_less_than_x(self):
        head = ListNode(1, ListNode(2, ListNode(3)))
        result = partition_list(head, 5)
        self.assertEqual(result.val, 1)
        self.assertEqual(result.next.val, 2)
        self.assertEqual(result.next.next.val, 3)
        self.assertIsNone(result.next.next.next)

    def test_multiple_elements_all_greater_than_x(self):
        head = ListNode(7, ListNode(8, ListNode(9)))
        result = partition_list(head, 5)
        self.assertEqual(result.val, 7)
        self.assertEqual(result.next.val, 8)
        self.assertEqual(result.next.next.val, 9)
        self.assertIsNone(result.next.next.next)

    def test_multiple_elements_mixed(self):
        head = ListNode(1, ListNode(4, ListNode(3, ListNode(2, ListNode(5, ListNode(2))))))
        result = partition_list(head, 3)
        self.assertEqual(result.val, 1)
        self.assertEqual(result.next.val, 2)
        self.assertEqual(result.next.next.val, 2)
        self.assertEqual(result.next.next.next.val, 4)
        self.assertEqual(result.next.next.next.next.val, 3)
        self.assertEqual(result.next.next.next.next.next.val, 5)
        self.assertIsNone(result.next.next.next.next.next.next)

    def test_x_in_the_middle(self):
        head = ListNode(1, ListNode(4, ListNode(3, ListNode(2, ListNode(5, ListNode(2))))))
        result = partition_list(head, 3)
        self.assertEqual(result.val, 1)
        self.assertEqual(result.next.val, 2)
        self.assertEqual(result.next.next.val, 2)
        self.assertEqual(result.next.next.next.val, 4)
        self.assertEqual(result.next.next.next.next.val, 3)
        self.assertEqual(result.next.next.next.next.next.val, 5)
        self.assertIsNone(result.next.next.next.next.next.next)