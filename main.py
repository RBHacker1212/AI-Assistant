from core.speech_recognition import listen_command
from core.text_to_speech import speak
from core.ai_engine import ask_openai
from core.commands import open_application

def main():
  speak("System is online. Hello! I am Your AI-Assistant. How can I help you?")
  while True:
    command = listen_command()
    if command:
      command_lower = command.lower()
      if "exit" in command_lower:
        speak("Goodbye!")
        break
      elif "open" in command_lower:
        response = open_application(command_lower)
        speak(response)
      else:
        response = ask_openai(command)
        speak(response)
    else:
      speak("I didn`t understand that. Could you repeat?")

if __name__ == "__main__":
  main()
