from collections import defaultdict


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        L = len(s)
        for i in range(L):
            tmp_res = 1
            tmp_s = set(s[i])
            for j in range(i + 1, L):
                if s[j] not in tmp_s:
                    tmp_res += 1
                    tmp_s.add(s[j])
                else:
                    break
            res = max(res, tmp_res)
        return res

class Solution2:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n < 2:
            return n

        left = 0
        lookup = {s[left]: left}
        right = left + 1
        longestSubstring = -sys.maxsize

        """
            This problem can be solved by using Sliding Window Technique.
            Lets define the window size to be of length 2, left pointer on 0 and right on 1.
            Now we will keep on increasing the window size by incrementing right by 1 and store each element with its index in a hashmap which will help us to check for repeated element in O(1) time.            
            If at any point the element at right index is repeating then update the position of left pointer based on the following condition-
            1. If the repeated element is present at right side of left pointer, then update left with previous index of element at right + 1 so that the repeated value is ignored in current window size.
            2. Else, no need to update left pointer as repeated value is already behind the current window size.
            In the hashmap, store/update the most recent index of the current element.
        """
        while right < n:
            if s[right] in lookup:
                left = max(lookup[s[right]] + 1, left)

            lookup[s[right]] = right
            longestSubstring = max(longestSubstring, right - left + 1)
            right += 1

        return longestSubstring


if __name__ == "__main__":
    s = " "
    print(Solution().lengthOfLongestSubstring(s))
