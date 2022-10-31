"""
pandas 的使用总结
1. 取时间区间, data_range
2.


pd.TimeStamp() 可以将时间戳转成日期
pd.sort_values(col) 根据哪一列来排序
pd.to_numpy() 二维数组
pd.iloc[]    选取指定的值
"""

import pandas as pd
import numpy as np

data_range = pd.date_range(start="20220811", end="20220812", freq="H")

# 1.怎么创建一个pd Object
# pd.Series()
# 可以传一个二维数组, 或者字典
dates = pd.date_range(start="20221022", periods=6)
df1 = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list("ABCD"))
print(df1)

df2 = pd.DataFrame({
    "A": "fff",
    "B": 1111,
    "C": [11, 2, 3, 4]
})

print(df2)
print(df2.iloc[3, 2])

