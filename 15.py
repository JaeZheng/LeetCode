# 超时
# class Solution:
#     def threeSum(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[List[int]]
#         """
#         if len(nums)<3:
#             return []
#         if len(nums) == 3:
#             if nums[0]+nums[1]+nums[2] == 0:
#                 return [nums]
#             else:
#                 return []
#         result = []
#         idi = 0
#         for val1 in nums[:-1]:
#             idj = idi + 1
#             for val2 in nums[idi+1:-1]:
#                 inv = -(val1+val2)
#                 if inv in nums[idj+1:]:
#                     tmp = [val1, val2, inv]
#                     if sorted(tmp) not in result:
#                         result.append(sorted(tmp))
#                 idj += 1
#             idi += 1
#         return result


class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        nums.sort()
        l_nums = len(nums)
        # 固定一个数，找其他两个数来匹配，达到加和为0
        for i in range(l_nums):
            # 排序后存在两个重复值时，跳过，避免重复计算
            if i>0 and nums[i-1] == nums[i]:
                continue
            target = 0-nums[i]  # 另外两个数的和为当前值的相反数
            left = i+1
            right = l_nums-1
            # 从两边夹逼
            while left < right:
                if nums[left] + nums[right] < target:
                    left += 1  # 如果小于目标值，首部右移，增大
                elif nums[left]+nums[right] > target:
                    right -= 1  # 如果大于目标值，尾部左移，减小
                else:  # 等于目标值
                    result.append([nums[i], nums[left], nums[right]])
                    right -= 1
                    left += 1
                    # 尾部连续两个值相等，索引减一
                    while left<right and nums[right] == nums[right+1]:
                        right -= 1
                    # 首部连续两个值相等，索引加一
                    while left<right and nums[left] == nums[left-1]:
                        left += 1
        return result


s = Solution()
a = [-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6]
b = s.threeSum(a)
print(b)