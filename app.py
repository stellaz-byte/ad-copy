import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="Ad Copy AI Expert", layout="wide")

# 侧边栏配置
with st.sidebar:
    st.title("⚙️ Setting")
    api_key = st.text_input("Gemini API Key:", type="password")
    st.info("Get your key at: aistudio.google.com")

st.title("🎯 US Market Ad Copy Generator")
st.caption("Generate high-converting Google & Facebook ads based on PDP, Reviews, and R&D docs.")

# 输入布局
col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("📦 Product Info")
    pdp_url = st.text_input("Product URL (PDP):")
    uploaded_file = st.file_uploader("Upload R&D / Marketing Doc", type=['pdf', 'txt'])
    customer_reviews = st.text_area("Customer Reviews (Voice of Customer):", placeholder="Paste Amazon/Shopify reviews here...")

with col2:
    st.subheader("📣 Ad Strategy")
    ad_type = st.selectbox("Campaign Objective:", ["Evergreen / Product Launch", "Promo / Seasonal Sale"])
    custom_req = st.text_input("Specific Requirements:", placeholder="e.g. Focus on pet owners, witty tone")

# 生成逻辑
if st.button("🚀 Generate Diverse Ad Copies", use_container_width=True):
    if not api_key:
        st.warning("Please enter your API Key in the sidebar!")
    else:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        # 更加精准的 Prompt
        prompt = f"""
        Role: Senior US Growth Copywriter.
        Data: PDP={pdp_url}, Reviews={customer_reviews}, Strategy={ad_type}.
        Goal: Generate English ad copy for US customers.
        
        Task 1: Google Ads (Responsive Search Ads)
        - 15 Diverse Headlines (30 chars max): Use different angles (1-3 Brand/Product, 4-6 Specs, 7-9 Pain points, 10-12 Benefits, 13-15 CTAs). NO REPETITION.
        - 4 Descriptions (90 chars max).
        
        Task 2: Facebook Ads
        - 3 Primary Texts (Short, List-based, Emotional).
        - 3 Catchy Headlines.
        
        Note: Use US English idioms. Focus on solving pain points found in reviews.
        """
        
        with st.spinner('AI is thinking...'):
            try:
                response = model.generate_content(prompt)
                st.divider()
                st.markdown(response.text)
                # Streamlit自带的复制按钮会在代码块右上角自动出现
            except Exception as e:
                st.error(f"Error: {e}")

st.divider()
st.caption("Made for US Market Performance Marketing")
