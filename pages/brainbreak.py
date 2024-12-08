import streamlit as st

# Set the page configuration
st.set_page_config(
    page_title="Neurene - Questions",
    page_icon="🫀",
    layout="centered",
    initial_sidebar_state="collapsed"
)


def main():
    
    current_feeling = st.selectbox("How are you feeling right now?", 
                                   ("Happy", "Sad", "Stressed", "Angry", "Productive", "Lazy"), 
                                   placeholder="Select an option")
    
    if 'current_feeling' not in st.session_state:
        st.session_state['current_feeling'] = current_feeling

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