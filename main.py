import streamlit as st

# Set the page configuration
st.set_page_config(
    page_title="Neurene - Mindful Breaks",
    page_icon="🧘",
    layout="centered",
)

# Load the logo
logo_path = "./static/neurene_logo.jpeg"


# Design the landing page
def main():
    # Logo and title section
    st.image(logo_path, use_container_width=True)
    st.markdown(
        """
        <div style='text-align: center; margin-top: -20px;'>
            <h1 style='font-family: Arial, sans-serif; color: #FFFFFF;'>Neurene</h1>
            <h3 style='font-family: Arial, sans-serif; color: #FFFFFF;'>Mindful Breaks, Seamlessly Integrated</h3>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Subheading and app description
    st.markdown(
        """
        <div style="text-align: center; margin-top: 20px;">
            <p style="font-size: 18px; color: #FFFFFF; font-family: Arial, sans-serif;">
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
            <h2 style='text-align: center; font-family: Arial, sans-serif; color: #FFFFFF;'>Why Choose Neurene?</h2>
            <ul style='list-style-type: none; padding: 0; font-family: Arial, sans-serif; color: #FFFFFF;'>
                <li style='margin: 10px 0;'><b>🌟 Smart Integration:</b> Sync seamlessly with your calendar.</li>
                <li style='margin: 10px 0;'><b>🕰️ Bite-sized Breaks:</b> Short, effective sessions to recharge.</li>
                <li style='margin: 10px 0;'><b>🎧 Personalized Guidance:</b> Tailored mindfulness suggestions.</li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Call-to-action section
    st.markdown(
        """
        <div style="text-align: center; margin-top: 40px;">
            <a href="#" style="
                text-decoration: none;
                background-color: #4CAF50;
                color: white;
                padding: 10px 20px;
                border-radius: 5px;
                font-size: 16px;
                font-family: Arial, sans-serif;
            ">Get Started</a>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Footer
    st.markdown(
        """
        <div style="text-align: center; margin-top: 50px;">
            <p style="font-size: 14px; color: #FFFFFF; font-family: Arial, sans-serif;">
                © 2024 Neurene. All rights reserved.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )


if __name__ == "__main__":
    main()
