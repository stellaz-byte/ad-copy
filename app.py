import streamlit as st
import google.generativeai as genai

# 1. 页面配置
st.set_page_config(page_title="AI Ad Copy Pro", layout="wide")

# 侧边栏配置
with st.sidebar:
    st.title("🔑 Configuration")
    api_key = st.text_input("Enter NEW Gemini API Key:", type="password")
    st.info("Using a fresh key from aistudio.google.com ensures stability.")
    st.divider()
    st.caption("Target Market: United States 🇺🇸")

# 2. 主界面
st.title("🚀 US Market Ad Copy Expert")
st.markdown("Generate high-converting ads based on **PDP, Reviews, and R&D Docs**.")

# 3. 输入布局
col1, col2 = st.columns([1, 1], gap="large")

with col1:
    st.subheader("📦 Product Details")
    pdp_url = st.text_input("Product URL (PDP):", placeholder="https://example.com/product")
    customer_reviews = st.text_area(
        "Customer Reviews / Pain Points:", 
        height=200, 
        placeholder="Paste real customer feedback here. AI will extract 'Nightmare' vs 'Dream' scenarios."
    )

with col2:
    st.subheader("📣 Ad Strategy")
    ad_strategy = st.selectbox(
        "Campaign Type:",
        ["Evergreen / Product Launch", "Promo / Seasonal Sale"]
    )
    custom_req = st.text_input("Extra Requirements:", placeholder="e.g., Witty tone, focus on eco-friendly")
    
    st.info("✅ Google Ads: 15 Diverse Headlines & 4 Descriptions\n\n✅ Facebook: 3 Primary Texts & 3 Headlines")

# 4. 生成核心逻辑
if st.button("🚀 Generate High-Converting Ad Copy", use_container_width=True):
    if not api_key:
        st.error("Please enter your API Key in the sidebar!")
    else:
        try:
            genai.configure(api_key=api_key)
            model = genai.GenerativeModel('gemini-1.5-flash')
            
            # 深度营销 Prompt
            prompt = f"""
            Role: Senior US DTC Performance Marketer & Copywriter.
            Context:
            - Product: {pdp_url}
            - Reviews: {customer_reviews}
            - Strategy: {ad_strategy}
            - Extra: {custom_req}

            TASK: Generate ad copy for the US market.
            
            --- 1. GOOGLE ADS (RSA) ---
            Generate 15 Headlines (max 30 chars). CRITICAL: Every headline must focus on a DIFFERENT angle to allow Google's algorithm to test effectively. 
            Mix these angles: 
            - 3x Addressing Pain Points (from reviews)
            - 3x Hard Features/Specs (from PDP)
            - 3x Core Benefits (The 'Dream' state)
            - 3x Social Proof/Trust Signals
            - 3x Urgency/CTAs
            Generate 4 Descriptions (max 90 chars). Format: 'Problem + Solution + CTA'.

            --- 2. FACEBOOK ADS ---
            Generate 3 Primary Texts (Short, List-based, and Story-based) with Emojis.
            Generate 3 Catchy Headlines.

            Specific Logic:
            - Analyze the reviews: Identify the #1 frustration and flip it into a USP.
            - Language: Use US-native English, idioms, and high-intensity conversion verbs.
            - If '{ad_strategy}' is Promo, emphasize the specific discount and limited-time nature.
            """

            with st.spinner('AI is analyzing data and crafting ads...'):
                response = model.generate_content(prompt)
                st.success("Generation Successful!")
                st.divider()
                st.markdown(response.text)
                
        except Exception as e:
            st.error(f"Error: {e}")
            st.info("Check if your API Key project has 'Generative Language API' enabled.")

st.divider()
st.caption("Powered by Gemini 1.5 Flash | Built for DTC Growth")
