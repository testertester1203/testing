#%%
from llama_index.llms.groq import Groq

llm = Groq(model = 'llama3-70b-8192', api_key = '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')

#%%
from llama_index.core.llms import ChatMessage

messages = [
    ChatMessage(
        role="system", 
        content="compare them, and combine them if they are the same or close to the same. The output please equalize with the input."
    ),
    ChatMessage(role="user", content="{'1': 'Tugu Insurance', '2': 'AXA Indonesia', '3': 'Asuransi Avrist', '4': 'Asuransi Sinar Mas', '5': 'Asuransi Astra', '6': 'ACA Finance', '7': 'Zurich Insurance', '8': 'Asuransi Jasindo', '9': 'Asuransi Sompo', '10': 'Asuransi Mega', '11': 'Asuransi Allianz', '12': 'Asuransi Wahana Tata', '13': 'Asuransi Jasa Raharja Putra', '1000': 'Tidak tahu'}, {'1': 'Tugu Insurance', '2': 'AXA Indonesia', '3': 'Asuransi Avrist', '4': 'Asuransi Sinar Mas', '5': 'Asuransi Astra', '6': 'ACA Finance', '7': 'Zurich Insurance', '8': 'Asuransi Jasindo', '9': 'Asuransi Sompo', '10': 'Asuransi Mega', '11': 'Asuransi Allianz', '12': 'Aswata', '13': 'Asuransi Jasa Raharja Putra', '999': 'Lainnya:...', '1000': 'Tidak tahu'}"),
]
response = llm.chat(messages)
text = response.message.content
start_index = text.find('{')
end_index = text.rfind('}') + 1
extract_text = text[start_index:end_index]
print(extract_text)
# %%
