import streamlit as st

# Page Configuration 
st.set_page_config(page_title="Reels Audio Promo Hub", layout="centered")

# Title and Intro
st.title("🎧 Reels Audio Promo Hub")
st.write("Welcome! This is your portal to explore and use trending audio from emerging artists supported by Equal Measure Arts (EMA).")

# Artist Selection
artist = st.selectbox("Select an Artist to View Audio Assets:", [
    "Felecia Cruz",
    "Genius Black",
    "Danielle (Aerial Jade)",
    "Portals of Portland"
])

# Sample data for each artist
audio_data = {
    "Felecia Cruz": {
        "title": "Gleaming",
        "link": "https://www.instagram.com/reels/audio/3187564854717114/",
        "preview": "https://sample-videos.com/audio123/mp3/1.mp3",
        "kit": "https://fcgetsit.com",
        "bio": "Felecia Cruz has performed over 2,600 shows across 10 countries and continues to bring her electric blend of rap, hip-hop, DJ, and performance art to audiences around the world. Her beats tell stories — about resilience, adventure, and growth — and through workshops and community engagement, she helps young artists find their voice. Felecia’s journey from Maine jam sessions to international stages proves that creativity knows no borders."
    },
    "Genius Black": {
        "title": "Revolution Now",
        "link": "https://www.instagram.com/reels/audio/234567890/",
        "preview": "https://sample-videos.com/audio123/mp3/2.mp3",
        "kit": "https://yourdomain.com/kits/genius_black_reels_kit.zip",
        "bio": "Hip hop artist, educator, and social justice storyteller."
    },
    "Danielle (Aerial Jade)": {
        "title": "Sky Flow",
        "link": "https://www.instagram.com/reels/audio/345678901/",
        "preview": "https://sample-videos.com/audio123/mp3/3.mp3",
        "kit": "https://yourdomain.com/kits/aerial_jade_reels_kit.zip",
        "bio": "Aerialist and composer creating high-energy, movement-inspired soundscapes."
    },
    "Portals of Portland": {
        "title": "Time Loop",
        "link": "https://www.instagram.com/reels/audio/456789012/",
        "preview": "https://sample-videos.com/audio123/mp3/4.mp3",
        "kit": "https://yourdomain.com/kits/portals_of_portland_reels_kit.zip",
        "bio": "Experimental collective blending ambient music with storytelling."
    }
}

# Display selected artist info
info = audio_data[artist]
st.subheader(info["title"])
st.write(info["bio"])

# Preview audio
st.audio(info["preview"], format='audio/mp3')

# Buttons and links
st.markdown(f"[🎥 Use This Audio on Instagram]({info['link']})")
st.markdown(f"[📦 Download Reels Kit]({info['kit']})")

# Footer
st.markdown("---")
st.caption("This project is supported by Equal Measure Arts (EMA) to uplift emerging artists through social media visibility.")
