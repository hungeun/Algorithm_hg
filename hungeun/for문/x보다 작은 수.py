n, x = map(int, input().split())
num = list(map(int,input().split()))

for i in range(n):
    if num[i] < x:
        print(num[i], end = " ")

#num 변수를 만들어 둘째 줄에 입력되는 숫자들은 list에 int로 집어 넣는다.
#if문을 이용하여 num[0~9] list에 있는 숫자들이 x인 값보다 적을 때 print함수로 출력