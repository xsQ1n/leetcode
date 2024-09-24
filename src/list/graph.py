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


def graph_dfs_with_recursion(graph: dict, start) -> None:
    # 使用递归
    isTouch = set()

    def dfs_helper(node):
        print(node)
        isTouch.add(node)
        for node in graph.get(node):
            if node not in isTouch:
                dfs_helper(node)

    dfs_helper(start)


def graph_dfs_iteration(graph: dict, start) -> None:
    # 使用 栈 完成；先进后出，与递归的顺序不一样
    stack = [start]
    isTouch = set()
    isTouch.add(start)

    while stack:
        cur = stack.pop()
        for node in graph.get(cur):
            if node not in isTouch:
                stack.append(node)
                isTouch.add(node)
        print(cur)




if __name__ == "__main__":
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }
    print("使用迭代完成深度优先遍历")
    graph_dfs_iteration(graph, 'A')
    print("使用递归完成深度优先遍历")
    graph_dfs_with_recursion(graph, 'A')
    print("广度优先遍历")
    graph_bfs(graph, 'A')


