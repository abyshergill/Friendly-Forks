import streamlit as st
from upload import UPLOAD_FILE
from filterlogic import main

st.set_page_config(
    page_title = "Wai Project",
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

def check_auth(username, password):
    try:
        with open("users.txt", "r") as f:
            users = f.read().splitlines()
            for user in users:
                stored_username, stored_password = user.split(":")
                if username == stored_username and password == stored_password:
                    return True
    except FileNotFoundError:
        st.error("User data file not found. Please ensure 'users.txt' exists.")
        return False
    except Exception as e:
        st.error(f"An error occurred during authentication: {e}")
        return False
    return False

if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

if not st.session_state.authenticated:
    st.sidebar.title("Login")
    username = st.sidebar.text_input("Username")
    password = st.sidebar.text_input("Password", type="password")
    if st.sidebar.button("Login"):
        if check_auth(username, password):
            st.session_state.authenticated = True
            st.rerun()
        else:
            st.sidebar.error("Invalid username or password")
    
    if "currentPage" not in st.session_state:
        st.session_state.currentPage = "Extract"
else:
    st.sidebar.title("Navigation")
    if st.sidebar.button("Logout"):
        st.session_state.authenticated = False
        if 'filtered_df' in st.session_state:
            del st.session_state.filtered_df
        st.rerun()

    if "currentPage" not in st.session_state:
        st.session_state.currentPage = "Extract"

col1, col2, spacer, col3 = st.columns([1, 1, 8, 2])

with col1:
    if st.session_state.authenticated: 
        if st.button("Upload"):
            st.session_state.currentPage = "Upload"

with col2:
    if st.button("Extract"):
        st.session_state.currentPage = "Extract"

with col3:
    st.write(f"📄 {st.session_state.currentPage.capitalize()}")

st.markdown("---")

def page1():
    st.title("Wai Master Uploader")
    st.markdown("Make Sure your Excel file Should have Sheet with name **Wai Normal Rd**")
    UPLOAD_FILE()

def page2():
    st.title("Filter Master Data")
    main()

if st.session_state.authenticated and st.session_state.currentPage == "Upload":
    page1()
elif st.session_state.currentPage == "Extract":
    page2()
else:
    st.warning("Please log in to access the Upload page or select a valid page.")
	
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
        <p>&copy; Aby 2025 | Designed and Maintain by Kuldeep Singh aka Aby </p>
    </div>
"""
st.markdown(footer, unsafe_allow_html=True)