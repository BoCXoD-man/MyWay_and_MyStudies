

def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    for first_index in range(len(nums)-1):
        print(f'first_index = {first_index}')
        
        for second_index in range(first_index + 1, len(nums)):
            print(f'second_index = {second_index}')
            if nums[first_index] + nums[second_index] == target:
                print('Finish!')
                return [first_index, second_index]



assert twoSum([1,2,3], 5) == [1,2]
assert twoSum([3,3], 6) == [0,1]
assert twoSum([2,7,11,15], 9) == [0,1]