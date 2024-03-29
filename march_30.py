def countSubarrays( nums, k: int) -> int:
        n = len(nums)
        res=0
        count =0
        max_element = max(nums)
        
        placeholder=0
        left_pointer =0
        right_pointer=0
        while(count<k and right_pointer<n):

            if nums[right_pointer]==max_element:
                  count = count +1
            if count<k:
                 right_pointer=right_pointer+1
        while(right_pointer<n):
            
            if count==k:
                while(nums[left_pointer]!=max_element):
                      left_pointer=left_pointer+1
                if nums[left_pointer]==max_element:
                    res=res + left_pointer +1
                    count=count-1
                    if left_pointer==n:
                         break
                    left_pointer=left_pointer+1
                    
            elif count<k:
                 
                 right_pointer=right_pointer+1
                 if right_pointer<n:
                 
                    if(nums[right_pointer]==max_element):
                         
                         count=count+1
                    else:
                         res = res + left_pointer
                    
                    

        return res   
answer = countSubarrays([61,23,38,23,56,40,82,56,82,82,82,70,8,69,8,7,19,14,58,42,82,10,82,78,15,82],2)
print(answer)