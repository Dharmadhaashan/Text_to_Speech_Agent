import win32com.client
import sounddevice as sd
import soundfile as sf


class VBTTS:
    def __init__(self):
        self.speaker = win32com.client.Dispatch("SAPI.SpVoice")
        self.default_output = self.speaker.AudioOutput
        self.speaker.Rate = 2

    def text_to_wav(self, text, filename="tts.wav"):
        stream = win32com.client.Dispatch("SAPI.SpFileStream")

        # SSFMCreateForWrite = 3
        stream.Open(filename, 3)

        self.speaker.AudioOutputStream = stream
        self.speaker.Speak(text)

        stream.Close()

        # Restore speakers
        self.speaker.AudioOutput = self.default_output

    def find_vbcable(self):
        devices = sd.query_devices()

        for i, device in enumerate(devices):
            if "CABLE Input" in device["name"]:
                return i

        raise RuntimeError("VB-Cable output device not found.")

    def play_to_vbcable(self, filename="tts.wav"):
        device = self.find_vbcable()

        data, samplerate = sf.read(filename, dtype="float32")

        sd.play(
            data,
            samplerate,
            device=device
        )

        sd.wait()

    def speak(self, text):
        self.text_to_wav(text)
        self.play_to_vbcable()


tts = VBTTS()

tts.speak("""

If I have a meeting scheduled with my manager but an urgent task comes up at the same time, I would speak to my manager as soon as possible. I would be polite and explain the situation clearly.

I would say, "Good morning, I apologize for the inconvenience, but an urgent task has come up that requires my immediate attention. I don't think I will be able to attend our meeting at the scheduled time."

Then, I would request to reschedule the meeting. For example, I would say, "Would it be possible to move our meeting to later today, perhaps at 3:00 p.m., or tomorrow morning? I am happy to meet whenever it is convenient for you."

I would also assure my manager that the meeting is important to me by saying, "I value our discussion, and I want to give it my full attention after I complete this urgent task."


""")