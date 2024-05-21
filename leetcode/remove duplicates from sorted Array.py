def removeDuplicates(nums):
    duplicates = {}
    for i in nums:
        if i not in duplicates:
            duplicates[i] = 1
        else:
            duplicates[i] += 1

    return list(duplicates.keys())



print(removeDuplicates([0,0,1,1,1,2,2,3,3,4]))



def removeDuplicates2(nums):
    i=0
    while i<len(nums)-1:
        if nums[i]==nums[i+1]:
            nums.pop(i+1)
            nums.append(69)
        else:
            i+=1

    return nums

print(removeDuplicates2([0,0,1,1,1,2,2,3,3,4]))