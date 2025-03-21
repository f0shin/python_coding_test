# 백준 10828. 스택

import sys

rp = int(sys.stdin.readline().rstrip())

stk = []

for i in range(0, rp) :
    temp = sys.stdin.readline()

    cmd = ""
    num = 0
    result = 0

    if temp.count(" ") > 0 :
        cmd = temp.split(" ")[0]
        num = int(temp.split(" ")[1])
    else :
        cmd = temp
    
    if "push" in cmd :
        stk.append(num)
    
    if "pop" in cmd :
        if len(stk) > 0 :
            result = stk.pop()
        else :
            result = -1
    
    if "size" in cmd :
        result = len(stk)

    if "top" in cmd :
        if len(stk) > 0 :
            result = stk[len(stk) - 1]
        else :
            result = -1

    if "empty" in cmd :
        if len(stk) == 0 :
            result = 1
        else :
            result = 0
    
    if "push" not in cmd :
        strResult = str(result) + "\n"
        sys.stdout.write(strResult)