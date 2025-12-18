# # 202 HAPPY NUMBER
# class Solution(object):
#     def isHappy(self, n):
#         """
#         :type n: int
#         :rtype: bool
#         """
#         a= set()
#         while n!=1 :
#             if n in a:
#                  return False
#             a.add(n)
#             n=sum(int(d)*int(d)for d in str(n) )
#         return True

# # 169 Majority Number
# class Solution(object):
#     def majorityElement(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         d= dict.fromkeys(nums,0)
#         for i in nums:
#             d[i]+=1
#             if d[i]>len(nums)//2:
#                 return i 


# #389 Find the Differnce
# class Solution(object):
#     def findTheDifference(self, s, t):
#         """
#         :type s: str
#         :type t: str
#         :rtype: str
#         """
#         for ch in t:
#             if t.count(ch)> s.count(ch):
#                 return ch 


#136 Single Number
# class Solution(object):
#     def singleNumber(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         ans=0
#         for i in nums:
#             ans= ans^i
#         return ans

# #383 Ransom Note
# class Solution(object):
#     def canConstruct(self, ransomNote, magazine):
#         """
#         :type ransomNote: str
#         :type magazine: str
#         :rtype: bool
#         """
       
#         for ch in set(ransomNote):
#             if ransomNote.count(ch) > magazine.count(ch):
#                 return False
#         return True
        

# #771 Jewels and Stones
# class Solution(object):
#     def numJewelsInStones(self, jewels, stones):
#         """
#         :type jewels: str
#         :type stones: str
#         :rtype: int
#         """
#         count=0
#         for ch in stones:
#             if ch in jewels:
#                 count+=1
#         return count


