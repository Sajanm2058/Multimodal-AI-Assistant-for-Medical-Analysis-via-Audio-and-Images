Multimodal-AI-Assistant-for-Medical-Analysis-via-Audio-and-Images
Multimodal AI Assistant: MediVoiceVision (AI-Powered Voice and Vision Healthcare Assistant )for Medical Analysis via Audio and Images

Based on the raw setup guide and project phases you’ve provided, here’s a clean and professional `README.md` file for your project, integrating all instructions and information:

---

````markdown
🩺 MediVoiceVision: Multimodal AI Healthcare Assistant

**MediVoiceVision** is an AI-powered multimodal assistant that enables interactive, voice-based consultations enhanced by image-based diagnostics. Combining state-of-the-art models like **Whisper Large V3** for speech recognition and **LLaMA-4 Scout** for vision and conversation, this assistant simulates a digital doctor capable of interpreting patient voice and medical imagery.

---

📚 Table of Contents

1. [Features](#features)
2. [Installation Guide](#installation-guide)
   - [Install FFmpeg and PortAudio](#install-ffmpeg-and-portaudio)
   - [Set Up Python Environment](#set-up-python-environment)
3. [Running the Project](#running-the-project)
4. [Project Structure](#project-structure)
5. [Disclaimer](#disclaimer)
6. [License](#license)

---

✅ Features

- 🎤 **Speech-to-Text**: Powered by Whisper Large V3  
- 🧠 **Multimodal Reasoning**: Uses LLaMA-4 Scout for intelligent response generation from text + image  
- 🖼️ **Medical Image Input Support**: Upload medical visuals (e.g., X-rays) for enhanced diagnosis  
- 🗣️ **Text-to-Speech**: Converts AI response back to human-like voice  
- 🌐 **Gradio Interface**: Interactive web app for demonstration

---

🛠️ Installation Guide

⚙️ Install FFmpeg and PortAudio

macOS
```bash
# Install Homebrew if not already installed
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Install FFmpeg and PortAudio
brew install ffmpeg portaudio
````

#### Linux (Ubuntu/Debian)

```bash
sudo apt update
sudo apt install ffmpeg portaudio19-dev
```

#### Windows

1. **Download FFmpeg**

   * Visit: [https://ffmpeg.org/download.html](https://ffmpeg.org/download.html)
   * Download the latest Windows static build.

2. **Set FFmpeg Path**

   * Extract to `C:\ffmpeg`
   * Add `C:\ffmpeg\bin` to System PATH

3. **Install PortAudio**

   * Visit: [http://www.portaudio.com/download.html](http://www.portaudio.com/download.html)
   * Follow Windows installation instructions.

---

🐍 Set Up Python Environment

Option 1: Using Pipenv

```bash
pip install pipenv
pipenv install
pipenv shell
```

#### Option 2: Using pip + venv

```bash
python -m venv venv
# macOS/Linux
source venv/bin/activate
# Windows
venv\Scripts\activate

pip install -r requirements.txt
```

#### Option 3: Using Conda

```bash
conda create --name medivoice python=3.11
conda activate medivoice
pip install -r requirements.txt
```

---

▶️ Running the Project

Execute the following in order to simulate a full consultation flow:

### Phase 1: Initialize the Brain (Core AI Logic)

```bash
python brain_of_the_doctor.py
```

### Phase 2: Record Patient’s Voice Input

```bash
python voice_of_the_patient.py
```

### Phase 3: Generate and Play Doctor’s Voice

```bash
python voice_of_the_doctor.py
```

### Phase 4: Launch Gradio Web UI

```bash
python gradio_app.py
```

---

## 📁 Project Structure

```bash
mediVoiceVision/
├── audio_input/                # Raw audio from patients
├── image_input/                # Medical images for diagnosis
├── models/                     # Model wrappers and configs
├── brain_of_the_doctor.py      # Core multimodal processing logic
├── voice_of_the_patient.py     # Records patient voice
├── voice_of_the_doctor.py      # Converts response to speech
├── gradio_app.py               # Gradio-based UI
├── requirements.txt
└── README.md
```

---

⚠️ Disclaimer

> This tool is intended for **research and educational purposes only**. It is **not approved for real-world clinical use** and **should not replace professional medical diagnosis or treatment**.

---



```

---

Let me know if you'd like this saved as a `.md` file or want an additional GitHub badges section (e.g., Python version, license, etc.)!
```
