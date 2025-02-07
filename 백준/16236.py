import sys
from collections import deque

sys.stdin = open('sample_input.txt', 'r')

d = [(-1, 0), (0, -1), (1, 0), (0, 1)]

def bfs(shark_size, a, b):
    queue = deque()
    queue.append((a, b, 0))  # 거리 정보 추가 (distance)
    visited = [[False] * n for _ in range(n)]
    visited[a][b] = True

    min_dist = float('inf')
    target_fish = None  # 먹이 정보 저장
    
    while queue:
        r, c, dist = queue.popleft()

        # 먹이 발견 시 최단 거리 갱신 및 탐색 종료
        if 0 < shark_map[r][c] < shark_size:
            if dist < min_dist or (dist == min_dist and (r < target_fish[0] or (r == target_fish[0] and c < target_fish[1]))):
                min_dist = dist
                target_fish = (r, c)
                continue  # 먹이를 찾았으므로 더 이상 탐색하지 않음

        # 상어 이동 가능 위치 탐색 (먹이가 아닌 경우)
        for i in range(4):
            dr, dc = r + d[i][0], c + d[i][1]
            if 0 <= dr < n and 0 <= dc < n and not visited[dr][dc] and shark_map[dr][dc] <= shark_size:
                visited[dr][dc] = True
                queue.append((dr, dc, dist + 1))

    return target_fish, min_dist  # 먹이 위치, 최단 거리 반환

def feed(shark_size, x, y):
    global shark_eat, result

    while True:
        target_fish, dist = bfs(shark_size, x, y)
        if not target_fish:  # 먹이 없음
            return

        # 먹이 섭취 및 이동
        shark_map[target_fish[0]][target_fish[1]] = 9
        shark_map[x][y] = 0
        shark_eat += 1
        result += dist
        x, y = target_fish

        if shark_eat == shark_size:
            shark_size += 1
            shark_eat = 0

result = 0
shark_eat = 0
n = int(input())
shark_map = [list(map(int, input().split())) for _ in range(n)]
for i in range(n):
    for j in range(n):
        if shark_map[i][j] == 9:
            a, b = i, j
feed(2, a, b)
print(result)