import google.generativeai as genai

GEMINI_API_KEY = "AIzaSyDBzPbHUv3t95KuuBEWIwPIaGbaBglzBPU"
genai.configure(api_key=GEMINI_API_KEY)


model = genai.GenerativeModel('gemini-1.5-pro-latest')

def wrap_gemini_dialog(messages: list):
    formatted_messages = []
    for msg in messages:
        formatted_messages.append(f"{msg['role']}: {msg['content']}")
    input_prompt = "\n".join(formatted_messages)

    response = model.generate_content(input_prompt)
    return response.text
    