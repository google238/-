# -*- coding: utf-8 -*-
"""
输入两个单调递增的链表，输出两个链表合成后的链表，当然我们需要合成后的链表满足单调不减规则
"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        # write code here
        pha = phb = ListNode(0)
        while pHead1 and pHead2:
            if pHead1.val < pHead2.val:
                tmp = ListNode(pHead1.val)
                pHead1 = pHead1.next
            else:
                tmp = ListNode(pHead2.val)
                pHead2 = pHead2.next
            phb.next = tmp
            phb = phb.next
        if pHead1:
            phb.next = pHead1
        if pHead2:
            phb.next = pHead2
        return pha.next