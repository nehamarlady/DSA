class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        output=[False]*len(candies)
        max_candies=max(candies)
        for i in range (len(candies)):
            current= candies[i]+extraCandies
            if current >= max_candies:
                output[i]=True
            else:
                output[i]=False
        return output