import streamlit as st
st.title("User Login Form")
st.text_input("Enter Username")
st.text_input("Enter password",type="password")
st.text_area("Enter paragraph")
st.text("Audio")
st.audio("HELLO!___Akhil___Violin_tune_BGM_(Extended)_sad_and_happy_versions(256k).mp3")
st.audio_input("Speak here")

score = st.slider("Set Your Score", 0, 100, 90)
if score >= 80:
    st.success("Great Job! 🎯")
    st.balloons()
