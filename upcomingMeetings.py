import os
from dotenv import load_dotenv
from datetime import datetime, timedelta, timezone
from googleapiclient.discovery import build
from dateutil.rrule import rrulestr
from dateutil.parser import parse as parse_datetime
import pytz
import os
from dotenv import load_dotenv
from datetime import datetime, timedelta
from googleapiclient.discovery import build

# Load variables from the .env file
load_dotenv()

# Access the variables
SECRET_API_KEY = os.getenv("SECRET_API_KEY")
SECRET_CALENDAR_ID = os.getenv("SECRET_CALENDAR_ID")
DEBUG = os.getenv("DEBUG")

# Check if environment variables are undefined
if SECRET_API_KEY is None or SECRET_CALENDAR_ID is None:
    raise ValueError("SECRET_API_KEY or SECRET_CALENDAR_ID environment variable is not defined.")

# Use environment variables for API key and calendar ID
api_key = SECRET_API_KEY
calendar_id = SECRET_CALENDAR_ID

# Build the Google Calendar service
service = build('calendar', 'v3', developerKey=api_key)

# Set your calendar timezone
calendar_timezone = "America/Los_Angeles"

# Get current datetime in UTC
now = datetime.now(timezone.utc).isoformat()  # 'Z' indicates UTC time

# Calculate end date (two weeks from now)
end_date = (datetime.now(timezone.utc) + timedelta(days=14)).isoformat()  # 'Z' indicates UTC time

# Retrieve events from the calendar
events_result = service.events().list(
    calendarId=calendar_id,
    timeMin=now,
    timeMax=end_date,
    singleEvents=True,
    orderBy='startTime'
).execute()

# Define the is_all_day_event function
def is_all_day_event(event):
    start = event['start']
    end = event['end']
    return 'date' in start and 'date' in end

# Filter out all-day events from the list of events
events = events_result.get('items', [])
filtered_events = [event for event in events if not is_all_day_event(event)]

# Process and print events
if not filtered_events:
    print('No upcoming events found.')
else:
    print('Upcoming events:')
    for event in filtered_events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        start_time = datetime.fromisoformat(start)
        end = event['end'].get('dateTime', event['end'].get('date'))
        end_time = datetime.fromisoformat(end)
        duration = end_time - start_time
        event_title = ('summary','No Title')

# Define functions outside the loop
def extract_student_name(event_title):
    if "Tutoring Availability (" in event_title:
        name = event_title.split("Tutoring Availability (")[1].strip()
        if ")" in name:
            name = name.split(")")[0].strip()
    elif "Tutoring" in event_title:
        name = event_title.split(" Tutoring")[0].strip()
    else:
        name = event_title.strip()
    return name

def clean_event_title(event_title):
    if "Tutoring Availability (" in event_title:
        cleaned_title = event_title.split("Tutoring Availability (")[1].strip()
        if ")" in cleaned_title:
            cleaned_title = cleaned_title.split(")")[0].strip()
    elif "Tutoring" in event_title:
        cleaned_title = event_title.split(" Tutoring")[0].strip()
    else:
        cleaned_title = event_title.strip()
    return cleaned_title

# Create lists to store student names outside the loop
student_names = []
unique_student_names = []

while True:
    # Iterate through filtered sessions and extract student names from event titles
    for event in filtered_events:
        event_title = event.get('summary', '').strip()  # Use 'summary' key to get event title
        # Extract student name from the event title
        name = extract_student_name(event_title)
        # Append the student name to the list
        student_names.append(name)

    # Get unique student names
    unique_student_names = list(set(student_names))

    break

# Prompt user to select a student
for i, name in enumerate(unique_student_names, 1):
    print(f"{i}. {name}")

# Get user input for selected student
while True:
    try:
        selected_index = int(input("Enter the number of the student: "))
        if 1 <= selected_index <= len(unique_student_names):
            break
        else:
            print("Please enter a valid number.")
    except ValueError:
        print("Please enter a valid number.")

# Get the selected student's name
selected_student_name = unique_student_names[selected_index - 1]

# Filter events to include only those with the selected student's name in the summary
filtered_events = [event for event in events if selected_student_name in event['summary']]

# Print details of filtered events
if not filtered_events:
    print(f"No events found for {selected_student_name}.")
else:
    print(f"Events for {selected_student_name}:")
    for event in filtered_events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        start_time = datetime.fromisoformat(start)
        end = event['end'].get('dateTime', event['end'].get('date'))
        end_time = datetime.fromisoformat(end)
        duration = end_time - start_time

        # Format start and end dates
        start_date_formatted = start_time.strftime('%A %m/%d/%y')
        end_date_formatted = end_time.strftime('%A %m/%d/%y')

        # Convert start and end times to AM/PM format
        start_time_formatted = start_time.strftime('%I:%M %p')
        end_time_formatted = end_time.strftime('%I:%M %p')

        print('Event Date:', start_date_formatted)
        print('Start Time:', start_time_formatted)
        print('End Time:', end_time_formatted)
        print('Duration:', duration)
        print()