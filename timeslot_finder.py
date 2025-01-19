import streamlit as st
from datetime import datetime, timedelta, timezone
import urllib.parse

def generate_event_link(start, end, title):
    """
    Generates a Google Calendar event creation URL.
    """
    base_url = "https://calendar.google.com/calendar/render"
    params = {
        "action": "TEMPLATE",
        "text": title,
        "dates": f"{start.strftime('%Y%m%dT%H%M%SZ')}/{end.strftime('%Y%m%dT%H%M%SZ')}",
        "details": "Scheduled via Focus Time Finder",
        "sf": "true",
        "output": "xml"
    }
    return f"{base_url}?{urllib.parse.urlencode(params)}"

def find_new_time(events, preferred_time_slot):
    """
    Suggests a new 3-hour time slot outside the user's preferred time and existing events.
    """
    workday_start = 7
    workday_end = 20

    busy_times = []
    for event in events:
        event_start = datetime.fromisoformat(event["start"])
        event_end = datetime.fromisoformat(event["end"])
        busy_times.append((event_start, event_end))

    busy_times.sort(key=lambda x: x[0])

    time_slots = []
    for hour in range(workday_start, workday_end, 3):
        slot_start = datetime.now(timezone.utc).replace(hour=hour, minute=0, second=0, microsecond=0)
        slot_end = slot_start + timedelta(hours=3)
        time_slots.append((slot_start, slot_end))

    excluded_start = datetime.now(timezone.utc).replace(hour=preferred_time_slot[0], minute=0, second=0, microsecond=0)
    excluded_end = excluded_start + timedelta(hours=3)
    available_slots = [slot for slot in time_slots if not (slot[0] >= excluded_start and slot[1] <= excluded_end)]

    for busy_start, busy_end in busy_times:
        available_slots = [
            slot for slot in available_slots
            if not (slot[0] < busy_end and slot[1] > busy_start)
        ]

    return available_slots[0] if available_slots else None

# Mock function to get calendar events (replace with real Google API logic)
def get_calendar_events(maxresults):
    """
    Simulate fetching events. Replace with real API calls.
    """
    return [
        {"start": "2024-12-08T09:00:00Z", "end": "2024-12-08T11:00:00Z"},
        {"start": "2024-12-08T13:00:00Z", "end": "2024-12-08T14:30:00Z"},
    ]

# Streamlit UI
st.title("Focus Time Finder")

# Get user's preferred time
st.header("Select Your Preferred Time Slot")
preferred_start = st.selectbox(
    "When do you prefer to focus?",
    ["7-10 AM", "10 AM-1 PM", "1-4 PM", "4-7 PM"],
)

# Map selected slot to time range
time_slot_map = {
    "7-10 AM": (7, 10),
    "10 AM-1 PM": (10, 13),
    "1-4 PM": (13, 16),
    "4-7 PM": (16, 19),
}
preferred_time_slot = time_slot_map[preferred_start]

# Find suitable time slot
maxresults = 10
events = get_calendar_events(maxresults)
new_time_slot = find_new_time(events, preferred_time_slot)

if new_time_slot:
    start, end = new_time_slot
    suggestion_text = f"A suitable time slot is available from {start.strftime('%Y-%m-%d %H:%M')} to {end.strftime('%Y-%m-%d %H:%M')}."
    st.success(suggestion_text)
    
    # Generate a link for adding the event
    event_link = generate_event_link(start, end, "New Focus Meeting")
    st.markdown(f"[Click here to add the event to your Google Calendar]({event_link})", unsafe_allow_html=True)
else:
    st.error("No available time slot found.")
