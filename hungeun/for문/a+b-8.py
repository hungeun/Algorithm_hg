T = int(input()) 
x = 1
for i in range(1, T+1): #T 만큼 반복
    A,B = map(int,input().split())  
    print(f'Case #{i}: {A} + {B} = {A+B}')  #f-string은 print함수 안에서 문자열을 작성하기 위해 사용하는 따옴표 앞에 f를 접두사로 붙여서 사용한다.
                                #f-string을 이용하면 일반 문자열과 다르게 따옴표 안에 {}괄호를 입력하고 광호 안에 변수나 변수를 연산한 값을 입력할 수 있다.
  