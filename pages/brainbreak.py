import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="Neurene - Mindful Breaks",
    page_icon="🌻",
    layout="centered",
    initial_sidebar_state="collapsed"
)

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

# Initialize session state
if "break_active" not in st.session_state:
    st.session_state.break_active = False

if "current_mood" not in st.session_state:
    st.session_state.current_mood = None

if "goal" not in st.session_state:
    st.session_state.goal = None

# Workflow
if not st.session_state.break_active:
    st.title("Neurene - Mindful Breaks")

    # Step 1: Ask for current mood
    st.session_state.current_mood = st.selectbox(
        "How do you currently feel?",
        [
            "Stressed 😵‍💫", 
            "Anxious 😟", 
            "Sad 😢", 
            "Bored 😐", 
            "Angry 😠", 
            "Overwhelmed 😰", 
            "Tired 😴", 
            "Happy 😊", 
            "Productive 💪", 
            "Calm 😌", 
            "No answer 🤷"
        ],
        placeholder="Select your current mood",
        index=None
    )

    # Step 2: Ask for the goal of the break
    st.session_state.goal = st.selectbox(
        "What would you like to gain from your break?",
        df["Goal"].unique(),
        placeholder="Select what you'd like to achieve",
        index=None
    )

    # Start Break button
    if st.button("Start Your Break"):
        st.session_state.break_active = True


    # Show suggestions
    if st.session_state.current_mood and st.session_state.goal and st.session_state.break_active:
        st.write("Your device is now in **Do Not Disturb** mode. ⏾")
        
        st.subheader("Suggestions on how to spend your break based on your goal:")
        goal_index = df["Goal"].tolist().index(st.session_state.goal)

        activities = df.loc[goal_index, "Activity/Method"]
        descriptions = df.loc[goal_index, "Description"]

        for activity, description in zip(activities, descriptions):
            st.markdown(f"**Activity:** {activity}", unsafe_allow_html=True)
            st.write(description)


    @st.dialog("How do you feel after your break?")
    def vote(item):
        st.write(f"Select your current mood")
        reason = st.radio(
                "Choose your feeling:",
                ["😊 Happy", "😌 Calm", "😕 Neutral", "😞 Sad", "😡 Angry", "❌ No answer"],
                index=None
            )
        st.write("You currently feel: ", reason)
        if st.button("Submit"):
            st.session_state.vote = {"item": item, "reason": reason}
            st.rerun()

    if "vote" not in st.session_state:
        st.write("Are you done with your break?")
        if st.button("Yes"):
            vote("Yes")
        if st.button("No"):
            vote("No")
    else:
        f"You initally felt {st.session_state.current_mood}. Now, you feel {st.session_state.vote['reason']}"
    

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
