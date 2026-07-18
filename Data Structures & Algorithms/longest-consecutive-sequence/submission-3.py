class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        overall_longest = 0

        looker = set(nums)

        for j in looker:
            if (j - 1) in looker:
                continue

            longest_seen = 1
            while (j + longest_seen) in looker:
                longest_seen += 1

            if overall_longest < longest_seen:
                overall_longest = longest_seen

        return overall_longest