import unittest

class TestPartitionList(unittest.TestCase):
    def test_empty_list(self):
        result = partition_list(None, 3)
        self.assertIsNone(result)
    
    def test_single_node_less_than_x(self):
        head = ListNode(1)
        result = partition_list(head, 3)
        self.assertEqual(result.val, 1)
        self.assertIsNone(result.next)
    
    def test_single_node_greater_than_x(self):
        head = ListNode(5)
        result = partition_list(head, 3)
        self.assertEqual(result.val, 5)
        self.assertIsNone(result.next)
    
    def test_all_less_than_x(self):
        head = ListNode(1, ListNode(2, ListNode(3)))
        result = partition_list(head, 5)
        values = []
        while result:
            values.append(result.val)
            result = result.next
        self.assertEqual(values, [1, 2, 3])
    
    def test_all_greater_than_x(self):
        head = ListNode(4, ListNode(5, ListNode(6)))
        result = partition_list(head, 3)
        values = []
        while result:
            values.append(result.val)
            result = result.next
        self.assertEqual(values, [4, 5, 6])
    
    def test_mixed_values(self):
        head = ListNode(1, ListNode(4, ListNode(3, ListNode(2, ListNode(5, ListNode(2))))))
        result = partition_list(head, 3)
        values = []
        while result:
            values.append(result.val)
            result = result.next
        self.assertEqual(values, [1, 2, 2, 4, 3, 5])
    
    def test_x_in_middle(self):
        head = ListNode(3, ListNode(1, ListNode(2, ListNode(4, ListNode(5)))))
        result = partition_list(head, 3)
        values = []
        while result:
            values.append(result.val)
            result = result.next
        self.assertEqual(values, [1, 2, 3, 4, 5])
    
    def test_duplicate_values(self):
        head = ListNode(2, ListNode(2, ListNode(2)))
        result = partition_list(head, 3)
        values = []
        while result:
            values.append(result.val)
            result = result.next
        self.assertEqual(values, [2, 2, 2])