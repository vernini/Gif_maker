#!/bin/bash

echo "pip 없이 Pillow 설치를 시도합니다..."

# Homebrew가 설치되어 있는지 확인
if command -v brew &> /dev/null; then
    echo "Homebrew가 설치되어 있습니다. Pillow 의존성을 설치합니다..."
    brew install libjpeg libtiff little-cms2 openjpeg webp
    
    # Python3 설치 확인 및 설치
    if ! command -v python3 &> /dev/null; then
        echo "Python3를 설치합니다..."
        brew install python3
    fi
    
    # Pillow 소스 다운로드 및 설치
    echo "Pillow 소스를 다운로드하고 설치합니다..."
    curl -L https://github.com/python-pillow/Pillow/archive/10.1.0.tar.gz -o Pillow-10.1.0.tar.gz
    tar -xzf Pillow-10.1.0.tar.gz
    cd Pillow-10.1.0
    python3 setup.py install --user
    cd ..
    rm -rf Pillow-10.1.0 Pillow-10.1.0.tar.gz
    
    echo "Pillow 설치가 완료되었습니다."
else
    echo "Homebrew가 설치되어 있지 않습니다."
    echo "Homebrew를 설치하려면 다음 명령어를 실행하세요:"
    echo '/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"'
    echo "그 후 이 스크립트를 다시 실행하세요."
fi

echo "이제 다음 명령어로 GIF 메이커를 실행할 수 있습니다:"
echo "python3 gif_maker.py 입력_디렉토리 출력파일.gif" 