import requests
import wave

def test_speech_to_text():
    # Replace with the path to your WAV audio file
    audio_file_path = 'output.wav'
    
    with open(audio_file_path, 'rb') as audio_file:
        # response = requests.post('http://your-flask-server-ip:5000/speech-to-text', data=audio_file.read())
        response = requests.post('https://personalesp32chatbot.atharvapawar.repl.co/speech-to-text', data=audio_file.read())
    
    if response.status_code == 200:
        result = response.json()
        print(f'Speech-to-Text Result: {result["text"]}')
    else:
        print(f'Error: {response.status_code}, {response.text}')

def test_text_to_speech(text):
    # response = requests.post('http://your-flask-server-ip:5000/text-to-speech', data={'text': text})
    response = requests.post('https://personalesp32chatbot.atharvapawar.repl.co/text-to-speech', data={'text': text})
    
    if response.status_code == 200:
        with open('output.mp3', 'wb') as output_file:
            output_file.write(response.content)
        print('Text-to-Speech conversion successful. Output saved as output.mp3')
    else:
        print(f'Error: {response.status_code}, {response.text}')

if __name__ == "__main__":
    # Test Speech-to-Text
    test_speech_to_text()

    # Test Text-to-Speech
    text_to_speech_text = "Hello, this is a test. I got the text."
    test_text_to_speech(text_to_speech_text)
