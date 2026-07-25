# 🎙️ Text-to-Speech Agent

A Python-based Text-to-Speech (TTS) engine and virtual microphone routing utility. This repository provides scripts to generate high-quality neural voice speech using Microsoft Edge TTS, as well as route synthesized SAPI audio directly through a Virtual Audio Cable (VB-Cable) into microphone input channels.

---

## ✨ Features

- **🌐 Neural Text-to-Speech (`main.py`)**: Uses `edge-tts` to generate natural-sounding speech across multiple neural voices (e.g., `en-IN-PrabhatNeural`, `en-US-GuyNeural`, `en-GB-RyanNeural`) and plays back the generated MP3 audio directly.
- **🔊 Virtual Audio Cable Input (`new_speech.py`)**: Synthesizes offline audio using Windows Speech API (SAPI), saves it to a WAV stream, and plays it into a VB-Audio Virtual Cable input device using `sounddevice` and `soundfile`.
- **🎙️ Direct Mic Feeding**: Ideal for automated voice agents, virtual assistants, or streaming synthesized responses into applications like Zoom, Teams, Discord, or web-based voice interviews.

---

## 📁 Repository Structure

```text
├── main.py           # Edge Neural TTS generator and player
├── new_speech.py     # SAPI TTS & VB-Cable virtual mic output generator
├── requirements.txt  # Python package dependencies
├── output.mp3        # Sample generated MP3 file
└── tts.wav           # Sample generated WAV file
```

---

## 🛠️ Prerequisites & Installation

### 1. Python Environment
Ensure Python 3.8+ is installed on your system.

### 2. Install Python Dependencies
Clone the repository and install the required packages:

```bash
git clone https://github.com/Dharmadhaashan/Text_to_Speech_Agent.git
cd Text_to_Speech_Agent
pip install -r requirements.txt
```

### 3. VB-Audio Cable Setup *(For Virtual Mic Output)*
To use `new_speech.py` for routing audio to microphone inputs:
1. Download and install **VB-Audio Virtual Cable** from [vb-audio.com](https://vb-audio.com/Cable/).
2. Reboot or re-initialize audio devices on Windows.
3. Check that **CABLE Input (VB-Audio Virtual Cable)** is listed in your playback devices.

---

## 🚀 Usage

### 1. Generating Neural Speech (`main.py`)
Synthesize high-quality neural voice audio to `output.mp3` and play it back:

```bash
python main.py
```

- Edit `main.py` to change the prompt text or switch voices:
  - `en-IN-PrabhatNeural` (Default)
  - `en-US-GuyNeural`
  - `en-US-ChristopherNeural`
  - `en-GB-RyanNeural`
  - `en-AU-WilliamNeural`

### 2. Streaming Audio to Virtual Mic (`new_speech.py`)
Synthesize offline audio and play it straight into the VB-Cable input:

```bash
python new_speech.py
```

- **How it works**:
  1. Uses Windows SAPI (`win32com.client.Dispatch("SAPI.SpVoice")`) to synthesize text into `tts.wav`.
  2. Detects the `CABLE Input` device using `sounddevice`.
  3. Plays `tts.wav` directly into the VB-Cable device, making it audible to any application listening to the Virtual Cable microphone.

---

## ⚙️ Configuration & Customization

- **Voice Speed / Rate**:
  - In `main.py`: Modify `rate="+0%"` (e.g., `rate="+10%"` or `rate="-10%"`).
  - In `new_speech.py`: Adjust `self.speaker.Rate = 2` (values typically range from -10 to +10).
- **Pitch**:
  - In `main.py`: Modify `pitch="+0Hz"`.

---

## 📄 License

Distributed under the MIT License. See `LICENSE` for more information.
