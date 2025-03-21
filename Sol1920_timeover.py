# 백준 1920. 수 찾기

# 진행중

import sys

def binerySearch(array, target, start, end) :
    if start > end :
        return None
    mid = int((start + end) / 2)

    if array[mid] == target :
        return mid
    elif array[mid] > target :
        return binerySearch(array, target, start, mid - 1)
    else :
        return binerySearch(array, target, mid + 1, end)

rp = int(sys.stdin.readline().rstrip())
num = sys.stdin.readline().rstrip().split(" ")

num.sort()

rp = int(sys.stdin.readline().rstrip())
target = sys.stdin.readline().rstrip().split(" ")

for i in range(0, rp) :
    result = binerySearch(num, target[i], 0, rp - 1)
    if result :
        sys.stdout.write("1\n")
    else :
        sys.stdout.write("0\n")
