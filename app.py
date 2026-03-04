import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="Ad Copy Pro", layout="wide")

# 直接从侧边栏获取 Key
with st.sidebar:
    st.title("🔑 Configuration")
    api_key = st.text_input("Enter Gemini API Key:", type="password")

st.title("🚀 US Ad Copy Generator")

# 输入区
pdp = st.text_input("Product URL (PDP):")
reviews = st.text_area("Customer Reviews (Pain Points):", height=100)
strategy = st.selectbox("Ad Strategy:", ["Evergreen", "Promo/Sale"])

if st.button("Generate Ad Copy"):
    if not api_key:
        st.error("Please enter your API Key in the sidebar.")
    else:
        try:
            genai.configure(api_key=api_key)
            
            # 使用包含 'models/' 前缀的完整路径，这是最稳的调用方式
            # 即使库版本旧，这样写也能强行找到模型
            model = genai.GenerativeModel('models/gemini-1.5-flash')
            
            # 极简测试指令
            prompt = f"Act as a US Copywriter. Product: {pdp}. Strategy: {strategy}. Reviews: {reviews}. Write 15 diverse Google Headlines and 3 Facebook Ads."
            
            with st.spinner('Connecting to Google AI...'):
                response = model.generate_content(prompt)
                st.success("Generation Successful!")
                st.markdown(response.text)
                
        except Exception as e:
            st.error("Technical Error Details:")
            st.code(str(e))
            
            # 自动备选方案：尝试旧版模型名
            if "404" in str(e):
                st.info("Trying legacy model name...")
                try:
                    legacy_model = genai.GenerativeModel('gemini-pro')
                    resp = legacy_model.generate_content(prompt)
                    st.markdown(resp.text)
                except Exception as e2:
                    st.error("Legacy model also failed: " + str(e2))

st.divider()
st.caption("Free Tier API Support | Ensure your key is from aistudio.google.com")
