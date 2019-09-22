import smtplib
import os
from email.mime.text import MIMEText
from datetime import date

def send_mail(success, body):
  print('메일 전송을 시작합니다.')
  
  GMAIL_USER = os.getenv('GMAIL_USER')
  GMAIL_PASSWORD = os.getenv('GMAIL_PASSWORD')
  MAIL_TO = os.getenv('MAIL_TO')

  msg = MIMEText(body)
  msg['Subject'] = f"[{date.today()}] 환율 스크래핑 {'성공' if success else '실패'}"

  server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
  server.login(GMAIL_USER, GMAIL_PASSWORD)
  server.sendmail(GMAIL_USER, MAIL_TO, msg.as_string())
  server.quit()

  print('메일 전송이 완료되었습니다.')