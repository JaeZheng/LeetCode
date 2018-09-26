# 寻找数组中四数之和
class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        # 采用递归的思路，寻找N数之和可由 确定1个值+寻找N-1个数之和 构成
        def findNsum(left, right, target, N, result, results):
            # 小于2或者剩余数组长度小于所需数字个数时，跳出
            if right-left+1 < N or N < 2 or target < nums[0] * N or target > nums[-1] * N:
                return
            # N = 2 的情况
            if N == 2:
                while left < right:
                    s = nums[left] + nums[right]
                    if s == target:
                        results.append(result + [nums[left], nums[right]])  # 数组中每个元素添加两个新值
                        left += 1
                        right -= 1
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1
                    elif s > target:
                        right -= 1
                    else:
                        left += 1
            else:  # N大于2的情况
                for i in range(left, right+1):
                    if i == left or (i > left and nums[i - 1] != nums[i]):  # 递归
                        findNsum(i+1, right, target-nums[i], N-1, result+[nums[i]], results)
            return
        nums.sort()
        results = []
        findNsum(0, len(nums)-1, target, 4, [], results)
        return results
