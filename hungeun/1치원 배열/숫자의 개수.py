a = int(input())
b = int(input())
c = int(input())
result = list(str(a * b * c))

for i in range(10):
    print(result.count(str(i)))
    
#a,b,c를 각각 입력받고 result 변수를 설정 후 a,b,c를 곱한 값을 문자열(str)로 변환 후 list[]로 묶는다.

#result = list["17037300"]
#result = [1,7,0,3,7,3,0,0]
#" "안에 들어있는 문자열(str)은 list를 사용해서 리스트로 변형해주면 0부터 각각의 index로 저장

#count(item): 매칭되는 갯수를 리턴해줌
#a = [1,5,5,3,7,0,1,2]
#a.count(5)
#2
#a.count(13)
#0