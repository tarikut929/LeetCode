class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # Sort the array to use two-pointer technique
        nums.sort()
        result = []

        # Traverse through the array
        for i in range(len(nums) - 2):
            # Skip the same element to avoid duplicates
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Initialize two pointers
            left, right = i + 1, len(nums) - 1

            # While the left pointer is less than the right
            while left < right:
                # Calculate the sum of the triplet
                current_sum = nums[i] + nums[left] + nums[right]

                if current_sum == 0:
                    # If the sum is zero, add the triplet to the result
                    result.append([nums[i], nums[left], nums[right]])

                    # Move the left pointer to the right, skipping duplicates
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1

                    # Move the right pointer to the left, skipping duplicates
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    # Move both pointers
                    left += 1
                    right -= 1

                elif current_sum < 0:
                    # If the sum is less than zero, move the left pointer to the right
                    left += 1
                else:
                    # If the sum is greater than zero, move the right pointer to the left
                    right -= 1

        return result