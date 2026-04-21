import streamlit as st
import ollama

st.title("📚 Offline AI Notes Generator")

# User input
topic = st.text_input("Enter a topic for your notes:")

if st.button("Generate Notes"):
    if topic:
        with st.spinner("Phi-4 is thinking..."):
            try:
                # This sends your request to the Ollama server running locally
                response = ollama.chat(model='phi4', messages=[
                    {'role': 'user', 'content': f"Create study notes on {topic}. Include 5 bullet points, a simple explanation, one example, and a short summary."}
                ])
                
                # Extract the text from the response
                final_notes = response['message']['content']
                
                # Display the notes
                st.markdown(final_notes)
                
            except Exception as e:
                st.error("Error: Make sure the Ollama application is running in the background!")
    else:
        st.warning("Please enter a topic first.")