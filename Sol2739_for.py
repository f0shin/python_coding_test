# 백준 2739. 구구단

a = (int)(input())

for i in range(1, 10) : # 1 ~ 9
    print("%d * %d = %d" %(a, i, a * i))
    # print(a, "*", i, "=", a * i)