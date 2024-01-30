import openai
import os

OPENAI_API_KEY='6e65e9d2d05c4c9a8560cdc88595e14f'
OPENAI_API_ENDPOINT='https://sktfly2.openai.azure.com/'
OPENAI_API_TYPE = 'azure'
OEPNAI_API_VERSION = '2023-05-15'

openai.api_key = OPENAI_API_KEY
openai.azure_endpoint = OPENAI_API_ENDPOINT
openai.api_type = OPENAI_API_TYPE
openai.api_version = OEPNAI_API_VERSION

query = '나 지금 너무 힘들어.. 위로해줘'

# T의 대답
result = openai.chat.completions.create(
    model='dev-model',
    temperature=0,
    messages=[
        {'role':'system', 'content':'you are a helpful assistant.'},
        {'role':'user', 'content':query}
    ]
)

# F의 대답
result2 = openai.chat.completions.create(
    model='dev-model',
    temperature=1,
    messages=[
        {'role':'system', 'content':'you are a helpful assistant.'},
        {'role':'user', 'content':query}
    ]
)

print(result.choices[0].message.content)

print(result2.choices[0].message.content)