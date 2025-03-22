import streamlit as st
from extract_transcript import get_video_transcript
from summarization import summarize_text

st.title("YouTube Video Summarizer")

video_url = st.text_input("Enter YouTube Video URL:")

if st.button("Summarize"):
    if "youtube.com" in video_url or "youtu.be" in video_url:
        video_id = video_url.split("v=")[-1]  # Extracts ID from URL
        transcript = get_video_transcript(video_id)
        
        if "Error" in transcript:
            st.error("Could not fetch transcript. Try another video.")
        else:
            summary = summarize_text(transcript)
            st.subheader("Summary:")
            st.write(summary)
    else:
        st.error("Invalid YouTube URL")
