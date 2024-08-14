from langchain import OpenAI, ConversationChain
from langchain.prompts import PromptTemplate
from langchain.llms import HuggingFaceHub

llm = HuggingFaceHub(repo_id="EleutherAI/gpt-neo-2.7B")

conversation = ConversationChain(llm=llm, verbose=True)

context = "El texto de entrada sobre el que deseas hacer preguntas."
question = "¿Cuál es la idea principal del texto?"
prompt = f"{context}\n\nPregunta: {question}\nRespuesta:"

response = conversation.predict(prompt=prompt)
print(response)
