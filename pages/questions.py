import streamlit as st

# Set the page configuration
st.set_page_config(
    page_title="Neurene - Questions",
    page_icon="🫀",
    layout="centered",
    initial_sidebar_state="collapsed"
)


def main():
    st.markdown(
        """
        <h1 style='text-align: center; font-family: Arial, sans-serif;'>Welcome to the Questions Page</h1>
        <p style='text-align: center; font-family: Arial, sans-serif;'>This is where you can personalize your mental-health experience.</p>
        """,
        unsafe_allow_html=True,
    )

    # Here you can add the functionality or questions for the user.
    break_duration = st.selectbox("How long would you like to take your mental health breaks?",
                                  ("5 Minutes", "10 Minutes", "15 Minutes"),
                                    placeholder="Select an option"
                                    )
    

    st.write("Your Answer was: ", break_duration)

    # if 'break_duration' not in st.session_state:
    st.session_state['break_duration'] = break_duration

    productivity_time = st.selectbox("At which time of the day do you feel most productive?",
                                     ("In the morning (7 am - 10 am)", "In the late morning (10 am - 1 pm)", "In the early afternoon (2 pm - 5 pm)", "In the late afternoon (6 pm - 8 pm)", "Other"), 
                                     placeholder="Select an option"
                                )
    st.write("Your Answer was: ", productivity_time)

    st.session_state['productivity_time'] = productivity_time

    

    if st.button("Generate your BrainBreak Schedule"):
        st.switch_page("pages/results.py")

# Footer
    st.markdown(
        """
        <div style="text-align: center; margin-top: 50px;">
            <p style="font-size: 14px; font-family: Arial, sans-serif;">
                © 2024 Neurene. All rights reserved.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )


if __name__ == "__main__":
    main()
