import sys
from collections import deque
import heapq
# n = int(sys.stdin.readline())
# li1 = list(map(int,sys.stdin.readline().split()))
li = ["MatKor","WiCys","CyKor","AlKor","$clear"]
li = {i[0]:i for i in li}
print(li[input()])