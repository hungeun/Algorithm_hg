while 1:
    try:
        A,B = map(int,input().split())
        print(A+B)
    except:
        break
    
try:
    while 1:
        a,b = map(int,input().split())
        print(a+b)
except:
    exit()
    
#오류 처리를 위한 try,except문의 기본 구조
# try:
    #...                                
# except:[발생오류[as 오류 메시지 변수]]:
    #...
    
#1  try:
#       ...
#   except:
#       ...     오류 종류에 상관없이 오류나면 except블록 수행
#2  try:
#       ...
#   except 발생오류:
#       ...     발생오류에 관해서만 except 블록 수행
#3 try:
#       ...
#  except 발생오류 as 오류 메시지 변수:
#       ...      두 번째 경우에서 오류 메시지의 내용까지 알고 싶을 때
