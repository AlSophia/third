def is_monotonic(nums):
                inc = True
                dec = True
                for i in range(1,len(nums)):
                    if nums[i] > nums[i-1]:
                        dec = False
                    if nums[i] < nums[i-1]:
                        inc = False
                return inc or dec


print(is_monotonic([3,8,1,5]))
print(is_monotonic([1,9,11,25]))
print(is_monotonic([3,3,11,15]))
