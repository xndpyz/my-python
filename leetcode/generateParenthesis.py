"""
回溯法求括号组合
过滤掉不符合条件的
n = 1  ()
n = 2  ()(), (())
"""


def generateParenthesis(n):
    res = []

    def backstack(s, r, l):
        if r > n or l > r:
            return
        if len(s) == 2 * n:
            res.append(s)
            return
        backstack(s + "(", r + 1, l)
        backstack(s + ")", r, l + 1)

    backstack("", 0, 0)
    return res


generateParenthesis(3)
