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
    ChatMessage(role="user", content="{'1': 'Retail Direct', '2': 'Retail Partner', '3': 'Mendatangi langsung'}, {'1': 'Retail Direct (Nasabah Langsung)', '2': 'Retail Partner (Melalui Partner/Agen)'}"),
]
resp = llm.chat(messages)
print('')
# %%
