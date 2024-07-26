# 나머지
n_list1, n_list2 = [], []
for _ in range(10) :
    a = int(input())
    n_list1.append(a)
    n_list2.append(a % 42)
n_list2=set(n_list2)
print(len(n_list2))