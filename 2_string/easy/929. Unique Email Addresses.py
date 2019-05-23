class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        dic = {}
        for email in emails:
            email = email.split('@')
            local = email[0].split('+')
            local = local[0].replace('.', '')
            email = local + '@' + (email[1])
            if email in dic:
                continue
            dic[email] = 1
        return len(dic)