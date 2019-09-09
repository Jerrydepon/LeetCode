# append word to line if the width is smaller than the line
# if words+space+nextWord is larger than width, equally allocate space between words
# be careful with last word (left-justified)
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res, num_char, line = [], 0, []
        for word in words:
            if num_char + len(line) + len(word) > maxWidth:
                for space_i in range(maxWidth - num_char):
                    line[space_i % (len(line)-1 or 1)] += " "
                res.append("".join(line))
                num_char = 0
                line = []
            num_char += len(word)
            line.append(word)
        remain = " ".join(line)
        return res + [remain + (maxWidth-len(remain))*" "]