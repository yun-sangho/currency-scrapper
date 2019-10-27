# Currency Scrapper

python 3.7 버전을 기준으로 작업했습니다.

## Getting Started

### Configure

1. `credential.sample.json` 파일에 필요한 정보를 채우고 `credential.json`으로 파일이름을 변경합니다.

### Download Serverless-chrominum

```
$ mkdir -p bin/
$ curl -SL https://github.com/adieuadieu/serverless-chrome/releases/download/v1.0.0-37/stable-headless-chromium-amazonlinux-2017-03.zip > headless-chromium.zip
$ unzip headless-chromium.zip -d bin/
$ rm headless-chromium.zip
```

### Download chromedriver

```
$ curl -SL https://chromedriver.storage.googleapis.com/2.37/chromedriver_linux64.zip > chromedriver.zip
$ unzip chromedriver.zip -d bin/
$ rm chromedriver.zip
```

### Docker build

```
$ docker build -t currency-scrapper-lambda .
$ docker run -v ${pwd -W}:/var/task currency-scrapper-lambda
```

### AWS configure

**aws cli**를 설치합니다.

```
$ pip install awscli
```

configure 명령어로 aws cli 사용에 필요한 정보를 입력합니다.

```
$ aws configure

aws_access_key_id = YOUR_ACCESS_KEY_ID
aws_secret_access_key = YOUR_SECRET_ACCESS_KEY
region = YOUR_REGION
```

### Deploy Function

```
$ aws s3 cp deploy_package.zip s3://YOUR_BUCKET_NAME
$ aws lambda create-function --region YOUR_REGION --function-name YOUR_FUNCTION_NAME --runtime python3.7 --role YOUR_ROLE_NAME --code S3Bucket=YOUR_BUCKET_NAME,S3Key=deploy_package.zip --handler handler.start_app
```

### Update Function

```
$ aws s3 sync deploy_package.zip s3://YOUR_BUCKET_NAME
$ aws lambda update-function-code --function-name YOUR_FUNCTION_NAME --s3-bucket YOUR_BUCKET_NAME --s3-key deploy_package.zip
```
