t = int(input())

for i in range(t):
    ox = input()
    score = 0
    cnt = 0
    for i in range(len(ox)):
        if ox[i] == "O":
            cnt += 1
            score += cnt
        elif ox[i] == "X":
            cnt = 0
    print(score)

#변수 t를 설정해서 test case를 입력 받고 for문으로 test case의 수만큼 반복 해준다
#for문 안에서 변수ox를 설정 후 ox를 입력받고 최종 출력될 score 변수와 test case 마다 O의 수를 count할 변수 cnt를 만들어 0으로 초기화 시켜놓는다.
#다시 for문을 만들어서 ox에 입력받은 수만큼 반복을 해주며 if문으로 만약 ox(문자열 기본적으로 리스트) 리스트에 "O"가 있다면 cnt를 1 더해주고 score에 cnt만큼 더함
#"X"일 경우 (elif or else) cnt를 다시 0으로 초기화 시켜줘서 그 다음 "0"을 맞이할 때 다시 1부터 cnt를 셀 수 있도록 한다.
#cnt가 누적된 score를 출력해준다.