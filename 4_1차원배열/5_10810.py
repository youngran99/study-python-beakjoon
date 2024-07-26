# 공 넣기
n, m = map(int, input().split())
n_list = [0] * n
for _ in range(m):
    i,j,k = map(int, input().split())
    for a in range(i, j+1):
        n_list[a-1] = k
for i in range (n):
    print(n_list[i], end=' ')