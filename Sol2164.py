import sys
import queue

rp = int(sys.stdin.readline().rstrip())

q = queue.Queue()

for i in range(0, rp) :
    q.put(i + 1)

while q.qsize() > 1 :
    q.get(0)
    q.put(q.get(0))

sys.stdout.write(str(q.get(0)))