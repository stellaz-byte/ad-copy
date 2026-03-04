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

pdp = st.text_input("Product URL:")
reviews = st.text_area("Customer Reviews:", height=150)
strategy = st.selectbox("Type:", ["Evergreen", "Promo/Sale"])

if st.button("Generate Copy"):
    if not api_key:
        st.error("Please enter API Key in sidebar")
    else:
        try:
            genai.configure(api_key=api_key)
            
            # --- 自动兼容逻辑 ---
            # 尝试列表，哪个能用用哪个
            model_names = ['gemini-1.5-flash', 'gemini-1.5-pro', 'gemini-pro']
            success = False
            
            with st.spinner('Trying to connect to Gemini...'):
                for name in model_names:
                    try:
                        model = genai.GenerativeModel(name)
                        # 构造指令
                        prompt = "Act as a US ad expert. Create 15 Google headlines, 4 descriptions, and 3 Facebook ads. Product: " + pdp + ". Strategy: " + strategy + ". Reviews: " + reviews
                        response = model.generate_content(prompt)
                        st.success("Connected via " + name)
                        st.markdown(response.text)
                        success = True
                        break # 成功了就跳出循环
                    except Exception:
                        continue # 失败了尝试下一个名字
                
                if not success:
                    st.error("All models failed. Please check if your API Key is active at aistudio.google.com")
                    
        except Exception as e:
            st.error("System Error: " + str(e))

st.caption("Powered by Gemini AI")
