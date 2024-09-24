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


    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        """
            合并 K 个升序链表
        """
        ## 方法1：逐一合并
        def mergeList(l1: ListNode, l2: ListNode) -> ListNode:
            tmp = cur_head = ListNode(-1)

            while l1 and l2:
                if l1.val < l2.val:
                    tmp.next = l1
                    l1 = l1.next
                else:
                    tmp.next = l2
                    l2 = l2.next
                tmp = tmp.next

            tmp.next = l1 if l1 else l2
            return cur_head.next

        cur_head = ListNode(-1)
        for head in lists:
            if head is None:
                continue

            tmp = cur_head.next
            cur_head.next = mergeList(head, tmp)

        return cur_head.next

        ## 方法2：优先队列
        # if not lists:
        #     return None

        # # 使用优先队列（最小堆）来维护当前所有链表的头部节点
        # import heapq
        # dummy = ListNode(-1)
        # current = dummy

        # # 构建最小堆
        # heap = []
        # for i, lst in enumerate(lists):
        #     if lst:
        #         heapq.heappush(heap, (lst.val, i, lst))

        # # 合并链表
        # while heap:
        #     _, i, node = heapq.heappop(heap)
        #     current.next = node
        #     current = current.next
        #     if node.next:
        #         heapq.heappush(heap, (node.next.val, i, node.next))

        # return dummy.next


    def find_end_k_node(self, head:ListNode, k:int):
        """
        返回链表的倒数第 k 个节点
        """
        fast, slow = head, head
        for i in range(k):
            fast = fast.next

        while slow:
            fast, slow = fast.next, slow.next
        return fast


    def removeNthFromEnd(self, head:ListNode, n:int):
        """
        删除链表的倒数第 N 个结点
        """
        # 特殊情况当n = 链表长度时，寻找倒数n+1个节点时，会出现溢出，因此头部在添加一个节点，防止溢出
        cur_head = ListNode(-1, head)
        fast, slow = head, cur_head

        for i in range(n):
            fast = fast.next

        while fast:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next

        return cur_head.next


    def middleNode(self, head: ListNode) -> ListNode:
        """
        单链表的中点
        """
        slow, fast = head, head

        while fast and fast.next:
            slow  = slow.next
            fast = fast.next.next
        return slow


    def hasCycle(self, head: ListNode) -> bool:
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False


    def detectCycle(self, head: ListNode) -> ListNode:
        # ## 方法1：使用set实现
        # tmp = head
        # visited = set()
        # while tmp:
        #     if tmp in visited:
        #         return tmp

        #     visited.add(tmp)
        #     tmp = tmp.next
        # return None

        ## 方法2：快慢指针
        slow, fast = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                break

        if not fast or not fast.next:
            return None

        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return slow


    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        """
        两个链表是否相交
        """
        l1, l2 = headA, headB

        while l1 != l2:
            l1 = l1.next if l1 else headB
            l2 = l2.next if l2 else headA
        return l1


    def deleteDuplicates(self, head: ListNode) -> ListNode:
        """
        删除链表中重复的元素
        """
        if not head:
            return None

        slow, fast = head, head.next
        while fast:
            if slow.val == fast.val:
                slow.next = fast
                slow = slow.next
            fast = fast.next
        slow.next = None
        return head


    def removeElement(self, nums: List[int], val: int) -> int:
        """
        移除值为 val 的元素
        """
        slow, fast = 0, 0
        while fast < len(nums):
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1

        return slow


