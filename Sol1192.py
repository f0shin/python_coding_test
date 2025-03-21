import sys

def findFraction (x) :
    fract = {}
    # 0-분자: 1 ~ 2 -> 3 ~ 1 -> 1 ~ 4 ...
    # 1-분모: 2 ~ 1 -> 1 ~ 3 -> 4 ~ 1 ...

    i = 2
    rp = 2

    while 1 :
        if rp % 2 == 0 : # rp가 짝수인 경우 : 0-분자 증가, 1-분모
            fract[0] = 1
            fract[1] = rp

            for _ in range(0, rp) :
                if i > x :
                    return fract

                fract[0] += 1
                fract[1] -= 1

                i += 1
        else : # // rp가 홀수인 경우 : 0-분자 감소, 1-분모 증가
            fract[0] = rp
            fract[1] = 1

            for _ in range(0, rp) :
                if i > x :
                    return fract

                fract[0] -= 1
                fract[1] += 1

                i += 1

    
        rp += 1


x = int(sys.stdin.readline().rstrip())

fract = { 1, 1 }

if x > 1 :
    fract = findFraction((x - 1))

sys.stdout.write(str(fract[0]) + "/" + str(fract[1]))