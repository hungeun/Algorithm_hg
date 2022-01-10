num = int(input())
result = str()
for i in range(num):
    num_of_time, num_str = input().split()
    num_of_time = int(num_of_time)
    for j in num_str:
        result = result + (j * num_of_time)
    print(result)
    result = str()
#조건1, 첫째 줄에는 테스트 케이스의 개수가 주어진다. -> 테스트 케이스의 개수 만큼 반복문을 돌린다.
#조건2, 각 테스트 케이스에는 글자 반복횟수 R과 문자열S가 공백을 통해 주어진다. 
    #   -> 개수 만큼의 반복문 안에서, 문자열을 방아와서 글자 * 반복횟수를 출력한다. 