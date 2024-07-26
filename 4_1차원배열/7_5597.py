# 과제 안 내신 분..?
n_list1 = [i for i in range(1,31)]
n_list2 = []
for _ in range(28):
    a = int(input())
    n_list2.append(a)
for i in n_list1:
    if i not in n_list2:
        print(i)