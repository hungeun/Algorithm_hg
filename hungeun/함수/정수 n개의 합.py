def solve(a):
    ans = 0
    for i in a:
        ans += i
    return ans
#전달받은 매개변수 리스트 a를 반복문으로 이용해서 인자 하나씩 더해서 반환


#def function_name(argument....):    
# 괄호 안에는 전달받을 매개변수를 넣는다.
#   do something...
#  return result

#2번째
#def solve(a):
#    return sum(a)
#함수명을 solve, 전달받은 매개변수는 a
#반환값으로 파이썬 내장함수인 합계를 구해주는 sum함수를 써서 전달받은 리스트들의 합을 반환해 주었다.