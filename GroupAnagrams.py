class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        n = len(strs)
        dic = {}
        for str in strs:
            key = ''.join(sorted(str))
            if key in dic:
                dic.get(key).append(str)
            else:
                dic[key] = [str]
        return dic.values()