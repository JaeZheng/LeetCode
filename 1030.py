#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : JaeZheng
# @Time    : 2019/4/21 10:32
# @File    : 1030.py


class Solution(object):
    def allCellsDistOrder(self, R, C, r0, c0):
        """
        :type R: int
        :type C: int
        :type r0: int
        :type c0: int
        :rtype: List[List[int]]
        """
        result = []
        max_r_dist = max(abs(R-1-r0), abs(0-r0))
        max_c_dist = max(abs(C-1-c0), abs(0-c0))
        max_dist = max_r_dist + max_c_dist
        total = C*R
        if max_dist == 0:
            return [r0, c0]
        flag = []
        for i in range(R*C):
            flag.append(0)
        queue = []
        queue.append([r0,c0])
        flag[c0*R+r0] = 1
        while len(queue) != 0:
            r, c = queue.pop(0)
            result.append([r, c])
            self.BFS(R, C, r, c, queue, flag)

        return result

    def helper(self, R, C, r, c):
        return True if 0<=r<=R-1 and 0<=c<=C-1 else False

    def BFS(self,R, C, r0, c0, queue, flag):
        if self.helper(R, C, r0-1, c0) and flag[c0*R+r0-1] == 0:
            queue.append([r0-1, c0])
            flag[c0*R+r0-1] = 1
        if self.helper(R, C, r0+1, c0) and flag[c0*R+r0+1] == 0:
            queue.append([r0+1, c0])
            flag[c0*R+r0+1] = 1
        if self.helper(R, C, r0, c0-1) and flag[(c0-1)*R+r0] == 0:
            queue.append([r0, c0-1])
            flag[(c0-1)*R+r0] = 1
        if self.helper(R, C, r0, c0+1) and flag[(c0+1)*R+r0] == 0:
            queue.append([r0, c0+1])
            flag[(c0+1)*R+r0] = 1
        return


solution = Solution()
R=2
C=2
r0=0
c0=1
a = solution.allCellsDistOrder(R,C,r0,c0)
print(a)