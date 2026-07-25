import asyncio
import edge_tts
from playsound3 import playsound

# -----------------------------
# Configuration
# -----------------------------

#VOICE = "en-US-GuyNeural"      # Male Voice
#VOICE = "en-US-ChristopherNeural"
#VOICE = "en-GB-RyanNeural"
VOICE = "en-IN-PrabhatNeural" #good
#VOICE = "en-AU-WilliamNeural"
OUTPUT_FILE = "output.mp3"

TEXT = """
Hello everyone.

My name is Dharma.

I am currently persuring my B.Tech degree in Computer Science and Engineering at the Amrita vishwa vidyapeetham chennai campus . 

i am very interested in learning new technologies and exploring the world of programming.
"""

# -----------------------------
# Text to Speech Function
# -----------------------------

async def text_to_speech():
    communicate = edge_tts.Communicate(
        text=TEXT,
        voice=VOICE,
        rate="+0%",
        pitch="+0Hz"
    )

    await communicate.save(OUTPUT_FILE)

# -----------------------------
# Main Function
# -----------------------------

def main():
    print("Generating speech...")

    asyncio.run(text_to_speech())

    print("Speech generated successfully!")

    playsound(OUTPUT_FILE)

    print("Finished speaking.")

if __name__ == "__main__":
    main()