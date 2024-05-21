def moveZeros(nums):



    for i in range(1,len(nums)):
        pointer=i-1
        if nums[pointer]==0:
            nums.pop(pointer)
            nums.append(0)

    return nums



print(moveZeros([12,312,512,30,0,457,0,346,0]))