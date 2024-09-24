# 二叉树类
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 多叉数类
class MulTreeNode:
    def __init__(self, val: int):
        self.val = val
        self.children = []


# 迭代遍历数组
def traverse_array(array) -> None:
    for i in array:
        print(i)

# 递归遍历数组
def traverse_array_recursion(array, index) -> None:
    if len(array) == 0 or index == (len(array) - 1):
        return

    # 前序位置
    # print(array[index])
    traverse_array_recursion(array, index + 1)
    # 后序位置
    # print(array[index])

# 迭代遍历单链表
def traverse_list(head) -> None:
    while head is not None:
        print(head.val)
        head = head.next

# 递归遍历单链表
def traverse_list_recursion(head) -> None:
    if not head:
        return

    # 前序位置
    #print(head.val)
    traverse_list_recursion(head.next)
    # 后序位置
    #print(head.val)

# 二叉树递归遍历（DFS）框架
def traverse_binary_tree(tree: TreeNode) -> None:
    if tree is None:
        return

    # 前序变量：只能获取根节点的值
    traverse_binary_tree(tree.left)
    # 中序遍历：可以获取根节点的值，左子树
    traverse_binary_tree(tree.right)
    # 后序遍历：可以获取根节点的值、左子树，右子树

# 知识点： 二叉搜索树（BST） 的中序遍历结果是有序的


# 二叉树层序遍历（BFS）框架
## 写法1
from collections import deque
def levelOrderTraverse(tree: TreeNode) -> None:
    if tree is None:
        return
    # 创建一个双端队列
    q = deque()
    q.append(tree)

    while q:
        node = q.popleft();
        print(node.val)
        #子节点介入队列
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)


## 写法2：记录层级深度
from collections import deque
def levelOrderTraverse(tree: TreeNode) -> None:
    if tree is None:
        return
    # 创建一个双端队列
    q = deque()
    q.append(tree)
    # 记录等当层级深度
    depth = 1

    while q:
        size = len(q)
        for i in range(size):
            node = q.popleft();
            print(node.val, depth)

            #子节点介入队列
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

        depth += 1


## 写法3：适配不同权重边的写法，后序可进阶图遍历
from collections import deque
class State(object):
    def __init__(self, node: TreeNode, depth) -> None:
        self.node = node
        self.depth = depth

def levelOrderTraverse(tree: TreeNode) -> None:
    if tree is None:
        return

    q = deque()
    q.append(State(tree, 1))

    while q:
        cur = q.popleft()
        print(cur.node.val, cur.depth)

        if cur.node.left:
            q.append(State(cur.node.left, cur.depth + 1))
        if cur.node.right:
            q.append(State(cur.node.right, cur.depth + 1))


# 多叉数递归遍历（DFS）框架
def traverse_n_tree(tree: MulTreeNode) -> None:
    if tree is None:
        return

    # 前序位置
    for child in tree.children:
        traverse_n_tree(child)
    # 后序位置

# 知识点：多叉树没有了中序位置，因为可能有多个节点嘛，所谓的中序位置也就没什么意义了。


# 多叉数层序遍历（BFS）框架
## 方法1
from collections import deque
def levelOrderTraverse(tree: MulTreeNode) -> None:
    if tree is None:
        return

    q = deque()
    q.append(tree)

    while q:
        node = q.popleft();
        print(node.val)

        for child in node.children:
            q.append(child)

## 方法2：记录层级深度
from collections import deque
def levelOrderTraverse(tree: MulTreeNode) -> None:
    if tree is None:
        return

    q = deque()
    q.append(tree)
    depth = 1

    while q:
        size = len(q)
        for i in range(size):
            node = q.popleft();
            print(node.val, depth)

            for child in node.children:
                q.append(child)
        depth += 1

## 方法3：适配不同权重边的写法
class State(object):
    def __init__(self, node: MulTreeNode, depth) -> None:
        self.node = node
        self.depth = depth

def levelOrderTraverse(tree: MulTreeNode) -> None:
    if tree is None:
        return

    q = deque()
    q.append(State(tree, 1))

    while q:
        cur = q.popleft()
        print(cur.node.val, cur.depth)

        for child in cur.node.children:
            q.append(State(child, cur.depth + 1))


## 图-DFS
### 方式1：栈，先进后出
def graph_dfs_with_iteration(graph, start) -> None:
    if start not in graph:
        return

    stack = [start]
    isTouch = {start: 1}

    while len(stack) > 0:
        cur = stack.pop()
        nodes = graph.get(start)

        for node in nodes:
            if node not in isTouch:
                stack.append(node)
                isTouch[node] = 1

        print(cur)

### 方式2：递归
def graph_dfs_with_recursion(graph, start) -> None:
    if start not in graph:
        return

    isTouch = set()

    def dfs(node):
        isTouch.add(node)
        for node in graph.get(node):
            if node not in isTouch:
                dfs(node)

    dfs(start)



## 图-BFS
from collections import deque
def graph_bfs(graph: dict, start) -> None:
    # 使用队列完成，先进先出
    if start not in graph:
        return

    queue = deque([start])
    isTouch = set()
    isTouch.add(start)

    while queue:
        cur = queue.popleft()
        nodes = graph.get(cur)

        for node in nodes:
            if node not in isTouch:
                queue.append(node)
                isTouch.add(node)
        print(cur)


# 自顶向下递归的动态规划
# def dp(状态1, 状态2, ...):
#     for 选择 in 所有可能的选择:
#         # 此时的状态已经因为做了选择而改变
#         result = 求最值(result, dp(状态1, 状态2, ...))
#     return result

# 自底向上迭代的动态规划
# 初始化 base case
# dp[0][0][...] = base case
# # 进行状态转移
# for 状态1 in 状态1的所有取值：
#     for 状态2 in 状态2的所有取值：
#         for ...
#             dp[状态1][状态2][...] = 求最值(选择1，选择2...)


# 滑动窗口算法框架伪码
# 滑动窗口算法伪码框架
def slidingWindow(s: str):
    # 用合适的数据结构记录窗口中的数据，根据具体场景变通
    # 比如说，我想记录窗口中元素出现的次数，就用 map
    # 如果我想记录窗口中的元素和，就可以只用一个 int
    window = ...

    left, right = 0, 0
    while right < len(s):
        # c 是将移入窗口的字符
        c = s[right]
        window.add(c)
        # 增大窗口
        right += 1
        # 进行窗口内数据的一系列更新
        ...

        # *** debug 输出的位置 ***
        # 注意在最终的解法代码中不要 print
        # 因为 IO 操作很耗时，可能导致超时
        # print(f"window: [{left}, {right})")
        # ***********************

        # 判断左侧窗口是否要收缩
        while left < right and window needs shrink:
            # d 是将移出窗口的字符
            d = s[left]
            window.remove(d)
            # 缩小窗口
            left += 1
            # 进行窗口内数据的一系列更新
            ...
