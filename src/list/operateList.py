from asyncio.log import logger
from copy import copy
from email.errors import HeaderParseError
from email.quoprimime import header_check
from inspect import isfunction
import logging
import re
from typing import List
from .creatList import ListNode
from src.common.logger import Logger


class OperateList(object):
    """"
    operate list
    """
    def __init__(self) -> None:
        self.logger = Logger("Operate List").getlogger(leavel=logging.DEBUG)\

    def createList(self, length) -> ListNode:
        """
        create list
        """
        listnode = None
        for i in range(length,0,-1):
            listnode = ListNode(i, listnode)
        self.logger.info("Create list success !!!")
        return listnode

    def printList(self, head):
        """
        Print list
        """
        if (head == None):
            self.logger.error("List is None !!!")
            return head.val   

        list_var = [] 
        while head:
            list_var.append(head.val)
            head = head.next
        self.logger.info(f"Print list: {list_var}")

    def reverseList(self, head: ListNode) -> ListNode:
        """
        Revese list(iterate)
        """
        # if (head == None):
        #     self.logger.error("List is None !!!")
        #     return head 
        re_list = None
        while head:           
            tmp = head.next
            head.next = re_list
            re_list = head
            head = tmp
        self.logger.info(f"Revese list success !!!")
        return re_list

    def recursion_re_list(self, head: ListNode) -> ListNode:
        """
        Revese list(recursion)
        """
        if (head == None or head.next == None):
            return head
        newhead = self.recursion_re_list(head.next)
        head.next.next = head
        head.next = None
        return newhead

    def intersect_list(self, haedA: ListNode, headB: ListNode) -> ListNode:
        """
        find intersect list
        """
        if haedA == None and headB == None:
            return None
        copy_haedA = haedA
        copy_haedB = headB
        while copy_haedA != copy_haedA:
            if copy_haedA == None:
                copy_haedA = headB
            else:
                copy_haedA = copy_haedA.next
            if copy_haedB == None:
                copy_haedB = haedA
            else:
                copy_haedB = copy_haedB.next
        return copy_haedA

    def merge_2_list(self, headA: ListNode, headB: ListNode) -> ListNode:
        """
        merge two ascending list
        """
        #iteration
        #time:O(m+n),space:O(1)
        final_list = ListNode(-1)
        tmp_list = final_list
        while headA and headB:
            if headA.val > headB.val:
                tmp_list.next = headB
                headB = headB.next
            else:
                tmp_list.next = headA
                headA = headA.next
            tmp_list = tmp_list.next
        tmp_list.next = headB if headA == None else headA
        return final_list
        # #recursion
        # #time:O(m+n),space:O(m+n)
        # if headA == None:
        #     return headB
        # if headB == None:
        #     return headA
        # if headA.val > headB.val:
        #     headB.next = self.merge_2_list(headA, headB.next)
        #     return headB
        # else:
        #     headA.next = self.merge_2_list(headA.next, headB)
        #     return headA

    def partition_list(self, head: ListNode, x: int) -> ListNode:
        """
        partition list,less then x in front
        """
        if head == None:
            return None
        headA = ListNode
        headB = ListNode
        tmp_headA = headA
        tmp_headB = headB
        while head != None:
            if head.val < x:
                tmp_headA.next = head
                tmp_headA = tmp_headA.next
            else:
                tmp_headB.next = head
                tmp_headB = tmp_headB.next
            head = head.next
        tmp_headB.next = None
        tmp_headA.next = headB
        return headA

    def cycle_list(self, head:ListNode) -> ListNode:
        """
        find the entry to cycle list 
        """
        fast, slow = head, head
        while fast != None and fast.next != None:
            fast, slow = fast.next.next, slow.next
            if fast == slow:
                fast = head
                while fast != slow:
                    fast, slow = fast.next, slow.next
                return fast
        return None
