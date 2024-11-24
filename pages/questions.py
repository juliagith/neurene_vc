import streamlit as st

# Set the page configuration
st.set_page_config(
    page_title="Neurene - Questions",
    page_icon="🧘",
    layout="centered",
    initial_sidebar_state="collapsed"
)


def main():
    st.markdown(
        """
        <h1 style='text-align: center; font-family: Arial, sans-serif;'>Welcome to the Questions Page</h1>
        <p style='text-align: center; font-family: Arial, sans-serif;'>This is where you can ask your mindfulness-related questions.</p>
        """,
        unsafe_allow_html=True,
    )

    # Here you can add the functionality or questions for the user.
    break_duration = st.selectbox("How long would you like to take a break?",
                                  ("5 Minutes", "10 Minutes", "15 Minutes"))

    st.write("Your Answer was: ", break_duration)


if __name__ == "__main__":
    main()
