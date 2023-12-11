import pyttsx3

import subprocess
import os

from gtts import gTTS
def savespeak(text):
    tts = gTTS(text=text, lang='en')
    tts.save("output.mp3")

savespeak("hello world this is gta")



# Function to speak using text-to-speech
def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

# Function to list available voices
def list_voices():
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    
    print("Available Voices:")
    for idx, voice in enumerate(voices):
        voice_info = f"{idx + 1}. ID: {voice.id}, Name: {voice.name}"
        if hasattr(voice, 'languages') and voice.languages:
            voice_info += f", Lang: {voice.languages[0]}"
        print(voice_info)

# Function to set a specific voice
def set_voice(voice_id):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    
    if 1 <= voice_id <= len(voices):
        selected_voice = voices[voice_id - 1]
        engine.setProperty('voice', selected_voice.id)
        print(f"Voice set to ID: {selected_voice.id}, Name: {selected_voice.name}")
        if hasattr(selected_voice, 'languages') and selected_voice.languages:
            print(f"Lang: {selected_voice.languages[0]}")
    else:
        print("Invalid voice ID")

# Example usage
# list_voices()
# Set the desired voice by providing the ID for Hazel
# set_voice(2)
# speak("Hello, how can I help you today? I am using the Hazel voice.")


# Function to handle command execution
def execute_command(command, data):
    # You can implement various commands based on user input
    if "open notepad" in command:
        subprocess.run(["notepad.exe"])

    elif "create text file" in command:
        file_name = data + ".txt"
        try:
            with open(file_name, "w"):
                pass
            speak(f"Text file '{file_name}' created successfully.")
        except Exception as e:
            speak(f"Error: Failed to create text file '{file_name}'. {str(e)}")

    elif "open text file" in command:
        file_name = data + ".txt"
        try:
            subprocess.run(["notepad.exe", file_name], check=True, shell=True)
        except subprocess.CalledProcessError:
            speak(f"Error: Failed to open text file '{file_name}'. Make sure it exists.")

    elif "open github folder" in command:
        folder_path = r"C:\Users\Atharva Pawar\Documents\GitHub"
        # explorer C:\Users\Atharva Pawar\Documents\GitHub

        try:
            subprocess.run(["explorer", folder_path], check=True, shell=True)
        except subprocess.CalledProcessError:
            speak(f"Error: Failed to open GitHub folder. Make sure the path is correct.")

    elif "shutdown" in command:
        # subprocess.run(["shutdown", "/s", "/t", "1"])
        pass

    elif "cmd create folder" in command:
        substring_to_remove = "cmd create folder"
        result = command.replace(substring_to_remove, "").strip()
        # print("Check : ", result)

        try:
            subprocess.run(["mkdir", result], check=True, shell=True)
            speak(f"Folder '{result}' created successfully.")

        except subprocess.CalledProcessError:
            speak(f"Error: Failed to create folder '{result}'.")

    elif command == "open calculator":
        subprocess.run(["calc.exe"])

    elif command == "open command prompt":
        subprocess.run(["cmd.exe"])

    elif command == "open file explorer":
        subprocess.run(["explorer.exe"])

    elif command == "open control panel":
        subprocess.run(["control.exe"])

    elif command == "open system settings":
        subprocess.run(["control.exe", "sysdm.cpl"])

    elif command == "open task manager":
        subprocess.run(["taskmgr.exe"])

    elif command == "open device manager":
        subprocess.run(["devmgmt.msc"])

    elif command == "open registry editor":
        subprocess.run(["regedit.exe"])

    elif command == "open services":
        subprocess.run(["services.msc"])

    elif command == "open event viewer":
        subprocess.run(["eventvwr.exe"])

    elif command == "open notepad++":
        subprocess.run(["notepad++.exe"])

    else:
        speak("Command not recognized.")
