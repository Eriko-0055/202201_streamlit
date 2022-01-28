import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

st.title('streamlit 超入門')
st.write('DataFrame')

df = pd.DataFrame({
    '1列目':[ 1, 2, 3, 4],
    '2列目':[10,20,30,40]
})
# データフレーム st.write関数で表示
st.write(df)

# データフレーム st.dataframe関数で表示（幅を指定可能）
st.dataframe(df, width=100, height=100)

# データフレーム st.dataframe関数で表示（ハイライト）
# axis=0 ➔列のハイライト、axis=1 ➔行のハイライト
st.dataframe(df.style.highlight_max(axis=0))

# データフレーム st.table関数で表示（ハイライト可能。列の並び替えなど動的な動き不可）
st.table(df.style.highlight_max(axis=0))

# マークダウン
"""
# 章
## 節
### 項
```python
import streamlit as st
import numpy as np
import pandas as pd
```
"""
df_chart = pd.DataFrame(
    np.random.rand(20, 3),
    columns = ['a', 'b', 'c']
)
# 折れ線グラフ（チャート）
st.line_chart(df_chart)

# エリアチャート
st.area_chart(df_chart)

# 棒グラフ（積み上げ）
st.bar_chart(df_chart)


df_map = pd.DataFrame(
    np.random.rand(100, 2)/[50,50] + [35.69, 139.70],
    columns = ['lat', 'lon']
)
# マップ
st.map(df_map)

# 画像の読み込み
Image.open = ('sky.JPG')
st.image(Image, caption='sky', use_column_width=True)





