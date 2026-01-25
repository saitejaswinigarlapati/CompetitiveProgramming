t=int(input())
for _ in range(t):
    n,s,x=map(int,input().split())
    arr=list(map(int,input().split()))
    
    curr_sum=sum(arr)
    
    if curr_sum <= s or (s- curr_sum)%x ==0:
        print("Yes")
    else:
        print("No")