import os
from gdoctools import Document
from google.auth import exceptions
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

def authenticate_gdoctools():
    try:
        creds = None
        token_path = 'gdoctools_token.json'

        if os.path.exists(token_path):
            creds = Credentials.from_authorized_user_file(token_path)

        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'credentials.json',
                    ['https://www.googleapis.com/auth/documents.readonly']
                )
                creds = flow.run_local_server(port=8080)
            with open(token_path, 'w') as token:
                token.write(creds.to_json())

        return creds

    except exceptions.GoogleAuthError as e:
        print(f"Google Authentication Error: {e}")
        return None

def read_google_docs_content(*file_ids):
    creds = authenticate_gdoctools()

    if creds:
        for file_id in file_ids:
            try:
                doc = Document.from_drive(file_id, credentials=creds)
                content = doc.get_text()
                print(f"Content of the Google Docs file (ID: {file_id}):\n{content}")
            except Exception as e:
                print(f"Error reading Google Docs file (ID: {file_id}): {str(e)}")
