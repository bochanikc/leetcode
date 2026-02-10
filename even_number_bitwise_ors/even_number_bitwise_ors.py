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
