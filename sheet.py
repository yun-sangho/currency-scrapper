from oauth2client.service_account import ServiceAccountCredentials
import gspread

SCOPES = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

def insert_data(data):
  print('시트 입력을 시작합니다.')

  credentials = ServiceAccountCredentials.from_json_keyfile_name('credential.json', SCOPES)

  client = gspread.authorize(credentials)

  sheet = client.open_by_key('1Q9Fa1zF6Yo7NQHrt4rwe7fAUyw9akarzCfV0fyu44PY').worksheet('환율크롤링')

  for row in data:
    sheet.append_row(row)
  
  print('시트 입력이 완료되었습니다.')

  