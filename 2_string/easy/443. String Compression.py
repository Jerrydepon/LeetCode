class Solution:
    def compress(self, chars: List[str]) -> int:
        if chars == []:
            return 0

        tmp = chars[0]
        cnt = 1
        idx = 1
        for i in range(1, len(chars)):
            if chars[i] != tmp:
                if cnt == 1:
                    chars[idx] = chars[i]
                    idx += 1
                else:
                    for dig in str(cnt):
                        chars[idx] = dig
                        idx += 1
                    chars[idx] = chars[i]
                    idx += 1
                tmp = chars[i]
                cnt = 1
            else:
                cnt += 1
        if cnt > 1:
            for dig in str(cnt):
                chars[idx] = dig
                idx += 1
        return idx
                
            