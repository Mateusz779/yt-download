import os
import streamlit as st
from pytube import YouTube
st.title("Youtube Video Downloader")
st.subheader("Enter the URL:")
url = st.text_input(label='URL')
files = "/home/ubuntu/yt-download/"
if url != '':
    yt = YouTube(url)
    st.image(yt.thumbnail_url, width=300)
    st.subheader('''
    {}
    ## Length: {} seconds
    ## Rating: {}
    '''.format(yt.title , yt.length , yt.rating))
    video = yt.streams
    if len(video) > 0:
        downloaded , download_audio = False , False
        download_video = st.button("Prepare Video")
        if yt.streams.filter(only_audio=True):
            download_audio = st.button("Prepare Audio Only")
        if download_video:
            video.get_highest_resolution().download()
            downloaded = True
            st.subheader("Prepared Complete")
            with open(yt.title+".mp4","rb") as file:
               btn = st.download_button("Download file", data=file, file_name=yt.title+".mp4" , mime="video/mp4")
        if download_audio:
            video.filter(only_audio=True).first().download()
            downloaded = True
            st.subheader("Prepared Complete")
            with open(yt.title+".mp4","rb") as file:
               btn = st.download_button("Download file", data=file, file_name=yt.title+".mp3", mime="audio/mpeg")
    else:
        st.subheader("Sorry, this video can not be downloaded")
        
    os.remove(yt.title+".mp4")
