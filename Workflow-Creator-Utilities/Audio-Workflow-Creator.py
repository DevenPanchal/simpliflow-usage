import json
import speech_recognition as sr
import pyttsx3
# also installed pyaudio and pocketsphinx

# import from env the API tokens of OpenAI, Whisper, and Google Speech Recognition etc. if needed.

# Initialize the recognizer and text-to-speech engine
recognizer = sr.Recognizer()
tts_engine = pyttsx3.init()

def speak(text):
    """Speak the provided text using text-to-speech."""
    print(f"System: {text}")
    tts_engine.say(text)
    tts_engine.runAndWait()

def listen():
    """Listen to audio from the microphone and return the recognized text."""
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_sphinx(audio)
            print(f"User: {text}")
            return text
        except sr.UnknownValueError:
            speak("Sorry, I did not catch that. Please repeat.")
            return listen()
        except sr.RequestError as e:
            speak("Could not request results; please check your network connection.")
            return ""


def create_workflow():
    # Prompt for overall workflow description
    speak("Please describe the purpose of the workflow.")
    flow_description = listen()
    
    num_agents = 1
    # Ask for the number of agents in the workflow
    speak("How many agents should be in the workflow?")
    num_agents_text = listen()
    num_agents_text = num_agents_text.lower()
    try:
        # replace the spoken number with its integer equivalent
        number_words = {
            "one": 1,
            "two": 2,
            "three": 3,
            "four": 4,
            "five": 5,
            "six": 6,
            "seven": 7,
            "eight": 8,
            "nine": 9,
            "ten": 10
        }
        if num_agents_text in number_words:
            num_agents = number_words[num_agents_text]
            num_agents = int(num_agents)
    except ValueError:
        speak("I could not understand the number. Defaulting to one agent.")
        num_agents = 1
    
    agents = []
    for i in range(num_agents):
        speak(f"Agent {i+1}: What is the name of the agent?")
        name_of_agent = listen()
        
        speak(f"Agent {i+1}: What is the role of this agent?")
        role_of_agent = listen()
        
        speak(f"Agent {i+1}: Describe what this agent should do.")
        what_should_agent_do = listen()
        
        speak(f"Agent {i+1}: Specify the postprocessor function, if any. Say 'None' if no function is needed.")
        postprocessor_function = listen()
        if postprocessor_function.lower() == "none":
            postprocessor_function = None
        
        speak(f"Agent {i+1}: What is the name of the next agent? Say 'None' if this is the last agent.")
        next_agent = listen()
        if next_agent.lower() == "none":
            next_agent = None
        
        agent_data = {
            "head": "True" if i == 0 else "False",
            "name_of_agent": name_of_agent,
            "role_of_agent": role_of_agent,
            "what_should_agent_do": what_should_agent_do,
            "postprocessor_function": postprocessor_function,
            "next": next_agent
        }
        agents.append(agent_data)
    
    # Build the workflow JSON structure
    workflow = {
        "flow_description": flow_description,
        "agents": agents
    }
    
    # Save the workflow JSON to a file
    import os
    workflows_dir = os.path.join(os.getcwd(), "Workflows")
    os.makedirs(workflows_dir, exist_ok=True)
    workflow_file_path = os.path.join(workflows_dir, "Audio-made-workflow.json")
    with open(workflow_file_path, "w") as f:
        json.dump(workflow, f, indent=4)
    
    speak("Workflow JSON has been created and saved as workflow.json.")
    print(json.dumps(workflow, indent=4))

if __name__ == "__main__":
    create_workflow()