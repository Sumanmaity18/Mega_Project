import pyautogui
import time
import pyperclip
import google.generativeai as genai

genai.configure(api_key="your api key")

# Step 1: Load the model
# model = genai.GenerativeModel(model_name="gemini-2.0-flash")

# Step 2: Click on the icon
pyautogui.click(1432, 1046)
time.sleep(1)  # Wait for window/app to open

# Step 3: Drag to select text
pyautogui.moveTo(697, 178)
# pyautogui.moveTo(576, 135)
pyautogui.mouseDown()
pyautogui.moveTo(1859, 902, duration=1.0)
# pyautogui.moveTo(1319, 954, duration=1.0)
pyautogui.mouseUp()

# Step 4: Copy the selected text to clipboard
pyautogui.hotkey('ctrl', 'c')
time.sleep(0.5)  # Give clipboard time to update
pyautogui.click(1861, 917)                               

# Step 5: Get the copied text
copied_text = pyperclip.paste()

# Output the result
print("Copied text:")
print(copied_text)

model = genai.GenerativeModel(model_name="gemini-2.5-flash")
command_as_list = [{"role": "user", "parts": [copied_text]}]

custom_prompt = {"role": "user", "parts": [
    "You are Suman Maity, a friendly human from India who speaks Bengali and English. "
    "Your job is to analyze the **last user message only** from the chat history above and "
    "reply to it in a short, casual, friendly Bengali-English style. Be meaningful but concise."
]}

all_contents = command_as_list + [custom_prompt]

# Step 3: Generate content
response = model.generate_content(contents=all_contents)
reply = response.text.strip()

pyperclip.copy(response.text)

time.sleep(1)
pyautogui.click(861, 969)
time.sleep(0.5)

# Step 2: Paste clipboard content (Ctrl + V)
pyautogui.hotkey('ctrl', 'v')
time.sleep(0.2)

# Step 3: Press Enter
pyautogui.press('enter')
