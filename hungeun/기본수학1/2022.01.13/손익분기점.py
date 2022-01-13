a = int(input('고정비용을 입력하시오: '))
b = int(input('가변비용을 입력하시오: '))
c = int(input('노트북 가격은 얼마인가요?: '))

if b >= c:
    print(-1)
else:
    print(a//(c-b)+1)