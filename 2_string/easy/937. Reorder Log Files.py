class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letter_list = []
        digit_list = []
        for log in logs:
            if log.split(' ')[1].isdigit():
                digit_list.append(log)
            else:
                letter_list.append(log)
        letter_list.sort(key = lambda p: p.split(' ')[0])
        letter_list.sort(key = lambda p: p.split(' ')[1:])
        letter_list += digit_list
        return letter_list