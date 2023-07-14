from src.list.creatList import ListNode
from src.list.operateList import OperateList

if __name__ == '__main__':
    
    #revese list
    list = OperateList()
    listnode = list.createList(4)
    list.printList(listnode)
    list.printList(list.reverseList(listnode))
    #list.printList(list.recursion_re_list(listnode))