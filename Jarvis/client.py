import google.generativeai as genai

genai.configure(api_key="your api key")

model = genai.GenerativeModel("gemini-pro")
response = model.generate_content("Say something funny about AI.")
print(genai.list_models())


