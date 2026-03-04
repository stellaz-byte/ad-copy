import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="Ad Copy Pro", layout="wide")

with st.sidebar:
    st.title("🔑 Configuration")
    api_key = st.text_input("Enter NEW Gemini API Key:", type="password")
    st.info("Please use a NEW key from aistudio.google.com")

st.title("🚀 Ad Copy Generator")

# 极简输入测试
pdp = st.text_input("Product URL:")
reviews = st.text_area("Customer Reviews:")

if st.button("Generate Ad Copy"):
    if not api_key:
        st.error("Please enter your API Key!")
    else:
        try:
            # 彻底初始化
            genai.configure(api_key=api_key)
            
            # 免费版最稳、最通用的模型名称
            # 这一次我们不加 'models/' 也不加版本号，让库自己去找
            model = genai.GenerativeModel('gemini-1.5-flash')
            
            prompt = f"Product: {pdp}. Reviews: {reviews}. Write 5 catchy headlines for US Facebook ads."
            
            with st.spinner('Testing connection...'):
                response = model.generate_content(prompt)
                st.success("IT WORKS!")
                st.markdown(response.text)
                
        except Exception as e:
            st.error("Still 404? Try this:")
            st.write("1. Go to AI Studio.")
            st.write("2. Create a BRAND NEW project and a NEW API Key.")
            st.code(str(e))

st.caption("Status: Debugging Mode")
