class TestPartitionList(unittest.TestCase):
    def create_linked_list(self, values):
        dummy = ListNode(0)
        current = dummy
        for val in values:
            current.next = ListNode(val)
            current = current.next
        return dummy.next
    
    def linked_list_to_list(self, head):
        result = []
        current = head
        while current:
            result.append(current.val)
            current = current.next
        return result
    
    def test_empty_list(self):
        head = None
        result = partition_list(head, 3)
        self.assertIsNone(result)
    
    def test_single_node_less_than_x(self):
        head = self.create_linked_list([2])
        result = partition_list(head, 3)
        self.assertEqual(self.linked_list_to_list(result), [2])
    
    def test_single_node_greater_than_x(self):
        head = self.create_linked_list([4])
        result = partition_list(head, 3)
        self.assertEqual(self.linked_list_to_list(result), [4])
    
    def test_all_less_than_x(self):
        head = self.create_linked_list([1, 2])
        result = partition_list(head, 3)
        self.assertEqual(self.linked_list_to_list(result), [1, 2])
    
    def test_all_greater_than_x(self):
        head = self.create_linked_list([4, 5])
        result = partition_list(head, 3)
        self.assertEqual(self.linked_list_to_list(result), [4, 5])
    
    def test_mixed_values(self):
        head = self.create_linked_list([1, 4, 3, 2, 5, 2])
        result = partition_list(head, 3)
        self.assertEqual(self.linked_list_to_list(result), [1, 2, 2, 4, 3, 5])
    
    def test_duplicate_values(self):
        head = self.create_linked_list([3, 3, 3])
        result = partition_list(head, 3)
        self.assertEqual(self.linked_list_to_list(result), [3, 3, 3])
    
    def test_x_at_boundary(self):
        head = self.create_linked_list([2, 3, 4])
        result = partition_list(head, 3)
        self.assertEqual(self.linked_list_to_list(result), [2, 3, 4])