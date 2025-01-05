import os webbrowser

def open_application(app_name):
  try:
    if "browser" in app_name:
      webbrowser.open("https://www.google.com")
      return "Opening your browser."
    elif "notepad" in app_name:
      os.system("notepad")
      return "Opening Notepad."
    elif "calculator" in app_name:
      return "Opening Calculator", os.system("calc")
    else:
      return "I cannot open that application yet."
  except Exception as e:
    return f"Error while opening  application: {e}"
