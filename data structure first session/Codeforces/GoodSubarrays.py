for _ in range(int(input())):
    n = int(input())
    arr = input()
    
    prefix = 0
    dic = {0:1}
    ans = 0
    
    for i in range(n):
        prefix += int(arr[i])
        x = prefix -  (i+1)
        if x not in dic:
            dic[x] = 1
        else:
           ans += dic[x]
           dic[x] +=1
        
        
    print(ans)