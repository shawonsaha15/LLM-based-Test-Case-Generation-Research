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

class TestPartitionList:
    def test_normal_cases(self):
        # Test case 1: List with numbers less than x
        head = ListNode(1, ListNode(4, ListNode(3, ListNode(2, ListNode(5)))))
        x = 3
        result = partition_list(head, x)
        self.assertEqual(result.val, 1)
        self.assertEqual(result.next.val, 2)
        self.assertEqual(result.next.next.val, 3)
        self.assertEqual(result.next.next.next.val, 4)
        self.assertEqual(result.next.next.next.next.val, 5)
        self.assertEqual(result.next.next.next.next.next, None)

        # Test case 2: List with numbers greater than x
        head = ListNode(7, ListNode(9, ListNode(1, ListNode(4, ListNode(5)))))
        x = 5
        result = partition_list(head, x)
        self.assertEqual(result.val, 7)
        self.assertEqual(result.next.val, 9)
        self.assertEqual(result.next.next.val, 1)
        self.assertEqual(result.next.next.next.val, 4)
        self.assertEqual(result.next.next.next.next.val, 5)
        self.assertEqual(result.next.next.next.next.next, None)

        # Test case 3: List with numbers equal to x
        head = ListNode(3, ListNode(3, ListNode(3, ListNode(3, ListNode(3)))))
        x = 3
        result = partition_list(head, x)
        self.assertEqual(result.val, 3)
        self.assertEqual(result.next.val, 3)
        self.assertEqual(result.next.next.val, 3)
        self.assertEqual(result.next.next.next.val, 3)
        self.assertEqual(result.next.next.next.next.val, 3)
        self.assertEqual(result.next.next.next.next.next, None)

    def test_edge_cases(self):
        # Test case 1: Empty list
        head = None
        x = 5
        result = partition_list(head, x)
        self.assertEqual(result, None)

        # Test case 2: List with one node
        head = ListNode(5)
        x = 5
        result = partition_list(head, x)
        self.assertEqual(result.val, 5)
        self.assertEqual(result.next, None)

        # Test case 3: List with one node and x is the value of the node
        head = ListNode(5)
        x = 5
        result = partition_list(head, x)
        self.assertEqual(result.val, 5)
        self.assertEqual(result.next, None)

    def test_invalid_inputs(self):
        # Test case 1: x is not an integer
        head = ListNode(1, ListNode(4, ListNode(3, ListNode(2, ListNode(5)))))
        x = 'a'
        with self.assertRaises(TypeError):
            partition_list(head, x)

        # Test case 2: x is a negative number
        head = ListNode(1, ListNode(4, ListNode(3, ListNode(2, ListNode(5)))))
        x = -3
        result = partition_list(head, x)
        self.assertEqual(result.val, 1)
        self.assertEqual(result.next.val, 4)
        self.assertEqual(result.next.next.val, 3)
        self.assertEqual(result.next.next.next.val, 2)
        self.assertEqual(result.next.next.next.next.val, 5)
        self.assertEqual(result.next.next.next.next.next, None)

if __name__ == "__main__":
    unittest.main()