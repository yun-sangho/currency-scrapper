# Currency Scrapper

python 3.7 버전을 기준으로 작업했습니다.

## Getting Started

### Configure

1. `.smaple.env` 파일에 필요한 정보를 채우고 `.env`로 파일이름을 변경합니다.
2. `credential.sample.json` 파일에 필요한 정보를 채우고 `credential.json`으로 파일이름을 변경합니다.

### Create virtualenv

##### Linux & macOs

`python3 -m venv your-env-name` 명령어로 새로운 virtual 환경을 만듭니다.
`source env/bin/activate` 명령어로 virtual 환경을 실행합니다.

##### Windows

`py -m venv your-env-name` 명령어로 새로운 virtual 환경을 만듭니다.
`.\env\Scripts\activate` 명령어로 virtual 환경을 실행합니다.

### Install Dependencies

`pip install -r requirements.txt` 명령어로 코드 실행에 필요한 pacakage들을 설치합니다.

### Run app

`python3 handler.py` 명령어를 입력하세요.
