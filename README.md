# **AI Video Summarizer**

Effortlessly generate detailed and short summaries of YouTube videos, recordings, lectures, podcasts, and audio files using AI models for transcription and summarization. This web app, built using **Streamlit**, integrates advanced AI features like **AssemblyAI** for transcription and **Google's Gemini** for text summarization.

## **Features**

- **File Upload**: Upload video/audio files (MP4/MP3) directly to generate AI-powered summaries.
- **URL Input**: Input a YouTube video URL to extract, transcribe, and summarize its content.
- **Detailed Summary**: Get a detailed breakdown of the content.
- **Short Summary**: Generate a concise summary using NLP models.
- **Real-time Preview**: View the uploaded video/audio and get the output instantly.

---

## **Tech Stack**

- **Frontend**: Streamlit (Python)
- **Backend**: Python
- **APIs**: 
  - [AssemblyAI](https://www.assemblyai.com/) for audio transcription
  - [Google Gemini](https://developers.generativeai.google/) for text summarization
  - [Pytube](https://pytube.io/) for downloading YouTube videos
  - [MoviePy](https://zulko.github.io/moviepy/) for audio extraction
  - [Transformers (Hugging Face)](https://huggingface.co/) for short summaries
  - [YouTube Transcript API](https://github.com/jdepoix/youtube-transcript-api) for fetching YouTube subtitles

---

## **Installation**

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/video-summarizer.git
   cd video-summarizer
