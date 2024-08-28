import sys

n, m = map(int, sys.stdin.readline().split())
visited = [False] * n
visited[0] = True # 1번 노드부터 시작하므로 방문처리

graph = [[] for _ in range(n)]

# 그래프 생성 (Linked list 이용)
for _ in range(m):
    x, y = map(int, sys.stdin.readline().split())
    graph[x-1].append(y-1)
    graph[y-1].append(x-1)

def DFS(vertex):
    for i in range(len(graph[vertex])):
        currV = graph[vertex][i]
        if not visited[currV]:
            visited[currV] = True
            DFS(currV)

if __name__=="__main__":
    root = 0
    DFS(root)

    print(visited.count(True)-1)