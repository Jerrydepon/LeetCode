# use two pointers for insert position and char
# increase length and char position by 1 if the char is the same as previous one
# replace the char at insert position
# (mind how to deal with count > 10 and count = 1)
class Solution:
    def compress(self, chars: List[str]) -> int:
        left = i = 0
        while i < len(chars):
            char, length = chars[i], 1
            while (i + 1) < len(chars) and char == chars[i + 1]:
                length += 1
                i += 1
            chars[left] = char
            if length > 1:
                len_str = str(length)
                chars[left + 1:left + 1 + len(len_str)] = len_str
                left += len(len_str)
            left += 1
            i += 1
        return left
    
#         if chars == []:
#             return 0

#         tmp = chars[0]
#         cnt = 1
#         idx = 1
#         for i in range(1, len(chars)):
#             if chars[i] != tmp:
#                 if cnt == 1:
#                     chars[idx] = chars[i]
#                     idx += 1
#                 else:
#                     for dig in str(cnt):
#                         chars[idx] = dig
#                         idx += 1
#                     chars[idx] = chars[i]
#                     idx += 1
#                 tmp = chars[i]
#                 cnt = 1
#             else:
#                 cnt += 1
#         if cnt > 1:
#             for dig in str(cnt):
#                 chars[idx] = dig
#                 idx += 1
#         return idx
                
            