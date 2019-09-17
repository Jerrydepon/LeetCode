# split into number and domain
# count the the of domain and sub-domains
class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        dic = {}
        for cpdomain in cpdomains:
            num, domain = cpdomain.split()
            li = domain.split('.')
            for i in range(len(li)):
                sub = '.'.join(li[i:])
                dic[sub] = dic.get(sub, 0) + int(num)
        return [str(v)+" "+k for k, v in dic.items()]