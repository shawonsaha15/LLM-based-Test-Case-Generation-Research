import unittest

class TestPartitionList(unittest.TestCase):
    @staticmethod
    def _build_linked_list(values):
        """Arrange helper: builds a linked list from a Python list."""
        dummy = ListNode(0)
        current = dummy
        for v in values:
            node = ListNode(v)
            current.next = node
            current = node
        return dummy.next

    @staticmethod
    def _linked_list_to_list(head):
        """Arrange helper: converts a linked list back to a Python list."""
        result = []
        current = head
        while current:
            result.append(current.val)
            current = current.next
        return result

    # -------------------- Normal Cases --------------------
    def test_partition_normal_mixed_values(self):
        # Arrange
        head = self._build_linked_list([1, 4, 3, 2, 5, 2])
        x = 3

        # Act
        result_head = partition_list(head, x)

        # Assert
        result = self._linked_list_to_list(result_head)
        # All nodes < 3 should appear before nodes >= 3, original relative order preserved
        self.assertEqual(result, [1, 2, 2, 4, 3, 5])

    def test_partition_normal_all_less(self):
        # Arrange
        head = self._build_linked_list([1, 2, 2])
        x = 5

        # Act
        result_head = partition_list(head, x)

        # Assert
        result = self._linked_list_to_list(result_head)
        self.assertEqual(result, [1, 2, 2])

    def test_partition_normal_all_greater_or_equal(self):
        # Arrange
        head = self._build_linked_list([5, 6, 7])
        x = 5

        # Act
        result_head = partition_list(head, x)

        # Assert
        result = self._linked_list_to_list(result_head)
        self.assertEqual(result, [5, 6, 7])

    # -------------------- Boundary Cases --------------------
    def test_partition_boundary_empty_list(self):
        # Arrange
        head = None
        x = 1

        # Act
        result_head = partition_list(head, x)

        # Assert
        self.assertIsNone(result_head)

    def test_partition_boundary_single_node_less(self):
        # Arrange
        head = self._build_linked_list([0])
        x = 1

        # Act
        result_head = partition_list(head, x)

        # Assert
        result = self._linked_list_to_list(result_head)
        self.assertEqual(result, [0])

    def test_partition_boundary_single_node_equal(self):
        # Arrange
        head = self._build_linked_list([1])
        x = 1

        # Act
        result_head = partition_list(head, x)

        # Assert
        result = self._linked_list_to_list(result_head)
        self.assertEqual(result, [1])

    # -------------------- Invalid Input Cases --------------------
    def test_partition_invalid_non_int_x(self):
        # Arrange
        head = self._build_linked_list([1, 2, 3])
        x = "2"  # non‑int

        # Act & Assert
        with self.assertRaises(TypeError):
            partition_list(head, x)

    def test_partition_invalid_head_not_listnode(self):
        # Arrange
        head = [1, 2, 3]  # plain list, not ListNode
        x = 2

        # Act & Assert
        with self.assertRaises(AttributeError):
            partition_list(head, x)

    def test_partition_invalid_head_circular_reference(self):
        # Arrange: create a circular list to ensure function does not loop infinitely
        node1 = ListNode(1)
        node2 = ListNode(2)
        node1.next = node2
        node2.next = node1  # circular reference
        x = 2

        # Act & Assert
        # The implementation will eventually hit a RecursionError or infinite loop;
        # we protect against it by setting a timeout using a separate thread.
        import threading

        result = []

        def target():
            try:
                result.append(partition_list(node1, x))
            except Exception as e:
                result.append(e)

        thread = threading.Thread(target=target)
        thread.daemon = True
        thread.start()
        thread.join(timeout=1)  # 1 second timeout

        # Assert that the thread did not finish successfully (i.e., it timed out)
        self.assertTrue(thread.is_alive() or isinstance(result[0], Exception))
