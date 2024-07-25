# 윤년
# 윤년은 연도가 4의 배수 && 100의배수! or 400의배수1
# 4의배수 && 100의 배수가 아닐때
# 4의배수 || 400의 배수
a = int(input())
result = '1' if a%4==0 and (a%100!=0 or a%400==0) else '0'
print(result)