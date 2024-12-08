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
    initial_sidebar_state="collapsed"
)

SCOPES = ["https://www.googleapis.com/auth/calendar.readonly", "https://www.googleapis.com/auth/calendar.events"]

def main():
    st.markdown(
        """
        <h1 style='text-align: center; font-family: Arial, sans-serif;'>Welcome to Your Results</h1>
        """,
        unsafe_allow_html=True,
    )    

    st.write(f"Your ideal BrainBreak would last {st.session_state.break_duration}. And would be scheduled after {st.session_state.productivity_time}.")
    st.write("Your meetings for today are shown below:")

    maxresults = 4
    events = get_calendar_events(maxresults)
    html_output = render_events_to_html(events)
    st.markdown(html_output, unsafe_allow_html=True)
    
    st.write(f"Your ideal BrainBreak for today would be scheduled at 2.30 pm and would last {st.session_state.break_duration}.")

    if st.button("Add BrainBreak to your calendar"):
        now = datetime.datetime.utcnow()
        start_time = datetime.datetime(year=now.year, month=now.month, day=now.day) + datetime.timedelta(days=1, hours= 13, minutes=30)
        print("Start Time:", start_time)
        end_time = start_time + datetime.timedelta(minutes=10)
        summary = "BrainBreak"
        
        result = create_calendar_event(summary, start_time, end_time)
        st.write(result)

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
