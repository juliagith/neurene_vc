import streamlit as st
import datetime
import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

st.set_page_config(
    page_title="Neurene - Results",
    page_icon="🫀",
    layout="centered",
    initial_sidebar_state="collapsed",
    menu_items={
         'About': "© 2024 Neurene Productivity Group GmbH. All rights reserved."
     }
)


# Sidebar with grouped pages
st.sidebar.title("Navigation")

# Group 1: General Information
with st.sidebar.expander("📋 Products"):
    if st.button("Start a Brain Break"):
        st.query_params("pages/brainbreak.py")
    if st.button("Analytics"):
        st.query_params("pages/analytics.py")
    

with st.sidebar.expander("🔒 User Tools"):
    if st.button("Logout"):
        st.switch_page("home.py")
    if st.button("FAQ"):
        st.switch_page("pages/faq.py")


SCOPES = ["https://www.googleapis.com/auth/calendar.readonly", "https://www.googleapis.com/auth/calendar.events"]


def main():
    st.markdown(
        """
        <h1 style='text-align: center; font-family: Arial, sans-serif;'>Welcome to Your Results</h1>
        """,
        unsafe_allow_html=True,
    )    

    st.write(f"Your ideal BrainBreak would last {st.session_state.break_duration}. "
             f"And it would be scheduled after {st.session_state.productivity_time}.")
    
    st.write("Your upcoming meetings are shown below:")

    max_results = 4
    events = get_calendar_events(max_results)  # Ensure this function is defined
    html_output = render_events_to_html(events)  # Ensure this function is defined

    st.markdown(html_output, unsafe_allow_html=True)

    # Check if "Brain Break" is in the event list
    if "BrainBreak" in events:
        brain_break_time = extract_brain_break_time(events)  # Function to extract the event time
        st.write(f"Your next Brain Break is already scheduled for {brain_break_time}.")
    else:
        st.write(f"Considering your preferences and your meetings for tomorrow, "
                 f"ideally a BrainBreak would be scheduled at 2:30 PM and "
                 f"would last {st.session_state.break_duration}.")


    if st.button("Add another BrainBreak to your calendar"):
        now = datetime.datetime.utcnow()
        start_time = datetime.datetime(year=now.year, month=now.month, day=now.day) + datetime.timedelta(days=1, hours= 13, minutes=30)
        print("Start Time:", start_time)
        end_time = start_time + datetime.timedelta(minutes=10)
        summary = "BrainBreak"
        
        result = create_calendar_event(summary, start_time, end_time)
        st.write(result)
        
    if st.button("Start your BrainBreak"):
            st.switch_page("pages/brainbreak.py")

    

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


# Function to extract Brain Break event time
def extract_brain_break_time(events):
    for event in events:
        if isinstance(event, dict) and "summary" in event and "BrainBreak" in event["summary"]:
            if "start" in event:
                return event["start"]  # Directly return the start time
    return "Unknown Time"



def get_calendar_events(maxresults):
    creds = None
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                "credentials.json", SCOPES
            )
            creds = flow.run_local_server(port=0)
        with open("token.json", "w") as token:
            token.write(creds.to_json())

    try:
        service = build("calendar", "v3", credentials=creds)
        now = datetime.datetime.utcnow().isoformat() + "Z"
        events_result = (
            service.events()
            .list(
                calendarId="primary",
                timeMin=now,
                maxResults=maxresults,
                singleEvents=True,
                orderBy="startTime",
            )
            .execute()
        )
        events = events_result.get("items", [])
        if not events:
            return []
        return [{"start": e["start"].get("dateTime", e["start"].get("date")), 
                 "end": e["end"].get("dateTime", e["end"].get("date")), 
                 "summary": e["summary"]} for e in events]

    except HttpError as error:
        print(f"An error occurred: {error}")
        return []

def create_calendar_event(summary, start_time, end_time):
    creds = None
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                "credentials.json", SCOPES
            )
            creds = flow.run_local_server(port=0)
        with open("token.json", "w") as token:
            token.write(creds.to_json())

    try:
        service = build("calendar", "v3", credentials=creds)
        event = {
            'summary': summary,
            'start': {
                'dateTime': start_time.isoformat(),
                'timeZone': 'UTC',
            },
            'end': {
                'dateTime': end_time.isoformat(),
                'timeZone': 'UTC',
            },
        }
        event = service.events().insert(calendarId='primary', body=event).execute()
        return f"Event created: {event.get('htmlLink')}"

    except HttpError as error:
        return f"An error occurred: {error}"

def render_events_to_html(events):
    if not events:
        return "<p>No upcoming events found.</p>"
    html = "<table border='1' style='width:100%;border-collapse:collapse;'>"
    html += "<tr><th>Start Time</th><th>Event</th></tr>"
    for event in events:
        html += f"<tr><td>{event['start']}</td><td>{event['summary']}</td></tr>"
    html += "</table>"
    return html

if __name__ == "__main__":
    main()
