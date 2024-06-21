# Mail Campaign Gun

A python script to send out emails (HTML mime) to a collection of contacts in an Excel Sheet from an Organisation Email Account in Google Workspace.
The script utilises the Gmail API available over Oauth Authentication libraries exposed by google.

## Prerequisites

Google Workspace Admin
Google Project creation for the account (Sender)
Google GMAIL API scoped credentials creation from the Google Project.

HTML with the formatted body and content 
Excel Sheet with two columns (Mandatory) `Name` and `Email` case-sensitive. (Name should be first name)


## Install

- create a virtual env
- install required packages with `-r requirements.txt`
- store credentials.json from google in a json file `credentials.json`
- Update the name of the excel Sheet in the script
- Update the subject and sender details in the script
- Activate the virtual env
- Run the script.


