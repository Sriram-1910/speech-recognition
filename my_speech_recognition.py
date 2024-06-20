import speech_recognition as sr
import pyttsx3

# Initialize the recognizer and the text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Function to recognize speech with extended time limit
def recognize_speech():
    with sr.Microphone() as source:
        print("Listening...")

        # Adjust for ambient noise
        recognizer.adjust_for_ambient_noise(source)

        # Capture the audio with extended time limit
        audio = recognizer.listen(source, timeout=5)

        try:
            print("Recognizing...")
            # Use Google Web Speech API to recognize the audio
            text = recognizer.recognize_google(audio)
            print("You said:", text)

            # Speak back the recognized text
            speak_text(text)
        except sr.UnknownValueError:
            print("Sorry, I couldn't understand what you said.")
            speak_text("Sorry, I couldn't understand what you said.")
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))
            speak_text("Could not request results. Please try again later.")

# Function to convert text to speech
def speak_text(text):
    engine.say(text)
    engine.runAndWait()

# Main function to start speech recognition
def main():
    print("Welcome to the Speech Recognition System!")
    speak_text("Welcome to the Speech Recognition System!")

    while True:
        choice = input("Press 'Enter' to start speaking (or 'Q' to quit): ").strip().lower()
        if choice == 'q':
            print("Exiting...")
            speak_text("Exiting the Speech Recognition System. goodbye!")
            break
        else:
            recognize_speech()

# Entry point of the program
if __name__ == "__main__":
    main()
