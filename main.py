import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title('streamlit 超入門')

st.write('Iteractive Widgets')

# プログレスバー
'start!'
latest_iteration = st.empty()
bar = st.progress(0)

# プログレスバーを０．１秒ずつ静止して表示していく
for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i + 1)
    time.sleep(0.1)

'Done!!!'

# サイドバーで表示(sidebarを追加)
option = st.sidebar.selectbox(
    'あなたの好きな数字は何ですか？',
    list(range(0, 11))
)
'あなたの好きな数字は',option,'です。'

text = st.sidebar.text_input('あなたの趣味を教えて下さい')
'あなたの趣味：',text

# ２カラムレイアウト
left_column, right_column = st.columns(2)
button = left_column.button('右カラムの文字を表示')
if button:
    right_column.write('ここは右カラムです')

# エクスパンダー
expander = st.expander('問い合わせ')
expander.write('ここに問い合わせ内容を書く')


option2 = st.selectbox(
    'あなたの好きな数字は何ですか？',
    list(range(0, 30))
)
'あなたの好きな数字は',option2,'です。'

text_sec = st.text_input('あなたの好きな漫画を教えて下さい')
'あなたの好きな漫画：',text_sec





