# mind the way to present binary, ex. 0b110
class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        start = 0
        while start < len(data):
            byte = data[start]
            if byte >> 7 == 0:
                valid = True
                start += 1
            elif byte >> 5 == 0b110:
                valid = self.checkUTF8(start+1, data, 1)
                start += 2
            elif byte >> 4 == 0b1110:
                valid = self.checkUTF8(start+1, data, 2)
                start += 3
            elif byte >> 3 == 0b11110:
                valid = self.checkUTF8(start+1, data, 3)
                start += 4  
            else:
                return False
            
            if not valid:
                return False
        return True
    
    def checkUTF8(self, begin, data, length):
        if begin + length > len(data):
            return False
        for i in range(begin, begin+length):
            if data[i] >> 6 != 0b10:
                return False
        return True