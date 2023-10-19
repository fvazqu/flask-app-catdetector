# ChatGPT Part
import openai

openai.api_key = "{your_api_key}"
messages = [{"role": "system", "content": "You are a intelligent assistant."}]

def chat_with_gpt(input_text):
    message = input_text
    if message:
      messages.append(
          {"role": "user", "content": message},
      )
      chat = openai.ChatCompletion.create(
          model="gpt-3.5-turbo", messages=messages
      )

    reply = chat.choices[0].message.content

    # print(f"ChatGPT: {reply}")
    chat_response = f"ChatGPT: {reply}"
    messages.append({"role": "assistant", "content": reply})
    print(chat_response)
    return chat_response