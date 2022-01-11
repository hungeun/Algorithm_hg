cro = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
a = input().lower()

for i in cro:
    a = a.replace(i,'c')
    
print(len(a))
#변수 cro로 크로아티아 알파벳을 미리 [] 리스트로 묶어서 만들어 놓고 변수 a를 설정해서 lower()로 소문자로 입력받고 for문으로 cro반복
#a = [ljes = njak] [예제1]
#반복문 안에서 입력받은 a 중 i에 해당하는 즉 cro 리스트 안에 있는 문자열에 해당하는 것을 'c'로 바꿔주면 a = [ceccak] [예제1]
#len()으로 출력

#문자열 변경(replace)
#replace(old,new,[count]) => replace("찾을값","바꿀값",[바꿀횟수])
#a = '123,456,789,999' 
#replaceALL = a.replace(',','')     => 123456789999
#replace_1  = a.replace(',','',1)   => 123456,789,999
#replace_2  = a.replace(',','',2)   => 123456789.999
#replace_3  = a.replace(',','',3)   => 123456789999