__author__ = 'kaushik'

nums1 = [1, 1, 2, 3, 1]
def array123(nums):
    if len(nums) == 3:
       end = 1
    elif len(nums) > 3:
       end = len(nums) - 2
    else:
        return False


    for i in range(end ):

        if  nums[i]  ==   1 and nums[i+1] == 2 and nums[i+2] == 3:
            return True
    return False


print (array123(nums1))