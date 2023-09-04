from flask import Flask, render_template, request
import boto3
import json

# AWS 계정 정보 및 버킷 이름 설정
aws_access_key = ''
aws_secret_key = ''
bucket_name = ''
file_key = ''  # 파일의 경로 및 이름

# AWS S3 클라이언트 생성
s3 = boto3.client(
    's3',
    aws_access_key_id=aws_access_key,
    aws_secret_access_key=aws_secret_key
)

# Flask 애플리케이션 생성
app = Flask(__name__)

@app.route("/")
def hello():
    try:
        response = s3.get_object(Bucket=bucket_name, Key=file_key)
        content = response['Body'].read().decode('utf-8')  # 파일 내용 읽어오기

        # 파일 내용 출력
        print("File Contents:")
        print(content)

        # 읽어온 값에 따라 조건문 실행
        value = int(content.strip())  # 문자열로 읽어온 값을 정수로 변환
        if value == 0:
            return render_template('index.html', value=value)
        elif value == 1:
            return render_template('report.html')

    except Exception as e:
        return "Error reading file: {}".format(e)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
