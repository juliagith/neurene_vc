import streamlit as st

# Set the page configuration
st.set_page_config(
    page_title="Neurene - Results",
    page_icon="🫀",
    layout="centered",
    initial_sidebar_state="collapsed"
)

def main():
    st.markdown(
        """
        <h1 style='text-align: center; font-family: Arial, sans-serif;'>Welcome to Your Results</h1>
        """,
        unsafe_allow_html=True,
    )

   
    

    st.write(f"Your ideal BrainBreak would last {st.session_state.break_duration}. And would be scheduled after {st.session_state.productivity_time}")

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