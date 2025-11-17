class Solution(object):
    def capitalizeTitle(self, title):
        """
        :type title: str
        :rtype: str
        """
        title=title.lower()
        title_list = title.split(" ")
        res=""
        for i in range(len(title_list)):
            if len(title_list[i])>=3:
                title_list[i]=title_list[i].capitalize()
            elif len(title_list[i])<3:
                title_list[i]=title_list[i].lower()
        res=" ".join(title_list)
        return res