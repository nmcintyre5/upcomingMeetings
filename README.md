# Upcoming Meeting Generator
[Overview](#overview) | [Key Features](#key-features) | [How to Install](#how-to-install)
## Overview

The Upcoming Appointments Tracker is a Python script that retrieves and displays upcoming appointments from a Google Calendar. It filters out all-day events and allows users to select a unique client to view their specific appointments. It is useful for business owners with recurring client meetings, such as therapists or consultants, as it simplifies the process of tracking and managing client appointments. By retrieving and displaying upcoming appointments from a Google Calendar, it provides a convenient overview of scheduled meetings, helping business owners stay organized and effectively manage their time.

## Key Features

   - Retrieves upcoming appointments for the next two weeks from Google Calendar API.
   - Filters out all-day events.
   - Allows users to select a client from a list and view their upcoming appointments.
   - Displays appointment details including date, start time, end time, and duration.

## How to Install
### Prerequisites

1. **Python 3**: Ensure you have Python 3 installed on your system. You can check the Python version by running `python --version` in the command line.

2. **Dependencies**:
   - `google-api-python-client` library
   - `pytz` library

3. **Google Calendar API key**:
   - Generate an API key from the Google Cloud Console. Follow the instructions in the [Google Calendar API documentation](https://support.google.com/googleapi/answer/6158862?hl=en) to obtain API key.
   
4. **Google Calendar ID**:
   - Obtain the Google Calendar ID by logging in to Google Calendar and navigating to the calendar settings. The Calendar ID is displayed under "Calendar ID" in the settings.

## Installation

1. Install the required libraries using pip:
   ```bash
    pip install google-api-python-client pytz
   ```
2. Obtain Google Calendar API credentials and an API key by following the instructions in the Google Calendar API documentation.

3. Ensure the Google Calendar is available to the public. Enable the "Make available to public" option in the calendar settings.

4. Create a .env file in the project directory based on the provided .envtemplate file. Replace the placeholders for api_key and calendar_id with your actual API key and calendar IDs.
```bash
makefile

    SECRET_API_KEY=your_google_api_key
    SECRET_CALENDAR_ID=your_google_calendar_id
 ```
## Usage

1. Run the script.
   ```bash
   python upcomingAppointments.py
    ```
2. Select a client from the displayed list.
3. View the client's upcoming appointments.
