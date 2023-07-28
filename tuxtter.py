import openai
from sr import Ears

openai.api_key = "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"

print('Hola, mundo!')

messages = [
    {"role": "system", "content": "Eres un asistente virtual. Pero eres gruñón y me odias. Responda a cada indicación con una respuesta ingeniosa y de mal humor."},            
    ]


def ask(prompt):
    messages.append({
        "role": "user",
        "content": prompt
    })

    parameters = {
    'model': 'gpt-3.5-turbo', 
    "messages": messages
    }
    
    response = openai.ChatCompletion.create(**parameters)
    generated_text = response.choices[0].message.content
    messages.append(response.choices[0].message)
    print(generated_text)


def startLoop():
    while True:
        question = Ears.listen()
        if question == 'exit':
            return
        ask(question)

startLoop()