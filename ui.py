import streamlit as st
import requests

st.title("🔎 AI Web Search Assistant")

query = st.text_input("Ask me any...")

if query:
    with st.spinner("Searching the web and thinking..."):
        response = requests.get("http://localhost:8000/ask", params={"q": query})
        st.markdown("### 💬 Answer")
        st.write(response.json()["answer"])
