from oauth2client.service_account import ServiceAccountCredentials
import gspread
import os

SCOPES = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

def insert_data(data):
  print('시트 입력을 시작합니다.')
  
  SHEET_ID = os.getenv('SHEET_ID')
  WORKSHEET_TITLE = os.getenv('WORKSHEET_TITLE')

  credentials = ServiceAccountCredentials.from_json_keyfile_name('credential.json', SCOPES)

  client = gspread.authorize(credentials)

  sheet = client.open_by_key(SHEET_ID).worksheet(WORKSHEET_TITLE)

  for row in data:
    sheet.append_row(row)
  
  print('시트 입력이 완료되었습니다.')

  