class Solution(object):
    def reformatNumber(self, number):
        """
        :type number: str
        :rtype: str
        """
        # phone_number=""
        # number=str(number.replace("-",""))
        # number=str(number.replace(" ",""))
        # if len(number)<=3:
        #     return number
        # else:
        #     while len(number)>4:
        #         phone_number+=number[:3]+"-"
        #         number=number[3:]
        #         if len(number)==2 or len(number)==3:
        #             phone_number+=number
        #             return phone_number
        #         if len(number)==4:
        #             phone_number+=number[:2]+"-"+number[2:]
        #             return phone_number
        #     if len(number)==2 or len(number)==3:
        #             phone_number+=number
        #             return phone_number
        #     if len(number)==4:
        #         phone_number+=number[:2]+"-"+number[2:]
        #         return phone_number

        number = number.replace("-","").replace(" ","")
        res=[]

        while len(number)>4:
            res.append(number[:3])
            number=number[3:]
        
        if len(number)==4:
            res.append(number[:2])
            res.append(number[2:])
        if len(number)==2 or len(number)==3:
            res.append(number)
        
        return "-".join(res)