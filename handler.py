from scrapper import run_scrapper
from sheet import insert_data
from mailer import send_mail

def start_app(event, context):
  print('App 작동 시작합니다.')

  try:
    data = run_scrapper()

    if not data:
      raise Exception('새로운 환율이 개시되지 않았습니다.')

    insert_data(data)

    body = f"스크래핑이 성공하였습니다.\n아래 링크에서 결과를 확인해보세요.\nhttps://docs.google.com/spreadsheets/d/1Q9Fa1zF6Yo7NQHrt4rwe7fAUyw9akarzCfV0fyu44PY/edit#gid=793018437"
    # send_mail(True, body)
  except Exception as e:
    print(e)
    body = f"스크래핑 중 에러가 발생했습니다. {str(e)}"
    # send_mail(False, body)

if __name__ == '__main__':
  start_app(None,None)