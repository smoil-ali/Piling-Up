from collections import deque
N=int(input())
temp=0
i,j=0,0
for x in range(N):
    n=int(input())
    cubes=list(map(int,input().split()))
    d=deque(cubes)
    for y in range(n):
        max_val=max(d)
        if d.popleft()==max_val:
            print("Yes")
            break
        elif d.pop()==max_val:
            print("Yes")
            break
        else:
            print("No")
            break 