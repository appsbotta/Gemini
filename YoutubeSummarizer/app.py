import streamlit as st
from dotenv import load_dotenv
load_dotenv()
import os
import google.generativeai as genai
from youtube_transcript_api import YouTubeTranscriptApi

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

prompt = "You are an youtube video summarizer. You will be taking the transcript text and summarizing the entire video and providing important summary in points with in 250 words. The transcript text is appended here : "

def generateContent(transcript,prompt):
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(prompt + transcript)
    return response.text

def transcriptContent(url):
    try:
        videoId = url.split("=")[1]
        transcriptText = YouTubeTranscriptApi.get_transcript(video_id=videoId)

        transcript = ""
        for i in transcriptText:
            transcript += " " + i["text"]
        
        return transcript
    
    except Exception as e:
        raise e
    
st.title("YouTube Video Summarizer")
youtbelink = st.text_input("Enter Youtube video Link")

if youtbelink:
    videoId = youtbelink.split("=")[1]
    st.image(f"http://img.youtube.com/vi/{videoId}/0.jpg",use_column_width=True)
    
if st.button("Summarize"):
    transcriptText = transcriptContent(youtbelink)

    if transcriptText:
        summary = generateContent(transcriptText,prompt)
        st.markdown("Detailed Summary in less than 250 words")
        st.write(summary)
