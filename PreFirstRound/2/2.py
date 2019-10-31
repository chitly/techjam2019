import queue
def solution(T):
    path = {}
    for i in range(1, len(T)):
        if i in path:
            path[i].append(T[i])
        else:
            path[i] = [T[i]]
        if T[i] in path:
            path[T[i]].append(i)
        else:
            path[T[i]] = [i]
    q = queue.Queue()
    q.put((0, False, 0)) # (curNode, useTicket, numberOfPath)
    visited = set()
    maxNumberOfPath = 0
    while not q.empty():
        curNode, useTicket, numberOfPath = q.get()
        if numberOfPath > maxNumberOfPath:
            maxNumberOfPath = numberOfPath
        for node in path[curNode]:
            if (curNode, node) in visited or (node, curNode) in visited:
                continue
            if node % 2 != 0 and useTicket:
                continue
            if node % 2 != 0:
                q.put((node, True, numberOfPath + 1))
            else:
                q.put((node, useTicket, numberOfPath + 1))
            visited.add((curNode, node))
    return maxNumberOfPath + 1