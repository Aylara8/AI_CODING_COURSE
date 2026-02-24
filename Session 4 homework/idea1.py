import pyttsx3
import json
import os
from textblob import TextBlob # Our AI Library

engine = pyttsx3.init()

def speak(audio):
    print(f"\n[ASTRA]: {audio}")
    engine.say(audio)
    engine.runAndWait()

def get_mood_label(polarity):
    if polarity > 0.3: return "Excited/Happy"
    if polarity < -0.3: return "Stressed/Sad"
    return "Neutral/Calm"

def psychology_session():
    # 1. Load Data
    if not os.path.exists('user_data.json'):
        data = {"name": "User", "interests": [], "mood_history": []}
    else:
        with open('user_data.json', 'r') as f:
            data = json.load(f)

    # 2. Interest Analysis
    speak(f"Before we start, {data['name']}, tell me: what has been on your mind lately?")
    user_input = input("You: ")
    
    # AI ANALYSIS START
    blob = TextBlob(user_input)
    sentiment = blob.sentiment.polarity  # This is the AI math!
    mood = get_mood_label(sentiment)
    # AI ANALYSIS END

    # 3. "Psychologist" Response Logic
    if mood == "Excited/Happy":
        speak(f"I can feel your positive energy about '{user_input}'! That's wonderful for your mental health.")
    elif mood == "Stressed/Sad":
        speak(f"I sense some tension regarding '{user_input}'. Remember to take breaks. Would you like to add a 'Rest' task to your list?")
    else:
        speak(f"I see. '{user_input}' sounds like a significant part of your day. Let's keep an eye on how that develops.")

    # 4. Save to JSON Memory
    data['last_interest'] = user_input
    data['current_mood'] = mood
    with open('user_data.json', 'w') as f:
        json.dump(data, f, indent=4)

if __name__ == "__main__":
    psychology_session()