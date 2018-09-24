class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        result = []
        nums.sort()
        l_nums = len(nums)
        for i, val in enumerate(nums[:-2]):
            left = i+1
            right = l_nums-1
            # 如果最左边两个加上去都比target大，直接跳出，没必要再比较下去
            if val+nums[left]+nums[left+1] > target:
                result.append(val+nums[left]+nums[left+1])
            # 如果最右边两个加上去都比target小，直接跳出，没必要再比较下去
            elif val+nums[right]+nums[right-1] < target:
                result.append(val+nums[right]+nums[right-1])
            else:
                while left<right:
                    result.append(val+nums[left]+nums[right])
                    if val+nums[left]+nums[right] < target:
                        left += 1
                    elif val+nums[left]+nums[right] > target:
                        right -= 1
                    else:
                        return target  # 出现与target相等，直接返回
            # 将所有可能结果以与target的差的绝对值排序，最终结果为排序后的第0个元素

        result.sort(key=lambda x:abs(x-target))
        return result[0]

nums = [-1,2,1,-4]
target = 1
s = Solution()
result = s.threeSumClosest(nums, target)
print(result)
