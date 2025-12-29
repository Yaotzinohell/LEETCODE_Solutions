class Solution(object):
    def angleClock(self, hour, minutes):
        """
        :type hour: int
        :type minutes: int
        :rtype: float
        """
        if hour==12:
            hour=0
        
        theeta = abs(30*hour - 5.5 * minutes)
        angle = min(theeta, 360 - theeta)
        return angle