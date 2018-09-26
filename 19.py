# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# class Solution:
#     def removeNthFromEnd(self, head, n):
#         """
#         :type head: ListNode
#         :type n: int
#         :rtype: ListNode
#         """
#         # 第一次遍历，得知链表长度
#         length = 0
#         tmp = head
#         while tmp.next:
#             tmp = tmp.next
#             length += 1
#         # 第二次遍历，删除第l-n+1个节点
#         dummy = ListNode(0)
#         p = dummy
#         m = length - n + 1  # 实际删除链表第m个元素
#         while m > 0:
#             p.next = head
#             head = head.next
#             p = p.next
#             m -= 1
#         p.next = head.next
#         return dummy.next

# 两个指针一次遍历
class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        fast = slow = head
        for _ in range(n):
            fast = fast.next
        # 如果是最后一个节点，则结果是去掉第一个节点
        if not fast:
            return head.next
        # 两个指针同时后移，直到fast到达链表尾
        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next =slow.next.next
        return head
