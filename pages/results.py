import streamlit as st
import datetime
import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

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

    st.write(f"Your ideal BrainBreak would last {st.session_state.break_duration}. And would be scheduled after {st.session_state.productivity_time}.")
    st.write("Your meetings for today are shown below:")

    maxresults = 4 # You can change this as needed
    events = get_calendar_events(maxresults)
    html_output = render_events_to_html(events)
    st.markdown(html_output, 
            unsafe_allow_html=True,
            )
    
    

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



# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/calendar.readonly"]

def get_calendar_events(maxresults):
    """
    Fetches the upcoming calendar events from the Google Calendar API and returns them.
    
    Args:
        maxresults (int): The maximum number of results to fetch.
    
    Returns:
        list of dict: A list of events with start time and summary.
    """
    creds = None
    
    # Authentication
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

        # Call the Calendar API
        now = datetime.datetime.utcnow().isoformat() + "Z"  # 'Z' indicates UTC time
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

        # Prepare event data
        event_list = []
        for event in events:
            start = event["start"].get("dateTime", event["start"].get("date"))
            end = event["end"].get("dateTime", event["end"].get("date"))
            event_list.append({"start": start, "end":end, "summary": event["summary"]})

        return event_list

    except HttpError as error:
        print(f"An error occurred: {error}")
        return []

def render_events_to_html(events):
    """
    Renders events in an HTML calendar format.
    
    Args:
        events (list of dict): A list of events with start time and summary.
    
    Returns:
        str: HTML string containing the events.
    """
    if not events:
        return "<p>No upcoming events found.</p>"

    html = "<table border='1' style='width:100%;border-collapse:collapse;'>"
    html += "<tr><th>Start Time</th><th>Event</th></tr>"
    for event in events:
        html += f"<tr><td>{event['start']}</td><td>{event['end']}</td><td>{event['summary']}</td></tr>"
    html += "</table>"

    return html

# Example usage

    

if __name__ == "__main__":
    main()