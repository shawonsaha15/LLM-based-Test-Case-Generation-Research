class TestPartitionList(unittest.TestCase):
    def test_empty_list(self):
        result = partition_list(None, 5)
        self.assertIsNone(result)
    
    def test_single_node_less_than_x(self):
        head = ListNode(3)
        result = partition_list(head, 5)
        self.assertEqual(result.val, 3)
        self.assertIsNone(result.next)
    
    def test_single_node_greater_equal_x(self):
        head = ListNode(7)
        result = partition_list(head, 5)
        self.assertEqual(result.val, 7)
        self.assertIsNone(result.next)
    
    def test_all_less_than_x(self):
        head = ListNode(1, ListNode(2, ListNode(3)))
        result = partition_list(head, 5)
        vals = []
        while result:
            vals.append(result.val)
            result = result.next
        self.assertEqual(vals, [1, 2, 3])
    
    def test_all_greater_equal_x(self):
        head = ListNode(5, ListNode(6, ListNode(7)))
        result = partition_list(head, 5)
        vals = []
        while result:
            vals.append(result.val)
            result = result.next
        self.assertEqual(vals, [5, 6, 7])
    
    def test_mixed_values(self):
        head = ListNode(1, ListNode(4, ListNode(3, ListNode(2, ListNode(5, ListNode(2))))))
        result = partition_list(head, 3)
        vals = []
        while result:
            vals.append(result.val)
            result = result.next
        self.assertEqual(vals, [1, 2, 2, 4, 3, 5])
    
    def test_duplicates_around_x(self):
        head = ListNode(3, ListNode(1, ListNode(3, ListNode(2, ListNode(3)))))
        result = partition_list(head, 3)
        vals = []
        while result:
            vals.append(result.val)
            result = result.next
        self.assertEqual(vals, [1, 2, 3, 3, 3])
    
    def test_x_in_middle(self):
        head = ListNode(2, ListNode(1, ListNode(4, ListNode(3))))
        result = partition_list(head, 3)
        vals = []
        while result:
            vals.append(result.val)
            result = result.next
        self.assertEqual(vals, [2, 1, 4, 3])