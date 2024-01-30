import openai
import os
import streamlit as st
"""document

st.text_area : https://docs.streamlit.io/library/api-reference/widgets/st.text_area
"""


OPENAI_API_KEY='6e65e9d2d05c4c9a8560cdc88595e14f'
OPENAI_API_ENDPOINT='https://sktfly2.openai.azure.com/'
OPENAI_API_TYPE = 'azure'
OEPNAI_API_VERSION = '2023-05-15'

openai.api_key = OPENAI_API_KEY
openai.azure_endpoint = OPENAI_API_ENDPOINT
openai.api_type = OPENAI_API_TYPE
openai.api_version = OEPNAI_API_VERSION

st.header('welcome to AI Poem', divider='rainbow')
st.write('아름다운 시를 함께 지어보아요')

name = st.text_input('작가의 이름을 입력하세요')
if name:
    st.write(f'{name}님 반갑습니다.')

subject = st.text_input('시의 주제를 입력하세요')
content = st.text_area('시의 내용을 입력하세요')

button_click = st.button("RUN")

if button_click:
    with st.spinner('please wait...'):
    
        result = openai.chat.completions.create(
            model='dev-model',
            temperature=1,
            messages=[
                {'role':'system', 'content':'you are a helpful assistant.'},
                {'role':'user', 'content':f'작가의 이름은 {name}'},
                {'role':'user', 'content':f'시의 주제는 {subject}'},
                {'role':'user', 'content':f'시의 내용은 {content}'},
                {'role':'user', 'content':f'이 정보로 시를 생성해줘.'}
            ]
        )

        st.success('done!')
        st.write(result.choices[0].message.content)
        