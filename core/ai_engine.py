import openai

openai.api_key = "YOUR-OPENAI-API-KEY"

def ask_openai(prompt):
  try:
    response = openai.Completion.create(
      model = "gpt-4",
      max_tokens=150,
      n=1,
      stop=None,
      temprature=0.7
    )
    return response.choices[0].text.strip()
  except Exception as e:
    return f"Error: {e}"
