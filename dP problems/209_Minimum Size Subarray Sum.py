def minSubArrayLen(target,nums):
    start,end,s=0,0,nums[0]
    n=len(nums)
    minlen=float('inf')

    while True:
        if s>=target:
            minlen = min(minlen,end-start+1)
            s=s-nums[start]
            start+=1
        else :
            end+=1
            if end>=n : break
            s=s+nums[end]
            
    return minlen if minlen != float('inf') else 0
    

nums=[1,1,1,1,1,1,1,1]
target=11
print(minSubArrayLen(target,nums))
