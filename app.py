import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="Ad Copy AI Expert", layout="wide")

# 侧边栏配置
api_key = "AIzaSyA9oHKZl5qzGI-FPk8Pi-fjqLGs9VCdtNo"

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
       # 深度痛点挖掘版 Prompt
        prompt = f"""
        Role: Senior US DTC Growth Architect & Copywriter.
        
        Inputs:
        - Product URL: {pdp_url}
        - Customer Reviews/Feedback: {customer_reviews}
        - Strategy: {ad_type}
        - Custom Requirements: {custom_req}

        --- STEP 1: VOICE OF CUSTOMER (VOC) ANALYSIS ---
        If reviews are provided, identify:
        1. THE "BEFORE" STATE: What was the specific frustration or 'nightmare' the customer faced? (e.g., "Replacing rusted trellises every year")
        2. THE "AHA" MOMENT: What specific feature turned them into a fan?
        3. THE COMPETITOR GAP: What did other products fail to do that this one solves?

        --- STEP 2: GENERATE AD COPY (US ENGLISH) ---
        
        Task A: Google Ads (Responsive Search Ads)
        - 15 Headlines (30 chars max): Use a 3-3-3-3-3 mix:
          * 3x Direct Benefit (Solve the #1 pain point from reviews)
          * 3x Hard Specs (Material, durability, US-based)
          * 3x Social Proof/Trust (Based on review sentiment)
          * 3x Brand & Authority
          * 3x Strong CTAs
        - 4 Descriptions (90 chars max): Mix 'Pain Point + Solution + CTA'.
        
        Task B: Facebook Ads (High Engagement)
        - Variation 1 (The "Problem-Solver"): Start with a question about the pain point.
        - Variation 2 (The "Review-Based"): Use a simulated quote or 'They said / We did' style.
        - Variation 3 (The "Feature-Deep-Dive"): Focus on the R&D/Quality aspect.
        
        Guidelines: 
        - Use US-native idioms (e.g., 'Say goodbye to...', 'Finally, a... that works').
        - Avoid marketing fluff like 'Revolutionary' or 'Game-changing'. Use specific facts.
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


