class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        triplets = []
        
        for i, num in enumerate(nums):  # Avoids out-of-bounds access
            if i > 0 and num == nums[i - 1]:  # Skip duplicates
                continue
            
            left, right = i + 1, len(nums) - 1

            while left < right:
                total = num + nums[left] + nums[right]

                if total > 0:
                    right -= 1
                elif total < 0:
                    left += 1                
                else:
                    triplets.append([num, nums[left], nums[right]])
                    left += 1

                    while (left < right) and (nums[left] == nums[left - 1]):  # Skip duplicates
                        left += 1


        return triplets
