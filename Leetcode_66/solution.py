class Solution(object):
    def plusOne(self, digits):
        total = 0
        for i in digits:
            total = total*10+i
        total+=1
        arr=[]
        while total!= 0:
            arr.append(total%10)
            total=total//10
        
        return arr[::-1]