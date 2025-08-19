import streamlit as st
from upload import UPLOAD_FILE
from filterlogic import main

st.set_page_config(
    page_title = "Lucas | Data",
	page_icon = "icon/icon.png",
	menu_items = None,
	layout = "wide",
    initial_sidebar_state="collapsed"
)


st.markdown("""
    <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
		.block-container {
            padding-top: 0rem;
        }
    </style>
""", unsafe_allow_html=True)

if "currentPage" not in st.session_state:
    st.session_state.currentPage = "Extract"

col1, col2, spacer, col3 = st.columns([1, 1, 8, 2])

with col1:
    if st.button("Upload"):
        st.session_state.currentPage = "Upload"

with col2:
    if st.button("Extract"):
        st.session_state.currentPage = "Extract"

with col3:
    st.write(f"📄 {st.session_state.currentPage.capitalize()}")

st.markdown("---")

def page1():
    st.title("Lucas Uploader")
    UPLOAD_FILE()

def page2():
    st.title("Data")
    main()

if st.session_state.currentPage == "Upload":
    page1()
elif st.session_state.currentPage == "Extract":
    page2()
	
footer = """
    <style>
        .footer {
            position: fixed;
            bottom: 0;
            left: 0;
            right: 0;
            background-color: #f1f1f1;
            text-align: center;
            padding: 0px;
            font-size: 14px;
            color: #333;
        }
    </style>
    <div class="footer">
        <p>&copy; abyshergill 2025 | Designed and Maintain by your_name </p>
    </div>
"""
st.markdown(footer, unsafe_allow_html=True)

