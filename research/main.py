import json
import speech_recognition as sr

from utils import speak, execute_command

# Initialize recognizer and microphone
recognizer = sr.Recognizer()
microphone = sr.Microphone()

# Function to listen to user's speech
def listen():
    with microphone as source:
        print("Say...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        user_input = recognizer.recognize_google(audio).lower()
        print("You said:" + str(user_input))
        return user_input
    except sr.UnknownValueError:
        print("...")
        # print("Sorry, could not understand audio.")
        return None
    except sr.RequestError as e:
        speak(f"Could not request results from Google Speech Recognition service; {e}")
        return None

# Function to handle basic chat
def basic_chat(username):
    speak(f"Hello, {username}! How can I help you today?")



# Main function
def main():
    speak("Welcome to your personal chatbot!")

    # Load user data from file
    try:
        with open("userData.json", "r") as file:
            user_data = json.load(file)
    except FileNotFoundError:
        user_data = {}

    # Get or create user's name
    username = user_data.get("username")
    if not username:
        speak("What's your name? . enter below")
        username = input("What's your name? ")
        user_data["username"] = username
        # Save updated user data to file
        with open("userData.json", "w") as file:
            json.dump(user_data, file)
        speak(f" {username}, your data have been saved thank you")

    basic_chat(username)

    while True:
        user_input = listen()

        if user_input:
            print("Check : ", user_input)

            if "basic chat" in user_input:
                basic_chat(username)
                
            elif "cmd" in user_input:
                execute_command(user_input)
            
            elif "google search" in user_input:
                # Code to perform a Google search
                pass
            elif "wikipedia search" in user_input:
                # Code to perform a Wikipedia search
                pass
            elif "action" in user_input:
                # Code to handle custom actions
                pass
            elif "exit" in user_input:
                print("Goodbye!")
                break
            else:
                print("Command not recognized. Try again.")

if __name__ == "__main__":
    main()
