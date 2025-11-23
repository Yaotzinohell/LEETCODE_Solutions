class Solution(object):
    def sampleStats(self, count):
        # ---------- 1. Minimum ----------
        minimum = None
        for i in range(256):
            if count[i] > 0:
                minimum = i
                break
        
        # ---------- 2. Maximum ----------
        maximum = None
        for i in range(255, -1, -1):
            if count[i] > 0:
                maximum = i
                break
        
        # ---------- 3. Mean ----------
        total_count = sum(count)
        total_sum = sum(i * count[i] for i in range(256))
        mean = float(total_sum) / total_count
        
        # ---------- 4. Mode ----------
        mode = max(range(256), key=lambda x: count[x])
        
        # ---------- 5. Median ----------
        median = 0
        half1 = (total_count + 1) // 2
        half2 = (total_count + 2) // 2
        
        running = 0
        median_left = None
        median_right = None
        
        for i in range(256):
            running += count[i]
            if median_left is None and running >= half1:
                median_left = i
            if median_right is None and running >= half2:
                median_right = i
                break
        
        median = (median_left + median_right) / 2.0
        
        return [float(minimum), float(maximum), mean, median, float(mode)]
