import streamlit as st
from streamer import stream_response

# Page configuration
st.set_page_config(
    page_title="Streaming Typer",
    page_icon="⚡",
    layout="centered"
)

st.title("⚡ Streaming Typer")
st.caption("Watch the AI respond in real time.")

# User input
prompt = st.text_area(
    "Enter your prompt",
    height=150,
    placeholder="Ask me anything..."
)

# Generate button
if st.button("Generate Response", use_container_width=True):

    if prompt.strip():

        output = st.empty()
        response = ""

        for token in stream_response(prompt):
            response += token
            output.markdown(response + "▌")

        output.markdown(response)

    else:
        st.warning("Please enter a prompt.")