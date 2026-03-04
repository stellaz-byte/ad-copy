import streamlit as st
import google.generativeai as genai

# 1. 页面配置
st.set_page_config(page_title="AI Ad Copy Pro", layout="wide")
st.title("🚀 US Market Ad Copy Generator")

# 侧边栏：配置 API
with st.sidebar:
    api_key = st.text_input("Enter Gemini API Key:", type="password")
    if api_key:
        genai.configure(api_key=api_key)

# 2. 输入区
col1, col2 = st.columns(2)

with col1:
    st.subheader("🔗 Data Sources")
    pdp_url = st.text_input("Product PDP URL:", placeholder="https://example.com/product")
    comp_url = st.text_input("Competitor URL (Optional):")
    uploaded_file = st.file_uploader("Upload R&D / Marketing Doc (PDF/TXT)", type=['pdf', 'txt'])
    
with col2:
    st.subheader("💡 Creative Inputs")
    customer_reviews = st.text_area("Paste Customer Reviews (to extract pain points):", height=100)
    ad_type = st.radio("Ad Strategy:", ["Promo/Sale", "Evergreen/Product Launch"])
    custom_req = st.text_input("Other Requirements (e.g. Tone, Target Audience):")

# 3. 核心生成逻辑
if st.button("Generate Ad Copy ✨"):
    if not api_key:
        st.error("Please enter your API Key first!")
    else:
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        # 构造复杂的 Prompt
        prompt = f"""
        Act as a senior US Direct-to-Consumer (DTC) Copywriter. 
        Context:
        - Product Link: {pdp_url}
        - Competitor: {comp_url}
        - Customer Voice/Reviews: {customer_reviews}
        - Strategy: {ad_type}
        - Custom Requirement: {custom_req}

        Task:
        Generate high-converting English ad copy for the US market.
        
        Requirements for Google Ads (RSA):
        1. Generate 15 diverse headlines (max 30 chars). Ensure each headline uses a different angle (Feature, Benefit, Social Proof, CTA, Urgency). Avoid repetition.
        2. Generate 4 descriptions (max 90 chars).
        
        Requirements for Facebook Ads:
        1. 3 Primary Text variations (Short, Story-based, List-style) with relevant Emojis.
        2. 3 Headlines.

        Specific Strategy:
        {"For Promo: Focus on discount variants like 'Save 30%' and urgent CTAs." if ad_type == "Promo/Sale" else "For Evergreen: Focus on hard specs from PDP and solving pain points found in reviews."}
        """
        
        with st.spinner('Analyzing data and crafting copy...'):
            response = model.generate_content(prompt)
            st.success("Generated!")

            st.markdown(response.text)
