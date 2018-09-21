class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        len1 = len(nums1)
        len2 = len(nums2)
        len3 = len1+len2
        result,i,j=0,0,0
        arr = []
        while i<len1 and j<len2:
            if nums1[i]<nums2[j]:
                arr.append(nums1[i])
                i+=1
            elif nums1[i]>=nums2[j]:
                arr.append(nums2[j])
                j+=1

        if i == len1 :
            for r in nums2[j:]:
                arr.append(r)
        else:
            for r in nums1[i:]:
                arr.append(r)

        if len3 % 2 == 0:
            result = (arr[len3//2]+arr[len3//2-1])/2
        else:
            result = arr[(len3-1)//2]
        return result
