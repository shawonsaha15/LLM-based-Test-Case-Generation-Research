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

class TestPartitionList(unittest.TestCase):
    def build_linked_list(self, values):
        dummy = ListNode(0)
        cur = dummy
        for v in values:
            cur.next = ListNode(v)
            cur = cur.next
        return dummy.next

    def linked_list_to_list(self, head):
        result = []
        cur = head
        while cur:
            result.append(cur.val)
            cur = cur.next
        return result

    def test_normal_cases(self):
        head = self.build_linked_list([1, 4, 3, 2, 5, 2])
        new_head = partition_list(head, 3)
        self.assertEqual(self.linked_list_to_list(new_head), [1, 2, 2, 4, 3, 5])

        head = self.build_linked_list([2, 1])
        new_head = partition_list(head, 2)
        self.assertEqual(self.linked_list_to_list(new_head), [1, 2])

    def test_edge_cases(self):
        self.assertIsNone(partition_list(None, 1))

        head = self.build_linked_list([1])
        new_head = partition_list(head, 0)
        self.assertEqual(self.linked_list_to_list(new_head), [1])

        head = self.build_linked_list([1, 2, 3])
        new_head = partition_list(head, 5)
        self.assertEqual(self.linked_list_to_list(new_head), [1, 2, 3])

        head = self.build_linked_list([5, 6, 7])
        new_head = partition_list(head, 5)
        self.assertEqual(self.linked_list_to_list(new_head), [5, 6, 7])

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            partition_list(123, 3)

        with self.assertRaises(TypeError):
            head = self.build_linked_list([1, 2, 3])
            partition_list(head, "2")

        with self.assertRaises(AttributeError):
            head = self.build_linked_list([1, None, 3])
            partition_list(head, 2)

if __name__ == "__main__":
    unittest.main()