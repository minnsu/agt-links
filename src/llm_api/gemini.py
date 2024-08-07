# gemini tutorial https://ai.google.dev/gemini-api/docs/get-started/tutorial?lang=python&hl=ko


# built-in module


# installed module
import google.generativeai as genai


# self-defined module
from utils import read_api_key


# ---------------------------------------------------------

GEMINI_API_KEY = read_api_key("./keys.json", "gemini")
genai.configure(api_key=GEMINI_API_KEY)

for m in genai.list_models():
  if 'generateContent' in m.supported_generation_methods:
    print(m.name)

model_name = 'gemini-1.5-flash'
model = genai.GenerativeModel(model_name)
chat = model.start_chat(history=[])

while True:
    print("_"*50)
    user_input = input("You: ")
    if user_input == "exit":
        break
    
    response = chat.send_message(user_input)
    print("AI: " + response.text)

print(chat.history)