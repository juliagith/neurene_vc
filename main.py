import streamlit as st

# Set the page configuration
st.set_page_config(
    page_title="Neurene - Mindful Breaks",
    page_icon="🌻",
    layout="centered",
    initial_sidebar_state="collapsed"
)


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
    st.image(logo_path, use_container_width="auto")
    st.markdown(
        """
        <div style='text-align: center; margin-top: -20px;'>
            <h1 style='font-family: Arial, sans-serif; '>Neurene</h1>
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
                Discover small moments of mindfulness amidst your busy schedule. 
                Neurene scans your calendar to find short, rejuvenating breaks tailored to you.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Features section
    st.markdown(
        """
        <div style='margin: 40px 0;'>
            <h2 style='text-align: center; font-family: Arial, sans-serif; '>Why Choose Neurene?</h2>
            <ul style='list-style-type: none; padding: 0; font-family: Arial, sans-serif'>
                <li style='margin: 10px 0;'><b>🌟 Smart Integration:</b> Sync seamlessly with your calendar.</li>
                <li style='margin: 10px 0;'><b>🕰️ Bite-sized Breaks:</b> Short, effective sessions to recharge.</li>
                <li style='margin: 10px 0;'><b>🎧 Personalized Guidance:</b> Tailored mindfulness suggestions.</li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Call-to-action section (Button to navigate to questions.py)
    if st.button("Get Started"):
        st.switch_page("pages/onboarding.py")

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
