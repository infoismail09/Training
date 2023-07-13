# 16. Given an array of strings, group the anagrams together. You can return the answer in any order.
# Input: str = ["eat","tea","tan","ate","nat","bat"]
#  Output: [["bat"],["nat","tan"],["ate","eat","tea"

str = ["eat","tea","tan","ate","nat","bat"]

result=[]

for i in range(len(str)):
    for j in range(i+1,len(str)):
        if sorted(str[i])==sorted(str[j]):
            pair=[str[i],str[j]]
            result.append(pair)
print(result)
