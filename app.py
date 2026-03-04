import streamlit as st
import google.generativeai as genai

# 1. 页面设置
st.set_page_config(page_title="Ad Copy Pro", layout="wide")

# 2. 侧边栏配置
with st.sidebar:
    st.title("🔑 Setup")
    api_key = st.text_input("Enter Gemini API Key:", type="password")
    st.info("Get your key at: aistudio.google.com")

# 3. 主界面布局
st.title("🚀 US Market Ad Copy Generator")

col1, col2 = st.columns([1, 1], gap="large")

with col1:
    st.subheader("📦 Product & Context")
    pdp_url = st.text_input("Product URL:", placeholder="https://example.com/product")
    customer_reviews = st.text_area("Customer Reviews:", height=150, placeholder="Paste reviews here...")
    uploaded_file = st.file_uploader("Upload R&D Doc", type=['pdf', 'txt'])

with col2:
    st.subheader("📣 Ad Strategy")
    ad_strategy = st.selectbox("Campaign Type:", ["Evergreen / Launch", "Promo / Sale"])
    custom_req = st.text_input("Extra Info:", placeholder="e.g. Witty tone")
    st.caption("✅ Google RSA: 15 Headlines + 4 Descriptions")
    st.caption("✅ Facebook: 3 Primary Texts + 3 Headlines")

# 4. 生成逻辑
if st.button("🚀 Generate Ad Copy", use_container_width=True):
    if not api_key:
        st.error("Please enter your API Key in the sidebar!")
    else:
        try:
            genai.configure(api_key=api_key)
            # 优先尝试 Flash 模型
            model = genai.GenerativeModel('gemini-1.5-flash')
            
            # 使用简单的字符串组合，避免缩进导致的 f-string 错误
            prompt_content = "Role: Expert US Growth Marketer.\n"
            prompt_content += f"Product URL: {pdp_url}\n"
            prompt_content += f"
