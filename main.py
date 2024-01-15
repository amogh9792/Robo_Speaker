import pyttsx3

def speak_text():
    # Initialize the text-to-speech engine
    engine = pyttsx3.init()

    try:
        while True:
            print("Welcome to RoboSpeaker 1.1. Created by Amogh")
            x = input("Enter what you want me to speak (press 'q' to exit): ")

            # Validate input to prevent potential security issues
            if x.lower() == 'q':
                break  # Exit the loop if the user enters 'q'
            elif not x.strip():  # Check if the input is empty or contains only whitespace
                print("Input is empty. Please enter something.")
            else:
                # Speak the input
                engine.say(x)

                # Wait for the speech to finish
                engine.runAndWait()

    except KeyboardInterrupt:
        print("\nExiting RoboSpeaker. Goodbye!")

if __name__ == "__main__":
    speak_text()
