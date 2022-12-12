"""
最长回文字符串
输入：s = "babad"
输出："bab"
输入：s = "cbbd"
输出："bb"

滑动窗口
i\j	0	1	2	3	...
0	True	ba	bab	baba	...
1		True	ab	aba	...
2			True	ba	...
3				True	...
4					True


"""


def longestPalindrome(s):
    size = len(s)
    if size == 1:
        return s
    max_len, start = 1, 0
    dp = [[False for _ in range(size)] for _ in range(size)]
    for i in range(1, size):
        for j in range(i):
            if i-j <= 2:
                if s[i] == s[j]:
                    dp[i][j] = True
                    cur_len = i - j + 1
            else:
                if s[i] == s[j] and dp[i+1][j-1]:
                    dp[i][j] = True
                    cur_len = i - j + 1
            if dp[i][j]:
                if cur_len > max_len:
                    max_len = cur_len
                    start = j
    print(start, max_len)


def my_test(s):
    size = len(s)
    if size <= 1:
        return s
    dp = [[False for _ in range(size)] for _ in range(size)]
    max_len = 1
    start = 0
    for i in range(size):
        for j in range(i):
            print(i, j)
            if i - j <= 2:
                if s[i] == s[j]:
                    dp[i][j] = True
                    cur_len = i - j + 1
            else:
                if s[i] == s[j] and dp[i+1][j-1]:
                    dp[i][j] = True
                    cur_len = i - j + 1
            if cur_len > max_len:
                cur_len = max_len
                start = j
    print(start, max_len)
    pass



longestPalindrome("babad")
my_test("babad")

