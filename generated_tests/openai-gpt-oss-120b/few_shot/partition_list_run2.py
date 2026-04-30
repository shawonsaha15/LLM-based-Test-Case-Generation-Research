import unittest

class TestPartitionList(unittest.TestCase):
    def _list_to_linked(self, values):
        """Create a linked list from a Python list and return its head."""
        head = None
        prev = None
        for v in values:
            node = ListNode(v)
            if head is None:
                head = node
            else:
                prev.next = node
            prev = node
        return head

    def _linked_to_list(self, head):
        """Convert a linked list back to a Python list."""
        result = []
        cur = head
        while cur:
            result.append(cur.val)
            cur = cur.next
        return result

    def test_mixed_values(self):
        head = self._list_to_linked([1, 4, 3, 2, 5, 2])
        new_head = partition_list(head, 3)
        self.assertEqual(self._linked_to_list(new_head), [1, 2, 2, 4, 3, 5])

    def test_all_less_than_x(self):
        head = self._list_to_linked([1, 2, 2])
        new_head = partition_list(head, 3)
        self.assertEqual(self._linked_to_list(new_head), [1, 2, 2])

    def test_all_greater_or_equal_x(self):
        head = self._list_to_linked([3, 4, 5])
        new_head = partition_list(head, 3)
        self.assertEqual(self._linked_to_list(new_head), [3, 4, 5])

    def test_empty_list(self):
        new_head = partition_list(None, 0)
        self.assertIsNone(new_head)

    def test_single_node_less(self):
        head = self._list_to_linked([1])
        new_head = partition_list(head, 2)
        self.assertEqual(self._linked_to_list(new_head), [1])

    def test_single_node_greater_or_equal(self):
        head = self._list_to_linked([5])
        new_head = partition_list(head, 3)
        self.assertEqual(self._linked_to_list(new_head), [5])

    def test_preserve_relative_order(self):
        # Nodes < x keep original order, as do nodes >= x
        original = [2, 1, 3, 2, 4, 3]
        head = self._list_to_linked(original)
        new_head = partition_list(head, 3)
        # Expected: [2,1,2] (all <3) followed by [3,4,3] (>=3) preserving order
        self.assertEqual(self._linked_to_list(new_head), [2, 1, 2, 3, 4, 3])

    def test_last_node_next_is_none(self):
        head = self._list_to_linked([5, 1, 4, 2])
        new_head = partition_list(head, 3)
        # Traverse to the end and ensure .next is None
        cur = new_head
        while cur.next:
            cur = cur.next
        self.assertIsNone(cur.next)