from collections import deque


def solution():  # input 처리
    N, M = map(int, input().split())
    graph = []
    for _ in range(N):
        graph.append(list(map(int, list(input()))))  # bfs를 위한 자료구조
    # 동서남북
    dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
    # graph와 똑같은 사이즈의 리스트(방문 여부, 방문한 곳의 수를 표시)
    visited = [[0 for _ in range(M)] for _ in range(N)]

    def bfs(i, j):
        # 출발
        visited[0][0] = 1
        queue = deque([(0, 0)])

        while queue:
            x, y = queue.popleft()  # 목적지에 도착하면 중단
            if x == N - 1 and y == M - 1:
                print(visited[x][y])
                break
            # 동서남북
            for i in range(4):
                next_x = x + dx[i]
                next_y = y + dy[i]
                # 리스트의 크기를 벗어나지 않는지 검사 # & 방문하지 않은 곳이 맞는지,
                # 방문할 수 있는 곳인지(길이 맞는지) 검사
                if 0 <= next_x <= N - 1 and 0 <= next_y <= M - 1 \
                 and visited[next_x][next_y] == 0 and graph[x][y] == 1:
            # 방문한 곳으로 표시
                    visited[next_x][next_y] = visited[x][y] + 1
            # 다음에 방문할 곳
                    queue.append((next_x, next_y))
            # 목적지까지 가기위해 방문한 곳의 개수를 리턴
        return visited[-1][-1]

    return bfs(0, 0)


solution()

