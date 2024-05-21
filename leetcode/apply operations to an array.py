def applyOperations(nums):

    for i in range(1,len(nums)):
        if nums[i]==nums[i-1]:
            nums[i-1]=nums[i]*2
            nums[i]=0


    zero_idx=0

    for i in range(len(nums)):
        if nums[i]!=0:
            nums[i],nums[zero_idx]=nums[zero_idx],nums[i]
            zero_idx+=1
    return nums


print(applyOperations([1,2,2,1,1,0]))