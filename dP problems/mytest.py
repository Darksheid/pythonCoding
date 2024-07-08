from collections import Counter

def hasDuplicates(nums):
    s= Counter(nums)
    for i in s.values():
        if i > 1: return True





def groupAnagrams(strs):
        dp={}
        for index,value in enumerate(strs):
            key="".join(sorted(value))
            if key in dp:
                dp[key]= dp[key] +"#"+value
            else:
                dp[key] = value
        arr=[]
        for values in dp.values():
            if "#" in values:
                arr.append(values.split("#"))
            else:
                arr.append(values)
        return arr


strs = ["act","pots","tops","cat","stop","hat"]
print(groupAnagrams(strs))







