a = input().lower()     #a = Mississipi / baaa
list_a = list(set(a))   #list_a = ['M','i','s','s,'i','s','s','i','p','i'] / ['b','a','a','a']
cnt = []
 
for i in list_a:        #i = m, i, s, p / b, a
    count = a.count(i)  
    cnt.append(count)   #cnt = [4,4,1,1] / [1,3]
    
if cnt.count(max(cnt)) >= 2:
    print('?')
else:
    print(list_a[(cnt.index(max(cnt)))].upper())

#변수 a 설정하고 lower()를 이용해서 입력받은 문자열을 소문자로만 받고 이것을 set()을 이용해서 자료형의 중복을 제거한 뒤 list()로 묶음
#가장 많이 사용된 알파벳을 알기 위해서 cnt변수를 []리스트로 초기화하면서 변수 설정 끝
#a = mississipi / list_a = ['m','i','s','p']
#list_a안의 문자들을 for문으로 반복해주는데 count변수를 새로 만들어 중복되는 문자를 제외하기 전 입력받은 a변수에서 그 문자가 몇 개 있었는지
#count()를 이용해서 세고, cnt변수 리스트에 append, 추가 / cnt = [4,4,1,1]
#if문을 사용해서 cnt변수 리스트에 가장 큰 값 max(cnt)를 count()함수를 이용해서 센 개수가 cnt변수 리스트 안에 2개 이상이라면 
#이 때는 가장 많이 사용된 알파벳, 즉 max(cnt)가 여러 개 존재하는 경우기기 때문에 '?' 출력
#나머지 경우를 설명하기 위해 a = bass / list_a = [b,a] / cnt = [1,3] 코드에서는 max(cnt)는 3이 되고, index(3)은 cnt에서 cnt[1]에 위치
#즉, index 자체가 가리키는 3이 cnt[1]이기 때문에 list_a[1]은 a를 가리키는데 이것이 uppercase()로 인해 대문자로 출력되므로 A가 출력