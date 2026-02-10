# def remove_duplicates_in_array1(nums: list[int]) -> int:
#     new_array = [nums[0]]
#     for num in nums:
#         print(num)
#         if num not in new_array:
#             new_array.append(num)
#     nums = new_array.copy()
#     return len(nums), nums

import math
import random
import pytest
from typing import Optional


def remove_duplicates_in_array2(nums: list[int]) -> int:
    remove_arr = []
    count = 0
    check_num = None
    for num in nums:
        # print(num, nums)
        if num == check_num:
            remove_arr.append(num)
        count += 1
        check_num = num
    #print(remove_arr)
    for num in remove_arr:
        nums.remove(num)
    print(len(nums), nums)
    return len(nums)

def remove_duplicates_in_array3(nums: list[int]) -> int:
    nums[:] = sorted(set(nums))
    return len(nums)

# print(remove_duplicates_in_array3([0,0,1,1,1,2,2,3,3,4]))
# print(remove_duplicates_in_array3([1,1,2]))


def reverse(x: int) -> int:
    # print(str(x)[::-1])
    min = -2147483648
    max = 2147483648 - 1

    if x < min or x > max:
        return 0
    elif x < 0:
        res = int(f'-{str(x)[:0:-1]}')
    else:
        res = int(str(x)[::-1])

    if res < min or res > max:
        return 0
    else:
        return res

# print(reverse(-123))
# print(reverse(123))
# print(reverse(120))
# print(reverse(1534236469))




# [4,5,1,9]
# 5
# ListNode{val: 5, next: ListNode{val: 1, next: ListNode{val: 9, next: None}}}
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.val
    
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        copy = nums1[0:m].copy()
        nums1.clear()
        nums1.extend(copy)
        nums1.extend(nums2)
        nums1.sort()
        print(nums1)
    
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        flag = True
        values = []
        if head.next is None:
            head = None
            return head
        values.append(head.val)
        while flag:
            values.append(head.next.val)
            head.val = head.next.val
            head.next = head.next.next
            print(head)
            if head.next == None:
                # print(head.val)
                # print(head.next)
                flag = False
                values.pop(len(values)-n)
                print(values)
                print(head)
        head.val = values[len(values)-2]
        head.next = ListNode(values[len(values)-1], None)
        for i in range(len(values)-3, -1, -1):
            head = ListNode(values[i], head)
            # print(head)
        return head

result = Solution()
num1 = [1, 2, 3, 0, 0, 0]
m = 3
num2 = [2, 5, 6]
n = 3
# result.merge(num1, m, num2, n);
# print(num1)
# num3 = [1,2,3,4,5]
# result.removeNthFromEnd(num3, 2)
# print(num3)

class Solution:
    def __init__(self):
        self.results = {}

    def climbStairs(self, n: int) -> int:
        # print(n, '-------------------')
        # print(self.results)

        self.results[0] = 1
        self.results[1] = 1
        if n <= 1:
            return self.results[0]
        elif n-1 in self.results.keys():
            val1 = self.results[n-1]
            if n-2 in self.results.keys():
                val2 = self.results[n-2]
            else:
                val2 = self.climbStairs(n - 2)
            self.results[n] = val1 + val2
            return self.results[n]
        else:
            self.results[n] = self.climbStairs(n - 1) + self.climbStairs(n - 2)
            return self.results[n]

result = Solution()
# print(result.climbStairs(0))
# print(result.climbStairs(1))
# print(result.climbStairs(2))
# print(result.climbStairs(3))
# print(result.climbStairs(4))
# print(result.climbStairs(5))
# print(result.climbStairs(44))

        

class Solution_2006:

    def __init__(self, nums: list[int]):
        self.reset_nums = nums.copy()
        self.nums = nums
        

    def reset(self) -> list[int]:
        self.nums = self.reset_nums.copy()
        return self.reset_nums

    def shuffle(self) -> list[int]:
        # print('_____________shuffle')
        shuffle_nums = []
        iteration = len(self.nums)
        for i in range(iteration):
            rand_num = random.randint(0, len(self.nums)-1)
            # print(rand_num)
            shuffle_nums.append(self.nums[rand_num])
            self.nums.pop(rand_num)
            # print(self.nums)
            # print('len ',len(self.nums))
        self.nums = shuffle_nums.copy()
        return shuffle_nums
        


# Your Solution object will be instantiated and called as such:
nums = [1, 2, 3, 4, 5, 6, 7, 99, 45, 334, 222]
obj = Solution_2006(nums)
param_1 = obj.reset()
param_2 = obj.shuffle()
# print(param_1)
# print(param_2)



class Solution_2106:
    def fizzBuzz(self, n: int) -> list[str]:
        print('__________fizzBuzz')
        res_arr = []
        for i in range(1, n+1):
            print(f'{i} % 3 =', i % 3)
            if i % 3 == 0 and i % 5 == 0:
                res_arr.append('FizzBuzz')
            elif i % 3 == 0:
                res_arr.append('Fizz')
            elif i % 5 == 0:
                res_arr.append('Buzz')
            else:
                res_arr.append(f'{i}')
        return res_arr


res1 = Solution_2106()
# print(res1.fizzBuzz(15))

class Solution_2406:
    def hammingWeight(self, n: int) -> int:
        print(f'_{n}_______hammingWeight_______')
        count = n
        res = ''
        while count >= 1:
            # print('______________________')
            res = res + f'{count % 2}'
            count = count // 2
            # print(f'{count} % 2', res)
            # print(f'{count} // 2', count)
        res = res[::-1]
        # res = int(res)
        weight = 0
        for i in res:
            if i == '1':
                weight = weight + 1
        return weight
            


res2 = Solution_2406()
# print(res2.hammingWeight(3))
# print(res2.hammingWeight(19))
# print(res2.hammingWeight(20))
# print(res2.hammingWeight(11))
# print(res2.hammingWeight(128))
# print(res2.hammingWeight(2147483645))

# хуета
# class Solution_2506:
#     def maxProfit(self, prices: list[int]) -> int:
#         len_prices = len(prices)
#         count = 0
#         for price in prices:
            

# res3 = Solution_2506()
# print(res3.maxProfit([7,1,5,3,6,4]))

class Solution_2506:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(k):
            dig = nums[len(nums)-1]
            nums.pop(len(nums)-1)
            nums.insert(0, dig)
        
res3 = Solution_2506()
nums = [-1,-100,3,99]
res3.rotate(nums, 2)
# print(nums)


class Solution_2606:
    def firstUniqChar(self, s: str) -> int:
        for i in range(len(s)):
            # print(s[i], s[i+1:])
            if s[i] not in s[i+1:]:
                # print(i, s[i+1:])
                return i
        return -1
        # voc = []
        # for i in range(len(s)):
        #     print(s[i], s[i+1:], voc)
        #     if s[i] not in s[i+1:] and s[i] not in voc:
        #         print(i, s[i+1:])
        #         return i
        #     else:
        #         voc.append(s[i])
        # return -1
        # for i in range(1, len(s)):
        #     print(i, s[i-1])
        #     print(i, s[i])
        #     if s[i-1] != s[i]:
        #         return i-1

res4 = Solution_2606()
# print(res4.firstUniqChar('leetcode'))
# print(res4.firstUniqChar('loveleetcode'))
# print(res4.firstUniqChar('aabb'))


# The isBadVersion API is already defined for you.
def isBadVersion(version: int) -> bool:
    if version >= 50:
        return True
    else:
        return False

class Solution_2806:
    def firstBadVersion(self, n: int) -> int:
        max = n
        min = 1
        check = n // 2
        badVersion = n

        if isBadVersion(min) is True:
            return min

        while max - min != 1:
            if isBadVersion(check) is True:
                max = check
                badVersion = check
                check = check // 2
            else:
                min = check
                check = ((max - min) // 2) + min
            # print('max___', max)
            # print('min____', min)
            # print('check____', check)
            # print('badVersion____', badVersion)
        return badVersion
        
        


res5 = Solution_2806()
# print("5 res_____",res5.firstBadVersion(500))
# print("6 res_____",res5.firstBadVersion(62131241))


class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        # print('______top',self.stack)
        # copy = []
        # for val in self.stack:
        #     if val is not None:
        #         copy.append(val)
        return self.stack[len(self.stack)-1]

    def getMin(self) -> int:
        # copy = []
        # for val in self.stack:
        #     if val is not None:
        #         copy.append(val)
        copy = self.stack.copy()
        copy.sort()
        return copy[0]


# Your MinStack object will be instantiated and called as such:
obj = MinStack()
# values = [-2,0,-1]
# for val in values:
#     obj.push(val)
# # obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# print(param_3)
# print(param_4)


class Solution_0307:
    def countPrimes(self, n: int) -> int:
        count = 0
        for i in range(1, n+1):
            print(i)
            if i % 2 == 0 and i % 3 == 0 and i % 5 == 0 and i not in [2, 3, 5]:
                continue
            else:
                count = count + 1 
        return count

# res = Solution_0307()
# print(res.countPrimes(10))


class Solution_0407:
    def isAnagram(self, s: str, t: str) -> bool:
        s_strip = list(s)
        t_strip = list(t)
        if len(s_strip) != len(t_strip):
            return False
        for char in t_strip:
            if char in s_strip:
                s_strip.remove(char)
            else:
                return False
        return True

    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        res = ''
        for char in s:
            if char.isalpha() or char.isalnum():
                res = res + char
        if res == res[::-1]:
            return True
        else:
            return False
        

res = Solution_0407()
# print(res.isAnagram('rat', 'tra'))
# print(res.isAnagram('rat', 'car'))
# print(res.isAnagram('ab', 'a'))
# print(res.isPalindrome('A man, a plan, a canal: Panama'))
# print(res.isPalindrome('A manddd, a plan, a canal: Panama'))
# print(res.isPalindrome("0P"))


class Solution_0807:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)
    def longestCommonPrefix(self, strs: list[str]) -> str:
        prefix = ''
        min_len = len(strs[0])
        test = ''
        for st in strs:
            if min_len > len(st):
                min_len = len(st)
        if len(strs) != 0:
            if strs[0] != '':
                test = strs[0][0]
            else:
                return prefix
        else:
            return prefix
        print(test)
        print(min_len)
        for i in range(0, min_len):
            test = strs[0][i]
            for st in strs:
                if st[i] == test:
                    continue
                else:
                    return prefix
            prefix = prefix + st[i]
        return prefix
            



res = Solution_0807()
# print(res.strStr("sadbutsad", "sad"))
# print(res.strStr("leetcode", "leeto"))
# print(res.longestCommonPrefix(["flower","flow","flight"]))
# print(res.longestCommonPrefix([""]))


class Solution_0907:
    def missingNumber(self, nums: list[int]) -> int:
        # min_num = nums[0]
        # max_num = nums[0]
        min_num = 0
        max_num = len(nums)+1
        # for num in nums:
        #     if min_num > num:
        #         min_num = num
        #     if max_num < num:
        #         max_num = num
        
        for i in range(min_num, max_num):
            if i not in nums:
                return i

res = Solution_0907()
# print(res.missingNumber([9,6,4,2,3,5,7,0,1]))
# print(res.missingNumber([3,0,1]))
# print(res.missingNumber([0,1]))

class Solution_1107:
    def reverseParentheses(self, s: str) -> str:
        n = len(s)
        open_parentheses_indices = []
        pair = [0] * n
        print(pair)

        # First pass: Pair up parentheses
        for i in range(n):
            print('open_parentheses_indices', open_parentheses_indices)
            if s[i] == "(":
                open_parentheses_indices.append(i)
            if s[i] == ")":
                j = open_parentheses_indices.pop()
                pair[i] = j
                pair[j] = i
                print(i, j)

        # Second pass: Build the result string
        result = []
        curr_index = 0
        direction = 1

        while curr_index < n:
            if s[curr_index] == "(" or s[curr_index] == ")":
                print(curr_index, direction)
                curr_index = pair[curr_index]
                direction = -direction
            else:
                print(s[curr_index])
                result.append(s[curr_index])
            curr_index += direction
            print(curr_index)

        return "".join(result)
        # in_indexes = set()
        # out_indexes = set()
        # flag = True
        # in_index = 0
        # out_index = 0
        # while True:
        #     if in_index == s.find('(', in_index) and out_index == s.find(')', out_index):
        #         break
        #     in_index = s.find('(', in_index) + 1
        #     out_index = s.find(')', out_index) + 1
        #     in_indexes.add(in_index)
        #     out_indexes.add(out_index)
        #     print(in_index)
        #     print(out_index)
        # print(in_indexes)
        # print(out_indexes)
        # return s
        # test = {}
        # count = 0
        # for char in s:
        #     # print(char)
        #     if char == '(':
        #         count += 1
        #         test[count] = ''
        #         continue
        #     elif char == ')':
        #         test[count] = test[count][::-1]
        #         count -= 1
        #         continue
        #     elif count > 0:
        #         print(test, count)
        #         test[count] += char
        #     else:
        #         print('test', test)
        # print(test)
        # test = s
        # test.rfind
        # while True:
        #     print(test)
        #     in_del = test.find('(')
        #     out_del = test.rfind(')')
        #     print(in_del, out_del)
        #     if in_del or out_del == -1:
        #         break
        #     test = test[out_del-1:in_del:-1]
        #     test.replace(')', '(')
        #     print(test)
        # return test

res = Solution_1107()
# print(res.reverseParentheses('(ytrewq)'))
# print(res.reverseParentheses('(ed(et(oc))el)'))


class Solution_1507:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        if x == x[::-1]:
            return True
        else:
            return False
    def lengthOfLastWord(self, s: str) -> int:
        words = s.split()
        return len(words[len(words)-1])

res = Solution_1507()
# print(res.isPalindrome(121))
# print(res.isPalindrome(-121))
# print(res.isPalindrome(21))
#print(res.lengthOfLastWord("   fly me   to   the moon  "))



class Solution_1002:
    def evenNumberBitwiseORs(self, nums: list[int]) -> int:
        check = 0
        for num in nums:
            #print(num)
            if (num % 2 == 0):
                #print(check, num)
                check = check | num
        return check


res = Solution_1002()
print(res.evenNumberBitwiseORs([1,2,3,4,5,6]))
print(res.evenNumberBitwiseORs([7,9,11]))
print(res.evenNumberBitwiseORs([1,8,16]))
