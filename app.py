import streamlit as st
import google.generativeai as genai

# 设置页面
st.set_page_config(page_title="Ad Copy Tool", layout="wide")

# 侧边栏
with st.sidebar:
    st.title("Settings")
    api_key = st.text_input("Gemini API Key:", type="password")

# 主界面
st.title("🚀 Ad Copy Generator")

# 输入框
pdp = st.text_input("Product URL:")
reviews = st.text_area("Customer Reviews:", height=150)
strategy = st.selectbox("Type:", ["Evergreen", "Promo/Sale"])

# 生成按钮
if st.button("Generate Copy"):
    if not api_key:
        st.error("Missing API Key")
    else:
        try:
            genai.configure(api_key=api_key)
            model = genai.GenerativeModel('gemini-1.5-flash')
            
            # 构建简单的指令，避免复杂的 f-string
            instruction = "You are a US ad expert. Create 15 Google headlines (max 30 chars), 4 Google descriptions, and 3 Facebook ad texts. "
            context = "Product: " + pdp + ". Strategy: " + strategy + ". Reviews: " + reviews
            full_prompt = instruction + context
            
            with st.spinner('Generating...'):
                response = model.generate_content(full_prompt)
                st.write(response.text)
        except Exception as e:
            st.error(str(e))

st.caption("Powered by Gemini")
