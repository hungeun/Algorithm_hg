def myCode():
    tc = int(input())
    num = list(map(int, input().split()))
    cnt = 0
    for i in num:
        if(i < 2):
            continue
        else:
            nanum = 2
            while(True):
                if(i == nanum):
                    cnt += 1
                    break
                if(i % nanum == 0):
                    break
                nanum += 1
    print(cnt)

def main():
    myCode()
if __name__ == '__main__':
    main()