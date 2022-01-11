alpha = input().lower()
dial = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
time = 0

for i in range(len(alpha)):
    for j in dial:
        if alpha[i] in j:
            time += dial.index(j) + 3
print(time)

#변수 alpha를 설정해서 lower()로 소문자로 단어를 입력받고 변수 dial로 숫자에 적혀있는 각각의 소문자를 [] 리스트로 만들어준다.
#다이얼을 걸기 위해 필요한 시간을 알기 위해 time변수를 0으로 초기화 시켜준다.
#변수의 len()만큼 i를 반복해주고 이중 반복문을 사용해서 dial에 있는 문자열 하나하나를 j로 반복
#dial = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
#dial = [0,1,2,3,4,5,6,7]
#if문으로 입력받은 alpha는 j의 문자열에 해당한다면 time에 해당하는 dial의 index 수와 j가 0부터 반복하기 시작한 것을 감안해 +3 해준다.

#index(x) 함수 : 리스트에 x 값이 있으면 x의 위치 값을 돌려준다.
#a = [1,2,3] >>> a.index(3) => 2 // a.index(1) => 0