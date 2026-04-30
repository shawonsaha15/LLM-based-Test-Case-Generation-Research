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

def build_linked(lst):
    dummy = ListNode(0)
    cur = dummy
    for v in lst:
        cur.next = ListNode(v)
        cur = cur.next
    return dummy.next

def to_list(head):
    res = []
    cur = head
    while cur:
        res.append(cur.val)
        cur = cur.next
    return res

class TestPartitionList(unittest.TestCase):
    def test_empty_list(self):
        self.assertIsNone(partition_list(None, 5))

    def test_single_node_less(self):
        head = build_linked([1])
        result = partition_list(head, 2)
        self.assertEqual(to_list(result), [1])

    def test_single_node_greater(self):
        head = build_linked([3])
        result = partition_list(head, 2)
        self.assertEqual(to_list(result), [3])

    def test_multiple_mixed(self):
        head = build_linked([1, 4, 3, 2, 5, 2])
        result = partition_list(head, 3)
        self.assertEqual(to_list(result), [1, 2, 2, 4, 3, 5])

    def test_all_less(self):
        head = build_linked([1, 2, 0])
        result = partition_list(head, 5)
        self.assertEqual(to_list(result), [1, 2, 0])

    def test_all_greater_or_equal(self):
        head = build_linked([5, 6, 7])
        result = partition_list(head, 5)
        self.assertEqual(to_list(result), [5, 6, 7])

    def test_duplicates_and_equal(self):
        head = build_linked([3, 1, 2, 3, 4])