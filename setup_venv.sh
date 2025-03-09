#!/bin/bash

echo "Python 가상 환경(venv) 설정을 시작합니다..."

# 가상 환경 디렉토리 이름
VENV_DIR="venv"

# Python3 설치 확인
if ! command -v python3 &> /dev/null; then
    echo "Python3가 설치되어 있지 않습니다."
    echo "Python3를 먼저 설치해주세요."
    exit 1
fi

# 가상 환경 생성
echo "가상 환경을 생성합니다: $VENV_DIR"
python3 -m venv $VENV_DIR

# 가상 환경 활성화 및 패키지 설치
echo "가상 환경을 활성화하고 필요한 패키지를 설치합니다..."
source $VENV_DIR/bin/activate
pip install --upgrade pip
pip install -r requirements.txt

echo ""
echo "가상 환경 설정이 완료되었습니다!"
echo ""
echo "가상 환경을 활성화하려면 다음 명령어를 실행하세요:"
echo "source $VENV_DIR/bin/activate"
echo ""
echo "가상 환경에서 GIF 메이커를 실행하려면:"
echo "1. 가상 환경 활성화: source $VENV_DIR/bin/activate"
echo "2. 단일 GIF 생성: python gif_maker.py 입력_디렉토리 출력파일.gif"
echo "3. 배치 처리: python batch_gif_maker.py test_images"
echo ""
echo "가상 환경을 비활성화하려면 다음 명령어를 실행하세요:"
echo "deactivate" 