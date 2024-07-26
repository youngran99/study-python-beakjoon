# 평균
n = int(input())
sum = 0
a = list(map(int, input().split()))
for i in range(n) :
    sum += a[i]/max(a)*100
print(sum/n)