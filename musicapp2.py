import streamlit as st
import librosa

st.title("Amaj7")
st.write("Upload a file")

uploaded_file = st.file_uploader(
    "Select file",
    type=["mp3", "wav"]
)

if uploaded_file is not None:
    y, sr = librosa.load(uploaded_file, sr=None)

    duration = librosa.get_duration(y=y, sr=sr)

    tempo, beats = librosa.beat.beat_track(y=y, sr=sr)

    st.write("File uploaded")
    st.write(f"The CD spins for {round(duration, 2)} seconds")
    st.write(f"Tempo (BPM): {round(float(tempo), 2)}")
