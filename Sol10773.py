import sys

rp = int(sys.stdin.readline().rstrip())

stk = []

# for i in range(0, rp) :
for _ in range(0, rp) :
    temp = int(sys.stdin.readline().rstrip())

    if temp == 0 :
        try :
            stk.pop()
        except :
            break
    else :
        stk.append(temp)


result = 0

for i in range(0, len(stk)) :
    result += stk[i]

sys.stdout.write(str(result) + "\n")