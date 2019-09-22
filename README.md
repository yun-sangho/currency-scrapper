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

### Install ChromeDriver

**Selenium**을 사용해 Chrome 브라우저를 조작하기 위해서 우선 ChromeDriver를 설치해야합니다.
[https://chromedriver.chromium.org/downloads](설치링크)에서 자신의 Chrome 브라우저 버전에 맞는 Chrome Driver를 설치(자신의 크롬 브라우저가 76 버전이라면 Driver도 76 버전을 설치합니다.)하고 설치 경로를 `.env` 파일에 입력합니다.

```
# scrapper.py
CHROME_DRIVER_PATH=이 곳에 크롬 드라이버 경로를 입력합니다.
```

### Run app

`python3 handler.py` 명령어를 입력하세요.
