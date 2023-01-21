import openai
import os

# Set the API key
openai.api_key = os.environ.get('OPENAI_API_KEY')

# Define the prompt
prompt = input('Digite sua pergunta: ')

# Generate text
response = openai.Completion.create(engine="text-davinci-002", prompt=prompt)

# Print the generated text
print(response["choices"][0]["text"])
