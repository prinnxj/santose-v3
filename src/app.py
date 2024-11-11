import streamlit as st
import yaml
from document_processor import DocumentProcessor

# Page config for a cleaner look
st.set_page_config(
    page_title="Santose",
    layout="centered"
)

# Custom CSS with adjusted positioning
st.markdown("""
    <style>
    .main {
        background-color: #f8f9fa;
        padding-top: 50px;
    }
    .title-container {
        display: flex;
        justify-content: center;
        align-items: center;
        height: 35vh;
        margin-bottom: -100px;
    }
    .main-title {
        font-size: 48px;
        color: #000000;
        font-family: 'SF Pro Display', -apple-system, BlinkMacSystemFont, sans-serif;
        font-weight: 400;
        text-align: center;
    }
    .stRadio {
        display: flex;
        justify-content: center !important;
        padding: 0 !important;
    }
    .stRadio > div {
        display: flex;
        justify-content: center !important;
        width: 100%;
    }
    div[data-testid="element-container"] div[role="radiogroup"] {
        display: flex;
        justify-content: center;
        gap: 20px;
        margin-left: -35px;
    }
    .stTextInput > div > div > input {
        background-color: white;
        padding: 15px;
        font-size: 16px;
        border-radius: 10px;
        border: 1px solid #e0e0e0;
    }
    div[data-testid="stVerticalBlock"] > div:nth-child(2) {
        margin-top: -80px;
    }
    </style>
    """, unsafe_allow_html=True)

# Initialize processor
processor = DocumentProcessor()

# Load articles from YAML
try:
    with open('data/articles.yaml', 'r', encoding='utf-8') as file:
        articles = yaml.safe_load(file)
        for article_id, content in articles.items():
            full_text = f"""[TH] {content['thai']}\n\n[EN] {content['english']}"""
            processor.add_document(article_id, full_text)
except FileNotFoundError:
    st.error("Articles file not found. Please check data/articles.yaml exists.")

# Centered title with custom HTML
st.markdown('<div class="title-container"><h1 class="main-title">Santose</h1></div>', unsafe_allow_html=True)

# Language selector (slightly left-adjusted)
language = st.radio("", ["English", "ไทย"], horizontal=True)

# Search box with placeholder
if language == "English":
    search_term = st.text_input("", placeholder="Search...", key="search")
else:
    search_term = st.text_input("", placeholder="ค้นหา...", key="search")

# Show results when search term is entered
if search_term:
    st.markdown("---")
    results = processor.search_text(search_term)
    if results:
        for doc_id, content in results:
            st.markdown(f"""
            <div style='background-color: white; padding: 20px; border-radius: 10px; margin-bottom: 10px; border: 1px solid #e0e0e0;'>
                <strong>{doc_id}</strong><br>
                {content}
            </div>
            """, unsafe_allow_html=True)
    else:
        if language == "English":
            st.info("No results found.")
        else:
            st.info("ไม่พบผลการค้นหา")