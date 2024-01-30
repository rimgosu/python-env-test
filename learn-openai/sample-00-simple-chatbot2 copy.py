import openai
import os
import streamlit as st
"""document

https://docs.streamlit.io/library/api-reference/widgets/st.text_input
https://docs.streamlit.io/library/api-reference/widgets/st.button
https://docs.streamlit.io/library/api-reference/status/st.spinner
"""


OPENAI_API_KEY='6e65e9d2d05c4c9a8560cdc88595e14f'
OPENAI_API_ENDPOINT='https://sktfly2.openai.azure.com/'
OPENAI_API_TYPE = 'azure'
OEPNAI_API_VERSION = '2023-05-15'

openai.api_key = OPENAI_API_KEY
openai.azure_endpoint = OPENAI_API_ENDPOINT
openai.api_type = OPENAI_API_TYPE
openai.api_version = OEPNAI_API_VERSION

st.header('welcome to GPT Bot', divider='rainbow')
st.write('궁금한 것을 물어보세요!')

query = st.text_input('Query? ')
button_click = st.button("run")

if button_click:
    with st.spinner('please wait...'):
    
        result = openai.chat.completions.create(
            model='dev-model',
            temperature=0,
            messages=[
                {'role':'system', 'content':'you are a helpful assistant.'},
                {'role':'user', 'content':query}
            ]
        )

        st.write(result.choices[0].message.content)
        st.success('done!')