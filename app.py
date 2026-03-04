import streamlit as st
import google.generativeai as genai

# 1. 页面基础设置
st.set_page_config(page_title="AI Ad Copy Pro (US Market)", layout="wide")

# 侧边栏：配置 API Key（安全模式：不在代码中硬编码）
with st.sidebar:
    st.title("🔑 Setup")
    api_key = st.text_input("Enter Gemini API Key:", type="password")
    st.info("Get your key at: aistudio.google.com")
    st.divider()
    st.caption("Secure Mode Active")

# 2. 主界面标题
st.title("🚀 US Market Ad Copy Generator")
st.markdown("Generate high-converting **Google & Facebook Ads** based on PDP, R&D docs, and Customer Reviews.")

# 3. 输入布局
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
    
    # 修复了之前的引号和括号嵌套问题
    st.caption("✅ Google RSA: 15 Diverse Headlines + 4 Descriptions")
    st.caption("✅ Facebook: 3 Primary Texts + 3 Headlines")

# 4. 生成按钮与逻辑
if st.button("🚀 Generate High-Converting Copy", use_container_width=True):
    if not api_key:
        st.error("Please enter your Gemini API Key in the sidebar first!")
    else:
        try:
            # 配置 API
            genai.configure(api_key=api_key)
            
            # 使用最稳定的模型名
            model = genai.GenerativeModel('gemini-1.5-flash')
            
            # 构造深度 Prompt
            prompt = f"""
            Role: Expert US Growth Marketer & Direct-Response Copywriter.
            Context:
            - Product Link: {pdp_url}
            - Customer Voice/Reviews: {customer_reviews}
            - Strategy
