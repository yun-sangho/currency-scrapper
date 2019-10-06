import smtplib
from email.mime.text import MIMEText
from datetime import date

def send_mail(success, body):
  print('메일 전송을 시작합니다.')

  msg = MIMEText(body)
  msg['Subject'] = f"[{date.today()}] 환율 스크래핑 {'성공' if success else '실패'}"

  server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
  server.login('gilgil3489@gmail.com', 'dbstkdgh1%')
  server.sendmail('gilgil3489@gmail.com', 'gilgil3489@gmail.com', msg.as_string())
  server.quit()

  print('메일 전송이 완료되었습니다.')

if __name__ == '__main__':
  send_mail(False, 'ㅂㅗ로로롤')