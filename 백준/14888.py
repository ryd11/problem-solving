from itertools import permutations
import sys

sys.stdin = open('Sample_input.txt', 'r')

#계산을 위해 함수 생성
def calc(a, b, x):
    if x == 0:
        return a + b
    elif x == 1:
        return a - b
    elif x == 2:
        return int(a * b)
    elif x == 3:
        return int(a / b)

#연산자 구하기
def oper_sel():
    global n, oper_list
    row = oper.copy()
    col_fir = [0]*row[0] + [1]*row[1] + [2]*row[2] + [3]*row[3]
    oper_list = list(permutations(col_fir, (n-1)))
    
    for i in range(len(oper_list)-1):
        j = i+1
        while j > (len(oper_list)):
            if oper_list[i] == oper_list[j]:
                del oper_list[j]
            j += 1
    return
    
#최대값, 최솟값 구하기
def check():
    global Min, Max, n, oper_list
    i = 0
    result = 0
    
    for i in range(len(oper_list)):
        y = oper_list[i]
        check_list = num_list.copy()
        for j in range(n-1):
            if j == 0:
                a = check_list.pop(0)    
                b = check_list.pop(0)
                l = y[j]
                result = calc(a,b,l)
            else:
                b = check_list.pop(0)
                l = y[j]
                result = calc(result,b,l)
        Max = max(Max, result)
        Min = min(Min, result)
    return

n = int(input())
Min, Max = 121, -121
num_list = list(map(int, input().split()))
oper = list(map(int, input().split(" ")))
oper_list = []
oper_sel()
check()

print("{}\n{}".format(Max,Min))