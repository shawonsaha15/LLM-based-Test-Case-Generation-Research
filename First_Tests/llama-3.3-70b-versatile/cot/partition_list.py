class ListNode:
    def __init__(self, val: int = 0, next: 'ListNode' = None):
        self.val = val
        self.next = next


def partition_list(head: ListNode, x: int) -> ListNode:
    before_head = ListNode(0)
    after_head = ListNode(0)

    before = before_head
    after = after_head

    current = head

    while current:
        if current.val < x:
            before.next = current
            before = current
        else:
            after.next = current
            after = current
        current = current.next

    after.next = None
    before.next = after_head.next

    return before_head.next

import unittest

class TestPartitionList(unittest.TestCase):

    def test_normal_input(self):
        head = ListNode(1, ListNode(4, ListNode(3, ListNode(2, ListNode(5, ListNode(2))))))
        result = partition_list(head, 3)
        expected = [1, 2, 2, 4, 3, 5]
        current = result
        for val in expected:
            self.assertEqual(current.val, val)
            current = current.next

    def test_all_less_than_x(self):
        head = ListNode(1, ListNode(2, ListNode(3)))
        result = partition_list(head, 4)
        expected = [1, 2, 3]
        current = result
        for val in expected:
            self.assertEqual(current.val, val)
            current = current.next

    def test_all_greater_than_x(self):
        head = ListNode(4, ListNode(5, ListNode(6)))
        result = partition_list(head, 3)
        expected = [4, 5, 6]
        current = result
        for val in expected:
            self.assertEqual(current.val, val)
            current = current.next

    def test_empty_list(self):
        result = partition_list(None, 3)
        self.assertIsNone(result)

    def test_single_element_list(self):
        head = ListNode(1)
        result = partition_list(head, 3)
        self.assertEqual(result.val, 1)
        self.assertIsNone(result.next)

    def test_x_is_zero(self):
        head = ListNode(1, ListNode(2, ListNode(3)))
        result = partition_list(head, 0)
        expected = [1, 2, 3]
        current = result
        for val in expected:
            self.assertEqual(current.val, val)
            current = current.next

if __name__ == '__main__':
    unittest.main()