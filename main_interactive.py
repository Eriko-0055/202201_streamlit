import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

st.title('streamlit 超入門')

st.write('Interactive Widgets')

# チェックボックス
if st.checkbox('Show image'):
    img = Image.open('sky.jpg')
    st.image(img, caption='sky', use_column_width=True)

# リストボックス
option = st.selectbox(
    'あなたの好きな数字は何ですか？',
    list(range(0, 11))
)

'あなたの好きな数字は',option,'です。'

# テキストボックス（１行）
text = st.text_input('あなたの趣味を教えて下さい')
'あなたの趣味：',text

# テキストボックス（複数行）
text_long = st.text_area('昨日の晩ごはんを教えて下さい')
'あなたの昨日の晩ごはん：',text_long

# スライダー
condition = st.slider('あなたの今の調子は？',0,100,50)
'あなたの今の調子：',condition


