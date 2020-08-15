import unittest


class ListNode:
    def __init__(self, val=0, n=None):
        self.val = val
        self.next = n

    def __eq__(self, other):
        if not isinstance(other, ListNode):
            return NotImplemented
        ptrs = self
        ptro = other
        while ptrs is not None or ptro is not None:
            if ptrs is None or ptro is None:
                return False
            if ptrs.val != ptro.val:
                return False
            ptrs = ptrs.next
            ptro = ptro.next
        return True


class Solution:
    def add_two_numbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        result = ListNode()
        p, q = l1, l2
        ptr = result
        carry = 0
        while p is not None or q is not None:
            x = p.val if p is not None else 0
            y = q.val if q is not None else 0
            s = x + y + carry
            carry = s // 10
            ptr.next = ListNode(s % 10)
            ptr = ptr.next
            if p is not None:
                p = p.next
            if q is not None:
                q = q.next

        if carry > 0:
            ptr.next = ListNode(carry)

        return result.next


class TestStringMethods(unittest.TestCase):

    def test_1(self):
        solution = Solution()
        l1 = ListNode(2, ListNode(4, ListNode(3)))
        l2 = ListNode(5, ListNode(6, ListNode(4)))
        res = ListNode(7, ListNode(0, ListNode(8)))
        self.assertEqual(solution.add_two_numbers(l1, l2), res)

    def test_2(self):
        solution = Solution()
        l1 = ListNode(1, ListNode(8))
        l2 = ListNode(0)
        res = ListNode(1, ListNode(8))
        self.assertEqual(solution.add_two_numbers(l1, l2), res)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestStringMethods)
    unittest.TextTestRunner(verbosity=2).run(suite)
