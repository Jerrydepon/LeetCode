# use set to keep unique name
# usage of split and join
# set.add()
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        email_set = set()
        for email in emails:
            local_name, domain_name = email.split("@")
            local_name ="".join(local_name.split('+')[0].split('.'))
            email = local_name + '@' + domain_name
            email_set.add(email)
        return len(email_set)
        
        # dic = {}
        # for email in emails:
        #     email = email.split('@')
        #     local = email[0].split('+')
        #     local = local[0].replace('.', '')
        #     email = local + '@' + (email[1])
        #     if email in dic:
        #         continue
        #     dic[email] = 1
        # return len(dic)