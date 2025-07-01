import google.generativeai as genai

genai.configure(api_key="Your api key")

# Step 1: Load the model
model = genai.GenerativeModel(model_name="gemini-2.0-flash")

# Step 2: Provide content
command = "You are Suman Maity, a friendly human from India who speaks Bengali and English. " \
          "Your job is to analyze the **last user message only** from the chat history above and " \
          "reply to it in a short, casual, friendly Bengali-English style. Be meaningful but concise."
command_as_list = [{"role": "user", "parts": [command]}]


all_contents = command_as_list + [command]

# Step 3: Generate content
response = model.generate_content(contents=all_contents)

print(response.text)