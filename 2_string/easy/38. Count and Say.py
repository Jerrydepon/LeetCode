class Solution:
    def countAndSay(self, n: int) -> str:
        re = "1"
        for _ in range(n-1):
            tmp, cnt, li = re[0], 0, ""
            for dig in re:
                if dig == tmp:
                    cnt += 1
                else:
                    li += (str(cnt) + str(tmp))
                    tmp = dig
                    cnt = 1
            li += (str(cnt) + str(tmp))
            re = li
        return re
                