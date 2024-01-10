for _ in range(int(input())):
    n,m = map(int,input().split())
    arr = list(map(int,input().split()))
    
    arr2 = sorted(arr)
   

    if m > 1 or arr2 == arr:
        print("YES")
    else:
        print("NO")