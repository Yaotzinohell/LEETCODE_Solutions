# class Solution(object):
#     def multiply(self, num1, num2):
#         n1,n2=int(num1),int(num2)
#         n3=n1*n2
#         num3=str(n3)
#         return num3

class Solution(object):
    def multiply(self, num1, num2):
        numbers = {"0":0,"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9}
        n1 = numbers[num1[0]]
        n2 = numbers[num2[0]]

        for i in range(1,len(num1)):
            n1 = numbers[num1[i]]+ (n1*10)
        for i in range(1,len(num2)):
            n2 = numbers[num2[i]]+ (n2*10)
        
        return str(n1*n2)