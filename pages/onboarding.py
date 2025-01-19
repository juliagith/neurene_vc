import streamlit as st

# Set the page configuration
st.set_page_config(
    page_title="Neurene - Onboarding",
    page_icon="🫀",
    layout="centered",
    initial_sidebar_state="collapsed"
)


def main():
    st.markdown(
        """
        <h1 style='text-align: center; font-family: Arial, sans-serif;'>Welcome to the Initialization of Neurene</h1>
        <p style='text-align: center; font-family: Arial, sans-serif;'>This is where you can personalize your mental-health experience.</p>
        """,
        unsafe_allow_html=True,
    )

    # Here you can add the functionality or questions for the user.
    break_duration = st.selectbox("How long would you like to take your mental health breaks?",
                                  ("5 Minutes", "10 Minutes", "15 Minutes"),
                                    placeholder="Select an option",
                                    index=None
                                    )

    st.write("Your Answer was: ", break_duration)

    # if 'break_duration' not in st.session_state:
    st.session_state['break_duration'] = break_duration

    productivity_time = st.selectbox("At which time of the day do you feel most productive?",
                                     ("7 - 10 AM", "10 AM - 1 PM", "1-4 PM", "4-7 PM", "Other"), 
                                     placeholder="Select an option",
                                     index=None
                                )
    st.write("Your Answer was: ", productivity_time)

    st.session_state['productivity_time'] = productivity_time

    # Here you can add the functionality or questions for the user.
    preferred_calendar = st.selectbox("Which calendar suite do you want to connect with?",
                                  ("Google", "Microsoft", "others"),
                                    placeholder="Select an option",
                                    index=None
                                    )

    if st.button("Generate your BrainBreak Schedule"):
        st.switch_page("pages/results.py")

# Footer
    st.markdown(
        """
        <div style="text-align: center; margin-top: 50px;">
            <p style="font-size: 14px; font-family: Arial, sans-serif;">
                © 2024 Neurene Productivity Group GmbH. All rights reserved.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )


if __name__ == "__main__":
    main()
