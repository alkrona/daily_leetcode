def maxSubarrayLength(nums,k:int)->int:
    n,l,d,max_sa,r = len(nums),0,{},0,0
    while(r<n):
        print(d)
        if nums[r] not in d:
            d[nums[r]]=1
            
        else:
            d[nums[r]]+=1
        while(l<=r and d[nums[r]]>k ):
            d[nums[l]]-=1
            l+=1
        max_sa=max(max_sa,r-l+1)
        r+=1
    return max_sa
print(maxSubarrayLength([1],1))