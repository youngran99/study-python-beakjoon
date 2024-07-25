# 알람시계
# 기존에 설정된 알람보다 45분 더 빠르게 설정하기
h,m = map (int, input().split())
m -= 45
if m<0:
    if h-1<0 :
        print("23",m+60)
    else :
        print(h-1,m+60)
else :
    print(h,m)