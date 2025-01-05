import openai

openai.api_key = "YOUR-OPENAI-API-KEY"

def ask_openai(prompt):
  try:
    response = openai.ChatCompletion.create(
        model = "gpt-4",
        messages=[
            {"role":"system","content":"You are a helpful assistant"},
            {"role":"user","content":prompt}
        ]
    )
    return response['choices'][0]['message']['content']
  except Exception as e:
    return f"Error: {e}"
