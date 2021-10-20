def dfs(graph,start_node):
    visited_queue, need_visit_stack = list(),list()
    need_visit_stack.append(start_node)
    while need_visit_stack:
        node = need_visit_stack.pop()
        if node not in visited_queue:
            visited_queue.append(node)
            need_visit_stack.extend(graph[node])
    return visited_queue
