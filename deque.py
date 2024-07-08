# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque
d = deque()
n = int(input())
for i in range(1,n+1):
    s = input()
    s = list(s.split())
    if s[0] == "append":
        d.append(int(s[1]))
    elif s[0] == "appendleft":
        d.appendleft(int(s[1]))
    elif s[0] == "pop":
        d.pop()
    elif s[0] == "popleft":
        d.popleft()
    elif s[0] == "clear":
        d.clear()
    elif s[0] == "extend":
        d.extend(s[1])
    elif s[0] == "extendleft":
        d.extendleft(s[1])
    elif s[0] == "remove":
        d.remove(s[1])
    elif s[0] == "reverse":
        d.reverse()
    elif s[0] == "rotate":
        d.rotate(s[1])
print(*d)