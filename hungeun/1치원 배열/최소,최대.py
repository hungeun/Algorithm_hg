a = int(input()) 
b = list(map(int,input().split()))
print('{} {}'.format(min(b),max(b)))

#배열에 입력을 받을 때 test case의 갯수와 상관없이 일단 입력만 받아놓고 진행한다.
#b에 리스트 형태로 값을 받는데 예제 입력에 보면 각 숫자마다 띄어쓰기로 구분하여 입력을 여러 개 받기 때문에 list,map,input().split()을 통해 입력을 받는다
#리스트의 최소값을 구하는 min과 최대값을 구하는 max를 이용