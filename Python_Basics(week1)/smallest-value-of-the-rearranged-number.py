class Solution:
    def smallestNumber(self, num: int) -> int:
        arr = []
        temp = num
        if num<0:
            temp = -1*num
        while temp > 0:
            arr.append(temp % 10)
            temp = temp // 10
        
        
        res = num
        if res > 0:
            arr.sort()
            
            i = 1
            while arr[0] == 0:
                if arr[i] != 0:
                    arr[0],arr[i] = arr[i],arr[0]
                
                i +=1
        else:
            arr = sorted(arr,reverse=True)
        
            
        
        
        poww = 0
        cur = 0
        for i in range(len(arr)-1,-1,-1):
            cur += 10**poww * arr[i] 
            poww +=1

        return cur if num >0 else -cur



