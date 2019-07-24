class Solution:
    def numberToWords(self, num: int) -> str:
        to19 = 'One Two Three Four Five Six Seven Eight Nine Ten Eleven Twelve \
           Thirteen Fourteen Fifteen Sixteen Seventeen Eighteen Nineteen'.split()
        tenth = 'Twenty Thirty Forty Fifty Sixty Seventy Eighty Ninety'.split()
        thousandth = 'Thousand Million Billion'.split()
        def transfer(num, idx=0):
            if num == 0:
                return []
            elif num < 20:
                return [to19[num-1]]
            elif num < 100:
                return [tenth[num//10-2]] + transfer(num%10)
            elif num < 1000:
                return [to19[num//100-1]] + ['Hundred'] + transfer(num%100)
            
            quotient, remain = num//1000, num%1000
            space = [thousandth[idx]] if quotient % 1000 !=0 else []
            return transfer(quotient, idx+1) + space + transfer(remain, 0)
                                             
        return ' '.join(transfer(num, 0)) or 'Zero'
        