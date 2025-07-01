import google.generativeai as genai

genai.configure(api_key="AIzaSyBf3vVZqN62LTr-TTviv6iQGlqHf9rhcaw")

model = genai.GenerativeModel("gemini-pro")
response = model.generate_content("Say something funny about AI.")
print(genai.list_models())


