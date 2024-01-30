import streamlit as st
import pandas as pd
"""Document
https://docs.streamlit.io/library/api-reference/write-magic/st.write
- 마크다운 문법 완벽지원, pandas 완벽지원
"""



st.header('Welcome to GPT bot',
          divider='rainbow')


st.write('Hello, *World!* :sunglasses: 궁금한 것을 물어보세요')
st.write(1234)
st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40],
}))