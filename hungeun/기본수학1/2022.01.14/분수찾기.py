a =int(input())
line = 1

while a > line:
    a -= line
    line += 1
    
if line % 2 == 0:
    n = a
    z = line - a + 1
    
else:
    n = line - a + 1
    z = a
print(n, "/", z ,sep = "")

"""
print("안녕", "하세요", sep ="!!")
===> 안녕!!하세요

print('010','1234','5678',sep'-')
===> 010-1234-5678
"""