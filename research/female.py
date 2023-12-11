import pyttsx3

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

# Function to list available voices
def list_voices():
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    
    print("Available Female Voices:")
    for idx, voice in enumerate(voices):
        if "female" in voice.name.lower():
            voice_info = f"{idx + 1}. ID: {voice.id}, Name: {voice.name}"
            if hasattr(voice, 'languages') and voice.languages:
                voice_info += f", Lang: {voice.languages[0]}"
            print(voice_info)

# Function to set a specific female voice
def set_female_voice():
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    
    female_voices = [voice for voice in voices if "female" in voice.name.lower()]
    
    if female_voices:
        selected_voice = female_voices[0]
        engine.setProperty('voice', selected_voice.id)
        print(f"Female voice set to ID: {selected_voice.id}, Name: {selected_voice.name}")
        if hasattr(selected_voice, 'languages') and selected_voice.languages:
            print(f"Lang: {selected_voice.languages[0]}")
    else:
        print("No female voice found.")

# Example usage
list_voices()
# Set the desired female voice
set_female_voice()
speak("Hello, how can I help you today?")
