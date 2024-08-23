import streamlit as st
from main import process_video_url
from shortsummary import youtube_sub, chunk_and_summarize, remove_redundant_sentences, capitalize_sentences_and_combine

# Page configuration
st.set_page_config(
    page_title="Video Summarizer",
    page_icon=":movie_camera:",
    layout="wide"
)

# Add an image and title in separate columns
col1, col2 = st.columns([1, 6])

with col1:
    st.image("download (1).png", use_column_width=False, width=120)

with col2:
    st.markdown("<h1 style='color: #c84e89; font-size: 2.5em; font-family: Pacifico; margin-bottom: 0; padding-top: 20px;'>"
                "Effortlessly Summarize Videos with AI</h1>", unsafe_allow_html=True)
    st.markdown("<p style='font-size: 1em; font-family: Open Sans; margin-top: 0;'>"
                "Generate AI-powered summaries of recordings, YouTube videos, lectures, and podcasts efficiently.</p>",
                unsafe_allow_html=True)

# File upload section
st.markdown("### Upload a Video or Audio File :arrow_up:")
uploaded_file = st.file_uploader("Drag and Drop a Video or Audio file here or Upload a File", type=["mp4", "mp3"], key="file_uploader")

# URL upload section
st.markdown("### Or Upload from URL :link:")
uploaded_url = st.text_input("Enter the link", placeholder="Paste a URL")

# Common submit button
if st.button("Summary :arrow_forward:"):
    if uploaded_file is not None:
        st.success(f":white_check_mark: File {uploaded_file.name} uploaded successfully!")
        # Display the uploaded video
        st.video(uploaded_file)
    elif uploaded_url:
        with st.spinner('⌛ Generating video summary!!!'):
            try:
                summary = process_video_url(uploaded_url)
                st.session_state['detailed_summary'] = summary
                st.success("✅ Audio extracted, transcribed, and summarized successfully.")
            except Exception as e:
                st.error(f"❌ Error: {str(e)}")
    else:
        st.warning("⚠️ Please upload a file or enter a URL.")

# Display detailed summary if it exists in session state
if 'detailed_summary' in st.session_state:
    st.markdown("### Detailed Summary :memo:")
    st.write(st.session_state['detailed_summary'])

    # Add another button to process the same URL with the additional function
    if st.button("Generate Short Summary :arrow_forward:"):
        with st.spinner('⌛ Generating short summary!!!'):
            try:
                transcript = youtube_sub(uploaded_url)
                summarized_text = chunk_and_summarize(transcript)
                clean_summary = remove_redundant_sentences(summarized_text)
                final_summary = capitalize_sentences_and_combine(clean_summary)
                st.session_state['short_summary'] = final_summary
                st.success("✅ Short summary generated successfully.")
            except Exception as e:
                st.error(f"❌ Error: {str(e)}")

# Display short summary if it exists in session state
if 'short_summary' in st.session_state:
    st.markdown("### Short Summary :memo:")
    st.write(st.session_state['short_summary'])

# Custom CSS for better styling
st.markdown("""
    <style>
        .stApp {
            background-color: #1e1e1e;
            font-family: Open Sans;
        }
        .css-1d391kg p {
            color: white;
        }
        .css-1d391kg h1 {
            color: #c84e89;
            margin-bottom: 0;
            padding-top: 10px;
        }
        .css-1d391kg .stFileUploader, .css-1d391kg .stTextInput {
            width: 80%;
            margin: auto;
            background-color: white;
            color: black;
            margin-top: 20px;
        }
        .css-1d391kg .stButton>button {
            background-color: #c84e89;
            color: white;
            border-radius: 4px;
        }
        .css-1d391kg .stButton>button:hover {
            background-color: #b43d7e;
        }
    </style>
""", unsafe_allow_html=True)
