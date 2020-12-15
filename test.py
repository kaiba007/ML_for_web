
class Solution:
    def teoSum(self, nums, target):
        """
        :param nums:   List[int]
        :param target: int
        :return:       List[int]
        """
        for i in range(length(nums)):
            for j in range(length(nums)-1):
                if nums[i] + num[j] === target
                return [i,j]

        for i in nums:
            j = target - nums[i]
            start_index = nums.index(i)
            next_index = start_index + 1
            temp_nums = nums[next_idex: ]
            if j in temp_nums:
                return(nums.index(i), next_index + temp_nums.index(j))

        dict = {}
        for i in range(len(nums)):
            if targrt - nums[i] not in dict:
                dict[nums[i]] = i
            else:
                return [dict[target-nums[i]], i]


















