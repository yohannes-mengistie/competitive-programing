n,k = map(int,input().split())
arr= list(map(int,input().split())
dp = [float("inf")]*n
dp[0] = 0

for i in range(n):
    for j in range(1,k+1):
        if i+j < n:
            dp[i+j] = min(dp[i+j],dp[i]+abs(arr[i]-arr[i+j]))
        else:
            break
    
print(dp[n-1])
