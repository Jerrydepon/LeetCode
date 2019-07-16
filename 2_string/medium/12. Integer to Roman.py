class Solution:
    def intToRoman(self, num: int) -> str:
        roman_li = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
        num_li = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9 ,5, 4, 1]
        i, res = 0, ''       
        while num:
            times = num // num_li[i]
            res += times * roman_li[i]
            num %= num_li[i]
            i += 1
        return res
                