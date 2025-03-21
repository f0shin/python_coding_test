# 백준 9012. 괄호

rp = (int)(input())

for i in range(0, rp) :
    target = input()
    result = 1
    cnt = 0

    for j in range(0, len(target)) :
        c = target[j]

        if c == "(" :
            cnt = cnt + 1
        else :
            cnt = cnt - 1
            if cnt < 0 :
                result = 0
    
    if cnt > 0 :
        result = 0

    if result == 1 :
        print("YES")
    else :
        print("NO")

