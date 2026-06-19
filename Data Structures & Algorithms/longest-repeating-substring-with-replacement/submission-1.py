from collections import Counter

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_len_single = 0
        left, right = 0, k + 1
        counts = None
        while right <= len(s):
            print(f"{left=}, {right=}")
            print(f"{counts=}")
            counts = Counter(s[left:right]) if counts is None else counts
            max_count = max(counts.values())
            if right - left - max_count <= k:
                max_len_single = max(max_len_single, right - left)
                if right < len(s):
                    right += 1
                    counts[s[right-1]] = counts.get(s[right-1], 0) + 1
                else: 
                    return max_len_single
            else:
                counts[s[left]] = counts[s[left]] - 1
                left += 1
        return max_len_single