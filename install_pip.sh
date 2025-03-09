#!/bin/bash

echo "pip 설치 스크립트를 실행합니다..."

# get-pip.py 다운로드
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py

# Python으로 get-pip.py 실행
python3 get-pip.py

# 설치 확인
python3 -m pip --version

echo "pip 설치가 완료되었습니다."
echo "이제 다음 명령어로 필요한 라이브러리를 설치할 수 있습니다:"
echo "python3 -m pip install -r requirements.txt" 