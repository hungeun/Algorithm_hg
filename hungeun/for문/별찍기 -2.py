n = int(input()) 

for i in range(1, n+1):
   print(' ' *(n-i) + '*' *i)

  #' ' 빈 칸을 n에서 i = 1~n까지 빼준 값 만큼 곱해서 
  #' '
  #' '
  #' '...을 만든다.