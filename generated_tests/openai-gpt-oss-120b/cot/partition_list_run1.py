import unittest
import random

class TestPartitionList(unittest.TestCase):
    def list_to_linked(self, lst):
        head = None
        prev = None
        for val in lst:
            node = ListNode(val)
            if head is None:
                head = node
            else:
                prev.next = node
            prev = node
        return head

    def linked_to_list(self, head):
        result = []
        cur = head
        while cur:
            result.append(cur.val)
            cur = cur.next
        return result

    def test_partition_mixed(self):
        head = self.list_to_linked([1, 4, 3, 2, 5, 2])
        new_head = partition_list(head, 3)
        self.assertEqual(self.linked_to_list(new_head), [1, 2, 2, 4, 3, 5])

    def test_all_less(self):
        head = self.list_to_linked([1, 2, 2])
        new_head = partition_list(head, 3)
        self.assertEqual(self.linked_to_list(new_head), [1, 2, 2])

    def test_all_greater_or_equal(self):
        head = self.list_to_linked([3, 4, 5])
        new_head = partition_list(head, 3)
        self.assertEqual(self.linked_to_list(new_head), [3, 4, 5])

    def test_empty_list(self):
        new_head = partition_list(None, 5)
        self.assertIsNone(new_head)

    def test_single_node_less(self):
        head = self.list_to_linked([1])
        new_head = partition_list(head, 2)
        self.assertEqual(self.linked_to_list(new_head), [1])

    def test_single_node_greater_or_equal(self):
        head = self.list_to_linked([2])
        new_head = partition_list(head, 2)
        self.assertEqual(self.linked_to_list(new_head), [2])

    def test_negative_and_zero(self):
        head = self.list_to_linked([-1, 0, 1, 2])
        new_head = partition_list(head, 0)
        self.assertEqual(self.linked_to_list(new_head), [-1, 0, 1, 2])

    def test_large_random(self):
        values = list(range(100))
        random.shuffle(values)
        head = self.list_to_linked(values)
        x = 50
        new_head = partition_list(head, x)

        # Verify ordering property
        seen_ge = False
        cur = new_head
        while cur:
            if cur.val >= x:
                seen_ge = True
            else:
                self.assertFalse(seen_ge, "Found a value < x after a value >= x")
            cur = cur.next

        # Verify stability (relative order within partitions)
        before = [v for v in values if v < x]
        after = [v for v in values if v >= x]
        self.assertEqual(self.linked_to_list(new_head), before + after)

    def test_invalid_head_type(self):
        with self.assertRaises(AttributeError):
            partition_list(123, 5)  # head is not a ListNode

    def test_invalid_x_type(self):
        head = self.list_to_linked([1, 2, 3])
        # The function does not explicitly type‑check x, but using a non‑int will cause a TypeError
        # when comparing node.val < x. We assert that this error propagates.
        with self.assertRaises(TypeError):
            partition_list(head, "a")