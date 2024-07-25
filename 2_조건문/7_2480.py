# 주사위 세개
# 같은 눈이 3개 10,000+눈의수*1000
# 같은 눈이 2개 1,000+(같은눈)*100
# 모두 다른 눈이 나오는 경우 (그중의 큰눈)*100
a,b,c = map(int, input().split())
if a==b==c : print(10000+a*1000)
elif a==b or b==c or c==a :
    if a==b : print(1000+a*100)
    elif b==c : print(1000+b*100)
    elif a==c : print(1000+c*100)
else :
    if a>=b and a>=c : print(a*100)
    elif b>=c and b>=a : print(b*100)
    elif c>=a and c>=b : print(c*100)