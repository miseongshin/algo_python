# N x M 얼음틀.
# 구멍뚫려 있는 부분 0, 칸마기 1
# 상, 하, 좌, 우 붙어있는경우 서로 붙어있는것으로 간주.
# 생성되는 아이스크림갯수는?
# 1<=N, M<-1000
# 안되네요.. 참
'''
5 4
00110
00011
11111
00000
'''

n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

print(graph)
graph.pop()
print(graph)

def dfs_ice(x,y):
    if x <= -1 or x >= n-1 or y <= -1 or y >= m:
        return False
    elif graph[x][y] == 0:
        graph[x][y] = 1
        dfs_ice(x-1, y)
        dfs_ice(x, y-1)
        dfs_ice(x+1,y)
        dfs_ice(x,y+1)
        return True
    return False

result = 0
for i in range(n):
    for j in range(m):
        if dfs_ice(i, j):
            result +=1
print(result)
