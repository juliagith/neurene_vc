import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="Neurene - Mindful Breaks",
    page_icon="🌻",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# Initialize session state
if "break_active" not in st.session_state:
    st.session_state.break_active = False
if "current_mood" not in st.session_state:
    st.session_state.current_mood = None
if "goal" not in st.session_state:
    st.session_state.goal = None
if "post_mood" not in st.session_state:
    st.session_state.post_mood = None
if "break_ended" not in st.session_state:
    st.session_state.break_ended = False

# Create the DataFrame
data = {
    "Goal": [
        "Relaxation", "Mastery", "Connection", "Meaning"
    ],
    "Activity/Method": [
        [
            "Deep Breathing", 
            "Progressive Muscle Relaxation", 
            "Guided Meditation on <a href='https://www.calm.com/de' target='_blank'>Calm</a>"
        ],
        [
            "Puzzles", 
            "Learn a New Fact (e.g.  <a href='https://www.coursera.org/' target='_blank'>Coursera</a>)", 
            "Language App (e.g. <a href='https://de.duolingo.com/' target='_blank'>Duolingo</a>)"
        ],
        [
            "Call a Friend", 
            "Reconnect with an Old Friend", 
            "Join a Group Chat"
        ],
        [
            "Stretching", 
            "Drawing or Doodling", 
            "Work on a Craft Project"
        ]
    ],
    "Description": [
        [
            "Practice focused breathing to calm your mind.",
            "Progressively relax each muscle group.",
            "Follow a guided session for mindfulness."
        ],
        [
            "Challenge your mind with engaging puzzles.",
            "Learn something new and interesting.",
            "Practice language skills with a fun app."
        ],
        [
            "Call or text a loved one for connection.",
            "Reach out to someone you haven’t spoken to in a while.",
            "Join a group or community chat."
        ],
        [
            "Stretch your body to release tension.",
            "Draw or doodle to express creativity.",
            "Engage in a small craft or hobby project."
        ]
    ]
}

df = pd.DataFrame(data)
logo_path = "./static/neurene_logo_light.jpg"


# Title and Introduction
st.image(logo_path, width=80)
st.title(f"Welcome, {st.session_state.username}!")
st.subheader("We are so glad that you decided to take some time for yourself today.")

# Step 1: Ask for Current Mood
st.session_state.current_mood = st.selectbox(
    "How do you currently feel?",
    ["Stressed 😵‍💫", "Anxious 😟", "Sad 😢", "Bored 😐", "Angry 😠", "Overwhelmed 😰", "Tired 😴", "Happy 😊", "Productive 💪", "Calm 😌", "No answer 🤷"],
    index=None,
)

# Step 2: Ask for the Goal of the Break
st.session_state.goal = st.selectbox(
    "What would you like to gain from your break?",
    df["Goal"].unique(),
    index=None,
)

# Start or Skip Break
if st.button("Start Brain Break"):
    st.session_state.break_active = True
    st.session_state.break_ended = False
elif st.button("Skip Brain Break"):
    st.write("Skipping break. You can take one later!")

# Brain Break Phase
if st.session_state.break_active:
    st.subheader("Recommended Activities for Your Break")
    
    if st.session_state.goal:
        goal_index = df["Goal"].tolist().index(st.session_state.goal)
        activities = df.loc[goal_index, "Activity/Method"]
        descriptions = df.loc[goal_index, "Description"]
        
        for activity, description in zip(activities, descriptions):
            st.markdown(f"**Activity:** {activity}", unsafe_allow_html=True)
            st.write(description)
    
    st.warning("Your device is now in **Do Not Disturb** mode. ⏾")
    
    if st.button("End Break"):
        st.session_state.break_active = False
        st.session_state.break_ended = True

# Post-Break Mood Assessment
if st.session_state.break_ended:
    st.subheader("How do you feel after your break?")
    st.session_state.post_mood = st.radio(
        "Select your mood:",
        ["😊 Happy", "😌 Calm", "😕 Neutral", "😞 Sad", "😡 Angry", "❌ No answer"],
        index=None,
    )
    
    if st.session_state.post_mood and st.button("Save & View Analytics"):
        st.success("Your mood has been saved. Redirecting to Analytics...")
        st.switch_page("pages/analytics.py")

# Footer
st.markdown("""
    <div style="text-align: center; margin-top: 50px;">
        <p style="font-size: 14px; font-family: Arial, sans-serif;">
            © 2024 Neurene Productivity Group GmbH. All rights reserved.
        </p>
        <p style="font-size: 14px; font-family: Arial, sans-serif;">
            For support, visit our <a href="/faq" target="_self">FAQ Page</a> or contact us at 
            <a href="mailto:support@neurene.com">support@neurene.com</a>
        </p>
    </div>
""", unsafe_allow_html=True)
