"""
最长回文字符串
输入：s = "babad"
输出："bab"
输入：s = "cbbd"
输出："bb"

滑动窗口
"""


def longestPalindrome(s):
    for i in range(len(s)):
        l, r = 0, 0
        while l < len(s):
            print(l, r)
            r += 1
        pass

longestPalindrome("bbbbb")

