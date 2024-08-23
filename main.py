from pytube import YouTube
from moviepy.editor import VideoFileClip
import os
import assemblyai as aai
import google.generativeai as genai
from assemblyai import Transcriber

# Replace these with your actual API keys
aai.settings.api_key = "916c78e1a7184e2bb57a05aa0a709671"
genai.configure(api_key="AIzaSyA5l0n22kuaTBpbgVxyjhn-_X4elb0rThA")

def download_video(video_url):
    yt = YouTube(video_url)
    video_stream = yt.streams.filter(only_audio=False, file_extension='mp4').first()
    video_path = video_stream.download()
    return video_path

def extract_audio(video_path, output_audio_file="output_audio.mp3"):
    video_clip = VideoFileClip(video_path)
    audio_clip = video_clip.audio
    audio_clip.write_audiofile(output_audio_file)
    audio_clip.close()
    video_clip.close()
    return output_audio_file

def transcribe_audio(audio_path):
    transcriber = Transcriber()
    transcript = transcriber.transcribe(audio_path)
    
    # Debug statement to check the type and content of transcript
    # print(f"Transcript type: {type(transcript)}")
    # print(f"Transcript content: {transcript}")
    
    # Assuming the Transcript class has a 'text' attribute
    if hasattr(transcript, 'text'):
        return transcript.text
    else:
        raise TypeError("The transcription result is not in the expected format.")

def summarize_text(text):
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content(f"""Analyze the following context and 
                                          present it as topics and corresponding content 
                                          as in an essay and rephrase:
                                          {text}""")
    
    # Debug statement to check the type and content of response
    # print(f"Summary response type: {type(response)}")
    # print(f"Summary response content: {response}")
    
    # Adapt this part based on the actual structure of response
    if hasattr(response, 'text'):
        return response.text  # Assuming response.text contains the summarized text
    elif hasattr(response, 'text_parts'):
        return ' '.join(part['text'] for part in response.text_parts)
    else:
        raise TypeError("The summary result is not in the expected format.")

def process_video_url(video_url):
    video_path = download_video(video_url)
    print("the video Path is "+video_path)
    audio_path = extract_audio(video_path)
    print("the audio Path is "+audio_path)
    os.remove(video_path)  # Optional: remove video file to save space
    transcript_text = transcribe_audio(audio_path)
    summary = summarize_text(transcript_text)
    return summary


if __name__ =='__main__':
    # video_url = 'https://www.youtube.com/watch?v=Nx4bvwU0DqE'
#     # process_video_url(video_url)
#     audio_path = "output_audio.mp3"
    transcription_text = transcribe_audio("output_audio.mp3")
    # print("Transcripted Text \n"+transcription_text)
    final = summarize_text(transcription_text)
    print("The summarized value \n"+final)
