# 공 바꾸기
import sys
n,m = map(int, sys.stdin.readline().split())
n_list = []
for nn in range(n): n_list.append(nn+1)
for _ in range(m):
    i,j = map(int, sys.stdin.readline().split())
    n_list[i-1], n_list[j-1] = n_list[j-1], n_list[i-1]
for i in range (n):
    print(n_list[i], end=' ')