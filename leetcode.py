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


# # 1365. How Many Numbers Are Smaller Than the Current Number
# class Solution(object):
#     def smallerNumbersThanCurrent(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[int]
#         """
#         result=[]
#         for i in nums:
#             count=0
#             for j in nums:
#                 if j<i:
#                     count +=1
#             result.append(count)
#         return result 


#66 ONE PLUS

# class Solution(object):
#     def plusOne(self, digits):
#         """
#         :type digits: List[int]
#         :rtype: List[int]
#         """
#         for i in range (len(digits)-1, -1 ,-1):
#             if digits[i]<9:
#                 digits[i] +=1
#                 return digits
#             else:
#                 digits[i] =0
#         return [1]+digits


#485 Max Consecutive Number
# class Solution(object):
#     def findMaxConsecutiveOnes(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         # tup = tuple(nums)
#         max=0
#         total=0
#         for i in nums:
#             if i == 1:
#                  total += 1
#                  if total > max:
#                      max = total
#             else:
#                 total =0
#         return max


#349 Intersection of Two Arrays
# class Solution(object):
#     def intersection(self, nums1, nums2):
#         """
#         :type nums1: List[int]
#         :type nums2: List[int]
#         :rtype: List[int]
#         """
#         return list((set(nums1)).intersection(set(nums2)))


#217 Contain Duplicates
# class Solution(object):
#     def containsDuplicate(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: bool
#         """
#         n = set(nums)
#         return len(nums)!= len(n)


# 1920. Build Array from Permutation
# class Solution(object):
#     def buildArray(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[int]
#         """
#         ans = []
#         for i in range(len(nums)):
#             ans.append(nums[nums[i]])
#         return ans


#977. Squares of a Sorted Array

# class Solution(object):
#     def sortedSquares(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[int]
#         """
#         sqr = []
#         for i in nums:
#             sqr.append(i*i)
#             sqr.sort()
#         return sqr
        

# 1480. Running Sum of 1d Array
# class Solution(object):
#     def runningSum(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[int]
#         """
#         runningSum = []
#         total=0
#         for i in nums:
#              total += i
#              runningSum.append(total)

#         return runningSum



#191. Number of 1 Bits
# class Solution(object):
#     def hammingWeight(self, n):
#         """
#         :type n: int
#         :rtype: int
#         """
#         return bin(n).count('1')


#1108. Defanging an IP Address
# class Solution(object):
#     def defangIPaddr(self, address):
#         """
#         :type address: str
#         :rtype: str
#         """
#         return address.replace(".","[.]")


#412 FIZZ BUZZ
# class Solution(object):
#     def fizzBuzz(self, n):
#         """
#         :type n: int
#         :rtype: List[str]
#         """
#         result=[]
#         for i in range (1,n+1):
#          if(i%3==0 and i%5==0):
#            result.append("FizzBuzz")
#          elif (i%3==0):
#            result.append("Fizz")
#          elif(i%5==0):
#            result.append("Buzz")
#          else:
#            result.append(str(i))
#         return result




