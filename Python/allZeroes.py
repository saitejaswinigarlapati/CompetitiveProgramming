''' Given an integer array nums, move all zeroes to the end while keeping the order of non-zero elements the same. 

Example:

Input:
[0, 1, 0, 3, 12]

Output:
[1, 3, 12, 0, 0]

'''

def moveZeroes(nums):
    insert_pos = 0
    for num in nums:
        if num != 0:
            nums[insert_pos] = num
            insert_pos += 1
    while insert_pos < len(nums):
        nums[insert_pos] = 0
        insert_pos += 1

    return nums



print(moveZeroes([0, 1, 0, 3, 12]))
