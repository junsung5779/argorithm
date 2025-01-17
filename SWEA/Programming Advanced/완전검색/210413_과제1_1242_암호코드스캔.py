import sys
sys.stdin = open("input210413.txt")

#결과를 반환하는 함수
def solve():
    result = 0
    #arr의 가로 한 줄 한 줄에 대해서 뒤쪽부터 암호코드 찾기
    for i in range(N):  #가로 한줄 한줄 확인하기
        #맨 뒤쪽 부터 검사
        #암호코드 맨뒷자리 찾으면....암호코드 스캔할건데...
        #암호코드 맨 뒷자리 찾는 작업은
        #암호코드 하나가 7비트니까..8개 암호는 56비트
        #55번 인덱스까지만 암호코드가 있는지 없는지 조사하면됩니다.
        j  = M * 4 - 1  #가로 마지막 인덱스
        while j >= 55:  #j가 55보다 작을때는 암호코드가 시작 불가능
            # 암호코드가 여러행에 걸쳐져 있으니... 첫번째 시작줄에서만 암호코드 스캔시작
            if arr[i][j] == 1 and arr[i-1][j] == 0: #암호코드 스캔 시작
                pwd = list()
                for _ in range(8):
                    #0101형태로 반복되기때문에
                    #1다 읽고, 0읽고, 1읽고, 0읽고 반복
                    #암호코드 네개 영역의 길이를 저장할 변수 선언
                    n2 = n3 = n4 = 0
                    while arr[i][j] == 0:#암호코드 스캔전에, 0은 다 뛰어 넘기
                        j -= 1
                    while arr[i][j] == 1:
                        n4 += 1
                        j -= 1
                    while arr[i][j] == 0:
                        n3 += 1
                        j -= 1
                    while arr[i][j] == 1:
                        n2 += 1
                        j -= 1
                    #암호코드가 늘어났을 수도 있으니까...
                    #원래 비율을 찾기
                    #늘어나기전 비율에서 n2,n3,n4 영역에 항상 길이 1인 영역이 포함되어 있음
                    #n2,n3,n4중에서 최소값 찾기, 최소값: 늘어난 비율
                    #최소값으로 각 영역의 길이 나눠주면, 원래비율
                    min_v = min(n2,n3,n4)
                    n2 /= min_v
                    n3 /= min_v
                    n4 /= min_v
                    n1 = 7 - n2 - n3- n4
                    pwd.insert(0,code[(n1,n2,n3,n4)])
                #pwd가 유효한 암호코드인지 확인
                odd_sum = pwd[0] + pwd[2] + pwd[4] + pwd[6]
                even_sum = pwd[1] + pwd[3] + pwd[5]
                if (odd_sum*3 + even_sum + pwd[7]) % 10 == 0:
                    # 유효한 암호코드
                    result += odd_sum + even_sum +pwd[7]
            j -= 1 # arr[i][j]가 0이면 다음 자리 검사



    return result

#16진수 : 16개 경우의수
hex_dic = {"0" : [0,0,0,0],"1" : [0,0,0,1],"2" : [0,0,1,0],"3" : [0,0,1,1],"4" : [0,1,0,0],"5" : [0,1,0,1],
"6" : [0,1,1,0],"7" : [0,1,1,1],"8" : [1,0,0,0],"9" : [1,0,0,1],"A" : [1,0,1,0],"B" : [1,0,1,1],"C" : [1,1,0,0],
"D" : [1,1,0,1],"E" : [1,1,1,0],"F" : [1,1,1,1]}
code = {(3,2,1,1):0,
        (2,2,2,1):1,
        (2,1,2,2):2,
        (1,4,1,1):3,
        (1,1,3,2):4,
        (1,2,3,1):5,
        (1,1,1,4):6,
        (1,3,1,2):7,
        (1,2,1,3):8,
        (3,1,1,2):9}


T = int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split())
    data = [input() for _ in range(N)]
    arr = list()    #여기에 data를 2진수로 변형한 데이터를 저장
    #16진수를 >>>> 2진수로 변환
    for i in range(N):
        tmp= list() #가로 한 줄에 대한, 2진 코드를 저장할 배열
        for j in range(M):
            tmp += hex_dic[data[i][j]]  #배열 더하기 연산
        arr.append(tmp)
    # for row in arr:
    #     print(row)
    #이진으로 구성되어 있는 암호코드를 스캔
    result = solve()
    print('#{} {}'.format(tc,result))