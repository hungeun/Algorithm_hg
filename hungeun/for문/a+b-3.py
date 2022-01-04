T = int(input()) #테스트 케이스 개수 T를 입력받음

for i in range(T): #T 만큼 반복
    A,B = map(int,input().split())  
    print(A+B)
    #map이랑, input().split()이 뭔지//
    #split 함수를 이용해서 공백을 기준으로 두 문자열을 분리하고 정수로 변환하기 위해서 map 함수를 이용하여 코드를 한 줄로 작성하였다.  
    
    