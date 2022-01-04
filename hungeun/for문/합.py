n = int(input())
sum = 0

for i in range(1, n+1):
    sum += i
    
print(sum)

#n으로 정수를 입력받고, 정수 n까지 도달하는 정수를 다 더해줄 변수 sum을 0으로 초기화
#range는 1부터 입력받은 n+1까지 반복
#sum += i ->i =1 일때, sum = 0+1 / i = 2 , sum = 1 + 2 / i = 3, sum = 3 + 3