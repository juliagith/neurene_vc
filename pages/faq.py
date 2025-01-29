import streamlit as st

# Set the page configuration
st.set_page_config(
    page_title="Neurene - FAQ",
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
    
    # FAQ Section
    st.image(logo_path, width=80)
    st.markdown("### Frequently Asked Questions")

    # Question 1
    with st.expander("**What is Neurene?**"):
        st.write("Neurene is a productivity tool that integrates with your calendar to identify and recommend short mindfulness breaks that fit your schedule.")

    # Question 2
    with st.expander("**How does Neurene work?**"):
        st.write("Neurene scans your calendar for open slots or existing breaks and suggests short, mindful activities you can do during those times to recharge.")

    # Question 3
    with st.expander("**Is my data secure with Neurene?**"):
        st.write("Yes, Neurene prioritizes your privacy and ensures all your data is securely encrypted. We only access the information needed to provide our services.")

    # Question 4
    with st.expander("**Can I customize the mindfulness activities?**"):
        st.write("Absolutely! You can customize the types of mindfulness breaks suggested by Neurene to match your preferences.")



    # Footer
    st.markdown(
        """
        <div style="text-align: center; margin-top: 50px;">
            <p style="font-size: 14px; font-family: Arial, sans-serif;">
                For further questions, please reach out to <a href="mailto:support@neurene.com">support@neurene.com</a>
            </p>
            <p style="font-size: 14px; font-family: Arial, sans-serif;">
                © 2024 Neurene Productivity Group GmbH. All rights reserved.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )


if __name__ == "__main__":
    main()
