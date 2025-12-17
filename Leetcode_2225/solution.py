class Solution(object):
    def findWinners(self, matches):
        """
        :type matches: List[List[int]]
        :rtype: List[List[int]]
        """
        losers_dict = {}
        losers = [m[1] for m in matches]
        winners = [m[0] for m in matches]
        never_lost = sorted(set(winners) - set(losers))
        for lose in losers:
            losers_dict[lose] = losers_dict.get(lose, 0) + 1
        lost_once=[]
        for key,values in losers_dict.items():
            if values==1:
                lost_once.append(key)
        lost_once = sorted(lost_once)
        return [never_lost, lost_once]