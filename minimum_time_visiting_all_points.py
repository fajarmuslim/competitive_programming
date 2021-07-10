from typing import List


class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:

        res = 0
        x1 = points[0][0]
        y1 = points[0][1]
        for i in range(1, len(points)):
            x2 = points[i][0]
            y2 = points[i][1]

            x2_min_x1 = abs(x2 - x1)
            y2_min_y1 = abs(y2 - y1)

            slope = min(x2_min_x1, y2_min_y1)
            remainder = abs(x2_min_x1 - y2_min_y1)
            res = res + slope + remainder

            x1 = points[i][0]
            y1 = points[i][1]

        return res