import openai
import os

openai.api_key = os.environ.get('OPENAI_API_KEY') # Definir a variável de ambiente com a API_KEY gerada no site do ChatGPT.

prompt = input('Digite sua pergunta: ')

response = openai.Completion.create(engine="text-davinci-002", prompt=prompt)

print(response["choices"][0]["text"])
