import streamlit as st

# Set the page configuration
st.set_page_config(
    page_title="Neurene - Mindful Breaks",
    page_icon="🌻",
    layout="centered",
    initial_sidebar_state="collapsed",
    menu_items={
         'Get Help': "http://localhost:8501/faq",
         'Report a bug': "mailto:support@neurene.com",
         'About': "© 2024 Neurene Productivity Group GmbH. All rights reserved."
     }
)

# Sidebar with grouped pages
st.sidebar.title("Navigation")

# Group 1: General Information
with st.sidebar.expander("📋 General Information"):
    if st.button("Home"):
        st.switch_page("home.py")
    if st.button("FAQ"):
        st.switch_page("pages/faq.py")

# Load the logo
logo_path = "./static/neurene_logo_light.jpg"

# Design the landing page
def main():
    # Apply a custom background color
    st.markdown(
        """
        <style>
        body {
            background-color: #E1E1E1; /* Dark background for contrast */
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    # Logo and title section
    st.image(logo_path, width=80)
    st.markdown(
        """
        <div style='text-align: center; margin-top: -20px;'>
            <h1 style='font-family: Arial, sans-serif; '>Neurene - Login</h1>
            <h3 style='font-family: Arial, sans-serif; '>Mindful Breaks, Seamlessly Integrated</h3>
        </div>
        """,
        unsafe_allow_html=True,
    )
    

    # Subheading and app description
    st.markdown(
        """
        <div style="text-align: center; margin-top: 20px;">
            <p style="font-size: 18px; font-family: Arial, sans-serif;">
                Log in with your credentials.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )


    st.session_state.username = st.text_input("username")
    password=st.text_input("password", type='password')

    # Call-to-action section (Button to navigate to questions.py)
    if st.button("Login"):
        st.switch_page("pages/brainbreak.py")

    # Footer
    st.markdown(
    """
    <div style="text-align: center; margin-top: 50px;">
        <p style="font-size: 14px; font-family: Arial, sans-serif;">
            © 2024 Neurene Productivity Group GmbH. All rights reserved.
        </p>
        <p style="font-size: 14px; font-family: Arial, sans-serif;">
            For support, visit our <a href="/faq" target="_self">FAQ Page</a> or contact us at <a href="mailto:support@neurene.com">support@neurene.com</a>
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)


if __name__ == "__main__":
    main()
