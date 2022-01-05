n = int(input())       #68   
num = n
cnt = 0                #사이클 수

while True:
    a = num // 10       #6              #// : 나누기 연산 후 소수점 이하의 수를 버리고, 정수 부분의 몫을 구함
    b = num % 10        #8
    c = (a + b) % 10    #6 + 8 =1"4"
    num = (b * 10) + c  #80 + 4 = 84
    
    cnt = cnt + 1       #사이클 수 + 1
    if(num == n):       #num에서 입력된  n과 똑같은 숫자가 나오면 멈춤
        break
print(cnt)

#2번째 방법
#n = input()                                 #n = "26"
#num = n
#cnt = 0

#while 1:
#    if len(num) == 1:
#        num = "0" + num
#    plus = str(int(num[0] + int(num[1])))   #2 + 6 = "8"
#    num = num[-1] + plus[-1]                #"6" + "8" = "68"
#    cnt +=1
#    if num == n:
#        print(cnt)
#        break


