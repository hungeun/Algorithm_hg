'''
n = a*5 + b*3 (a+b)의 최소값 구하기
숫자 n을 5로 나누면 n = a*5+k (k는 나머지)
k를 3으로 나누면 k = b*3+1
'''
n = int(input())
f = n//5 #f에 입력값을 5로 나눈 몫을 저장하고, n을 그 나머지로 바꿔줌
n %= 5
t = 0
while f >=0:
    if n%3 == 0:
        t = n//3
        n = n%3
        break
    f -=1
    n +=5
print((n==0) and (f+t) or -1)