import speech_recognition as sr

def listen_command():
  recognizer = sr.Recognizer()
  with sr.Microphone() as source:
    print("Listening for your command...")
    try:
      audio = recognizer.listen(source)
      command = recognizer.recognize_google(audio)
      print(f"You: {command}")
      reeturn command
    except sr.UnknownValueError:
      print("Sorry, I could not understand your voice.")
      return ""
    except sr.RequestError:
      print("There seems to be an issue with the speech recognition service.")
      return ""
