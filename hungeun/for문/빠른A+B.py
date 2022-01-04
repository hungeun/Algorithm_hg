import sys # sys모듈 읽어 들이기

t = int(sys.stdin.readline())

for i in range(t):
    a,b = map(int, sys.stdin.readline().split())
    print(a+b)

#sys.stdin.readline() => 입력 받은 문자는 사용자가 숫자를 입력하더라도 문자열로 입력받게된다