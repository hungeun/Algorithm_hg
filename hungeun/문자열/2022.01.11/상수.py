a,b = input().split()
a = int(a[::-1])
b = int(b[::-1])

if a > b:
    print(a)
else:
    print(b)
    
#리스트는 리스트변수[시작인덱스 : 종료인덱스 : step]으로 이루어진다. 여기서 step을 이용하면 reverse()함수를 이용하지 않고 리스트 내용을 뒤집을 수 있다
#때문에 변수 a,b에 각각 입력받은 734,893을 다시 거꾸로 돌려서 int로 변환시키면 a = 437 , b = 398

#step 사용
# s = 'show how to index into sequences'. split()  >> s      => ['show', 'how', 'to', 'index', 'into', 'sequences']
#                                                  >> s[::2] => ['show', 'to', 'into']
#                                                  >> s[::-1]=> ['sequences'. 'into', 'index', 'to', 'how', 'show']

#reverse함수 : 리스트를 역순으로 뒤집어 준다. 이때 리스트 요소들을 순서대로 정렬한 다음 다시 역순으로 정렬하는 것이 아니라 현재의 리스트를 그대로 거꾸로 뒤집는다.
# a = ['a', 'c', 'b']  >> a.reverse() >> a  => ['b','c','a']