# 백준 9498. 시험 성적

a = (int)(input())
result = ""

if a >= 90 :
    result = "A"
elif a >= 80 :
    result = "B"
elif a >= 70 :
    result = "C"
elif a >= 60 :
    result = "D"
else :
    result = "F"

print(result)