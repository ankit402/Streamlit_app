import streamlit as st
from streamlit_webrtc import webrtc_streamer, WebRtcMode, RTCConfiguration

# Set page config
st.set_page_config(page_title="2-Person Video Call", layout="wide")

st.title("🎬 Two-Person Live Video Call")

st.markdown("""
This is a simple peer-to-peer (P2P) video chat.
- Person 1 opens this app.
- Person 2 opens **the same app URL**.
- Both will see and hear each other in real time.
""")

# Use a STUN server for connection
rtc_configuration = RTCConfiguration({
    "iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]
})

# Each connected user will have their own peer connection.
# WebRTC handles the signaling internally for Streamlit sessions.

webrtc_streamer(
    key="video-call",
    mode=WebRtcMode.SENDRECV,  # Send and receive both audio & video
    rtc_configuration=rtc_configuration,
    media_stream_constraints={"video": True, "audio": True},
)
