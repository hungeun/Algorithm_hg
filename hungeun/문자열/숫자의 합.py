sum = 0
a = int(input())
b = input()

for i in b:
    sum += int(i)
print(sum)

#입력 값을 모두 더해줄 sum 변수, 입력 개수를 받을 a , a개의 수를 받을 b 지정
#for i in b: 조건을 이용해 b의 값을 하나씩 i에 대입해서 사용
#for문에는 sum += int(i)는 i값을 int로 형변화하여 sum에 더해줌