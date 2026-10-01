class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        collect={}
        for i in range(len(strs)):
            l=''.join(sorted(strs[i]))
            if l in collect:
                collect[l].append(strs[i])
            if l not in collect:
                collect[l]=[strs[i]]
        return [value for key,value in collect.items()]