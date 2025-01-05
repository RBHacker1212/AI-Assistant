from core.speech_recognition import listen_command
from core.text_to_speech import speak

def main():
  while True:
    command = listen_command()
    if command:
      if "hello"in command.lower():
        speak("Hello! How can I help you today?")
      elif "exit" in command.lower():
        speak("Goodbye!")
        break
      else:
        speak("I didn`t understand that. Could you repeat?")

def __name__ == "__main__":
  main()
