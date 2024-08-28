import sys

n, m = map(int, sys.stdin.readline().split())
visited = [False] * n
visited[0] = True # 1번 노드부터 시작하므로 방문처리

graph = [[0 for _ in range(n)] for _ in range(n)] # 인접 행렬 이용

# 그래프 생성
for _ in range(m):
    x, y = map(int, sys.stdin.readline().split())
    
    graph[x-1][y-1] = 1 # 연결 되어 있음  
    graph[y-1][x-1] = 1 # 연결 되어 있음

def DFS(vertex):
    for i in range(n):
        if (graph[vertex][i] == 1) and (not visited[i]): # 그래프가 연결되어있고 아직 방문하지 않은 정점이라면
            visited[i] = True # 방문처리
            DFS(i)

if __name__=='__main__':
    root = 0
    DFS(root)
    print(visited.count(True)-1)