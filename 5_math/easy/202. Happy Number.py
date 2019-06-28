class Solution:
    def isHappy(self, n: int) -> bool:
        tmp_list = []
        while True:  
            sum_ = sum(int(i)**2 for i in str(n))
            if sum_ == 1:
                return True
            elif sum_ in tmp_list:
                return False
            else:
                n = sum_
                tmp_list.append(sum_)
        