# reveseList(反转链表)

## 1、迭代

### 解析

1. 设置初始结点，也是反转之后的头部结点

   ```
   re_list = None
   ```

2. 设置循环

   1. 设置临时变量，存放下一个结点的信息
   2. 当前结点的next指向re_list
   3. 给临时变量重新复制为head
   4. head切换到下一个结点

   ```python
   tmp = head.next
   head.next = re_list
   re_list = head
   head = tmp
   ```

### 实现

```python
def reverseList(self, head: ListNode) -> ListNode:
    """
        Revese list(iterate)
        """
    re_list = None
    while head:           
        tmp = head.next
        head.next = re_list
        re_list = head
        head = tmp
        self.logger.info(f"Revese list success !!!")
        return re_list
```

### 复杂度

时间复杂度：O(n)，n代表链表的长度，需要遍历链表一次

空间复杂度：O(1)

## 2、递归

### 解析

1. 递归寻找反转之后的头结点，即反转前的尾结点，也是递归之后返回的结点

   ```python
   newhead = self.recursion_re_list(head.next)
   ```

2. 结点反转，下一个结点指向当前结点

   ```python
   head.next.next = head
   ```

3. 当前结点next赋None，断开之前指向，防止成环

   ```python
   head.next = None
   ```

### 实现

```python
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
```

### 复杂度

时间复杂度：O(n)，n代表链表的长度，每个结点都需要进行一次反转操作

空间复杂度：O(n)，n代表链表的长度，主要是递归调用的栈空间，做多为n层