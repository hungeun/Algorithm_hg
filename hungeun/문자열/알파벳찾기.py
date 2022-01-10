a = input()
alpha = 'abcdefghijklmnopqrstuvwxyz'

for i in alpha:
    if i in a:
        print(a.index(i), end = ' ')
    else:
        print(-1,end = ' ')
#단어 입력 받을 변수 a
#알파벳들이 존재하는 변수 alpha
#입력한 a에 알파벳 존재 유무를 확인 하기 때문에 모든 알파벳 alpha 변수를 for문으로 반복해서 a에서의 그 위치를 반환
#알파벳의 각 요소가 a에 존재하면 그 때 a에서의 위치를 반환하기 위해 index사용. 
#예제는 한칸씩 듸워서 반환하기 때문에 출력이후 한칸을 띄우는 end = ' '사용 