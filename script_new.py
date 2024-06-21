import base64
import pandas as pd
import os
from email.mime.text import MIMEText
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from requests import HTTPError


SCOPES = [
        "https://www.googleapis.com/auth/gmail.send"
    ]
flow = InstalledAppFlow.from_client_secrets_file(
            'credentials.json', SCOPES)
creds = flow.run_local_server(port=0)
service = build('gmail', 'v1', credentials=creds)
from_email = '<EMAIL_SENDER@gmail.com>'

# Email content
subject = '<EMAIL_CONTENT>'

# Read the HTML template


# Read the Excel file
file_path = '<EXCEL_FILE>.xlsx'  # Path to your Excel file
contacts = pd.read_excel(file_path)




for index, row in contacts.iterrows():
    to_name = row['Name']
    to_email = row['Email']
    with open('<PATH_TO_EMAIL_BODY_TEMPLATE>.html', 'r') as file:
        html_template = file.read().replace('{name}', to_name)
    html_message = MIMEText(html_template, 'html')
    html_message['To'] = to_email
    html_message['Subject'] = subject
    html_message['From'] = from_email

    create_message = {'raw': base64.urlsafe_b64encode(html_message.as_bytes()).decode()}

    try:
        message = (service.users().messages().send(userId=from_email, body=create_message).execute())
        print(F'sent message to {message} Message Id: {message["id"]}')
    except HTTPError as error:
        print(F'An error occurred: {error}')
        message = None










