import streamlit as st
import google.generativeai as genai

# 1. 页面基础设置
st.set_page_config(page_title="AI Ad Copy Pro (US Market)", layout="wide")

# 侧边栏：配置 API Key
api_key = "AIzaSyApvr8_cnQ9bZX3Joe6qd0S08X2wOPOQBA"

# 2. 主界面标题
st.title("🚀 US Market Ad Copy Generator")
st.markdown("Generate high-converting **Google & Facebook Ads** based on PDP, R&D docs, and Customer Reviews.")

# 3. 输入布局：左侧产品信息，右侧广告策略
col1, col2 = st.columns([1, 1], gap="large")

with col1:
    st.subheader("📦 Product & Context")
    pdp_url = st.text_input("Product PDP URL:", placeholder="https://www.example.com/product")
    customer_reviews = st.text_area(
        "Customer Reviews / Pain Points:", 
        height=150, 
        placeholder="Paste real customer reviews here. AI will extract pain points and flip them into selling points."
    )
    uploaded_file = st.file_uploader("Upload R&D / Marketing Doc (Optional)", type=['pdf', 'txt'])

with col2:
    st.subheader("📣 Ad Strategy")
    ad_strategy = st.selectbox(
        "Select Campaign Type:",
        ["Evergreen / Product Launch", "Promo / Seasonal Sale"]
    )
    custom_req = st.text_input("Extra Instructions:", placeholder="e.g., Tone: Witty; Target: Urban Gardeners")
    
    # 针对 Google Ads 的硬性要求说明
    st.caption("✅ Google RSA: 15 Diverse Headlines + 4 Descriptions")
    st.caption("✅ Facebook: 3 Primary Texts + 3 Headlines
