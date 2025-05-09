import streamlit as st
import google.generativeai as genai

# Streamlit app setup
st.set_page_config(page_title="Q&A Demo")
st.header("Gemini LLM Application")

# Sidebar input for API Key
api_key = st.sidebar.text_input("Enter your Google API Key", type="password")

# Input for the user's question
user_input = st.text_input("Input:", key="input")
submit = st.button("Ask the question")

# Function to load Gemini model and get response
def get_gemini_response(api_key, question):
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("models/gemini-1.5-flash")
    response = model.generate_content(question)
    return response.text

# When the button is clicked
if submit:
    if not api_key:
        st.error("Please enter your Google API key in the sidebar.")
    elif not user_input:
        st.warning("Please enter a question.")
    else:
        response = get_gemini_response(api_key, user_input)
        st.subheader("The Response is")
        st.write(response)
