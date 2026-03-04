import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="Ad Copy Tool", layout="wide")

with st.sidebar:
    st.title("Settings")
    api_key = st.text_input("Gemini API Key:", type="password")
    st.info("Free Tier is supported!")

st.title("🚀 Ad Copy Generator")

pdp = st.text_input("Product URL:")
reviews = st.text_area("Customer Reviews:", height=100)
strategy = st.selectbox("Type:", ["Evergreen", "Promo/Sale"])

if st.button("Generate Copy"):
    if not api_key:
        st.error("Please enter API Key")
    else:
        try:
            genai.configure(api_key=api_key)
            
            # 免费版最稳的模型名通常是这个
            model = genai.GenerativeModel('gemini-1.5-flash')
            
            prompt = "Write 3 headlines for: " + pdp + ". Based on: " + reviews
            
            with st.spinner('Checking API...'):
                response = model.generate_content(prompt)
                st.success("Success!")
                st.markdown(response.text)
                
        except Exception as e:
            st.error("Detailed Error Message:")
            st.code(str(e)) # 这一行会把具体的错误代码打印出来
            
            if "403" in str(e):
                st.warning("Hint: 403 usually means your Country/Region is not supported by Google AI, or you need to enable the API in a new project.")
            elif "429" in str(e):
                st.warning("Hint: 429 means you've hit the Rate Limit (Free tier has limits per minute).")
