class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        collect={}
        for word in strs:
            freq=[0]*26
            for char in word:
                index=ord(char)-ord('a')
                freq[index]+=1
            key=tuple(freq)
            if key not in collect:
                collect[key]=[]
            collect[key].append(word)
        return list(collect.values())
             


