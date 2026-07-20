
import time
import streamlit as st
from streamer import stream_response

st.set_page_config(
    page_title="Streaming Typer",
    page_icon="⚡",
    layout="wide",
)

st.markdown("""
<style>
.stApp{
    background: linear-gradient(180deg,#0e1117,#111827);
    color:white;
}
.hero{
    padding:2rem;
    border-radius:20px;
    background:linear-gradient(135deg,#2563eb,#7c3aed);
    color:white;
    text-align:center;
    margin-bottom:1rem;
}
.card{
    background:#161b22;
    border:1px solid #2d3748;
    border-radius:18px;
    padding:1rem;
    margin-bottom:1rem;
}
.stat{
    background:#1e293b;
    padding:1rem;
    border-radius:12px;
    text-align:center;
}
.footer{
    text-align:center;
    color:#94a3b8;
    margin-top:2rem;
}
</style>
""", unsafe_allow_html=True)

if "messages" not in st.session_state:
    st.session_state.messages = []

st.markdown("""
<div class="hero">
<h1>⚡ Streaming Typer</h1>
<p>Real-time AI Streaming with Groq</p>
</div>
""", unsafe_allow_html=True)

with st.sidebar:
    st.header("⚙️ Settings")
    model = st.selectbox(
        "Model",
        [
            "llama-3.3-70b-versatile",
            "llama-3.1-8b-instant"
        ]
    )
    temperature = st.slider("Temperature",0.0,2.0,0.7,0.1)
    if st.button("🗑 Clear Chat", use_container_width=True):
        st.session_state.messages=[]
        st.rerun()

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

prompt = st.chat_input("Ask anything...")

if prompt:
    st.session_state.messages.append({"role":"user","content":prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    start=time.time()

    with st.chat_message("assistant"):
        placeholder=st.empty()
        response=""

        try:
            for token in stream_response(prompt):
                response += token
                placeholder.markdown(response+"▌")

            placeholder.markdown(response)

        except Exception as e:
            response=f"Error: {e}"
            placeholder.error(response)

    elapsed=time.time()-start

    st.session_state.messages.append(
        {"role":"assistant","content":response}
    )

    words=len(response.split())
    chars=len(response)

    st.markdown("### 📊 Response Statistics")
    c1,c2,c3=st.columns(3)
    with c1:
        st.markdown(
            f'<div class="stat"><h3>{chars}</h3><p>Characters</p></div>',
            unsafe_allow_html=True
        )
    with c2:
        st.markdown(
            f'<div class="stat"><h3>{words}</h3><p>Words</p></div>',
            unsafe_allow_html=True
        )
    with c3:
        st.markdown(
            f'<div class="stat"><h3>{elapsed:.2f}s</h3><p>Generation Time</p></div>',
            unsafe_allow_html=True
        )

    with st.expander("📋 Copy Response"):
        st.code(response)

st.markdown(
    '<div class="footer">Built with ❤️ using Streamlit + Groq</div>',
    unsafe_allow_html=True
)
