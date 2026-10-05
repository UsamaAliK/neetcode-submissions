class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return "None"
        new_str=":;".join(strs)
        return new_str

    def decode(self, s: str) -> List[str]:
        if s == "None":
            return []        
        orig_list=s.split(":;")
        return orig_list
