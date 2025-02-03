import streamlit as st
import pandas as pd
import random
import matplotlib.pyplot as plt
import datetime
import calendar

st.set_page_config(
    page_title="Neurene - Analytics",
    page_icon="📊",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# Sidebar with grouped pages
st.sidebar.title("Navigation")

# Group 1: General Information
with st.sidebar.expander("📋 Products"):
    if st.button("Getting Started"):
        st.switch_page("pages/onboarding.py")
    if st.button("Start a Brain Break"):
        st.query_params("pages/brainbreak.py")
    

with st.sidebar.expander("🔒 User Tools"):
    if st.button("Logout"):
        st.switch_page("home.py")
    if st.button("FAQ"):
        st.switch_page("pages/faq.py")

# Header
st.title("Neurene - Your Brain Break Analytics")
st.subheader("Track your mindful breaks and mood changes over time.")

# Generate past month data (weekdays only, random mood before and after)
dates = pd.date_range(end=datetime.date.today(), periods=30, freq='B')

mood_options = ["😵‍💫 Stressed", "😟 Anxious", "😢 Sad", "😐 Bored", "😠 Angry", "😰 Overwhelmed", "😴 Tired", "😊 Happy", "💪 Productive", "😌 Calm"]
data = []


for date in dates:
    if random.random() > 0.1:  # 90% chance that a break was taken
        mood_before = random.choice(mood_options[:7])  # More negative moods
        mood_after = random.choice(mood_options[5:]) if random.random() > 0.7 else mood_before  # Mostly improved
        data.append([date, mood_before, mood_after, "✅"])
    else:
        data.append([date, None, None, "❌"])

# Append today's data from session state
if "current_mood" in st.session_state and "post_mood" in st.session_state:
    today = datetime.date.today()
    data.append([today, st.session_state.current_mood, st.session_state.post_mood, "✅"])

df = pd.DataFrame(data, columns=["Date", "Mood Before", "Mood After", "Break Taken"])

# Convert 'Date' column to datetime just in case it's not
df["Date"] = pd.to_datetime(df["Date"])

# Create Calendar View
st.subheader("📅 Brain Break Calendar")

# Create a list of weekdays for the calendar header
weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
cal_df = pd.DataFrame(columns=weekdays)

# Populate the calendar rows
weeks = []
for i in range(0, len(df), 5):  # Step by 5 to get weekly data
    week_data = []
    for j in range(5):  # Loop through weekdays
        if i + j < len(df):  # If there is data for this day
            day_data = df.iloc[i + j]
            mood_emoji = day_data['Mood After'] if day_data['Mood After'] else "❓"
            break_taken = day_data['Break Taken']
            date_str = day_data['Date'].strftime('%Y-%m-%d')  # Format date as 'YYYY-MM-DD'
            week_data.append(f"{date_str} \n {break_taken}")
        else:
            week_data.append("")  # Empty field for missing data
    weeks.append(week_data)

# Add the weeks data to the DataFrame
cal_df = pd.DataFrame(weeks, columns=weekdays)

# Style the calendar: Color the "✅" and "❌" fields
def style_calendar(val):
    if val == "✅":
        return 'background-color: lightgreen'
    elif val == "❌":
        return 'background-color: lightcoral'
    return ''

st.dataframe(cal_df.style.applymap(style_calendar))


# Mood Analysis Chart
st.subheader("📊 Mood Trends")
fig, ax = plt.subplots(figsize=(10, 4))

# Ensure 'Date' is in datetime format for plotting
dates = pd.to_datetime(df["Date"])
moods_before = [mood_options.index(m) if m in mood_options else None for m in df["Mood Before"]]
moods_after = [mood_options.index(m) if m in mood_options else None for m in df["Mood After"]]

ax.plot(dates, moods_before, marker='o', label="Before Break", linestyle='dashed', color='red')
ax.plot(dates, moods_after, marker='o', label="After Break", linestyle='solid', color='lightblue')
ax.set_yticks(range(len(mood_options)))
ax.set_yticklabels(mood_options)
plt.xticks(rotation=45)
plt.legend()
st.pyplot(fig)

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
