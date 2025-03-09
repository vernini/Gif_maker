#!/bin/bash

echo "Git 저장소 설정을 시작합니다..."

# Git이 설치되어 있는지 확인
if ! command -v git &> /dev/null; then
    echo "Git이 설치되어 있지 않습니다."
    echo "Git을 먼저 설치해주세요."
    exit 1
fi

# Git 저장소 초기화
if [ ! -d ".git" ]; then
    echo "Git 저장소를 초기화합니다..."
    git init
    echo "Git 저장소가 초기화되었습니다."
else
    echo "이미 Git 저장소가 초기화되어 있습니다."
fi

# .gitignore 파일 생성
echo "Git 무시 파일(.gitignore)을 생성합니다..."
cat > .gitignore << EOL
# Python 가상 환경
venv/
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
env/
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
*.egg-info/
.installed.cfg
*.egg

# 테스트 이미지 및 출력 파일
test_images/**/*.jpg
test_images/**/*.jpeg
test_images/**/*.JPG
test_images/**/*.JPEG
*.gif

# 맥OS 시스템 파일
.DS_Store
.AppleDouble
.LSOverride
._*

# 윈도우 시스템 파일
Thumbs.db
ehthumbs.db
Desktop.ini
EOL

echo ".gitignore 파일이 생성되었습니다."

# Git 사용자 정보 설정 안내
echo ""
echo "Git 사용자 정보를 설정하세요 (아직 설정하지 않은 경우):"
echo "git config --global user.name \"사용자 이름\""
echo "git config --global user.email \"이메일 주소\""
echo ""

# 파일 추가 및 커밋 안내
echo "다음 명령어로 파일을 추가하고 커밋하세요:"
echo "git add ."
echo "git commit -m \"초기 커밋: GIF 메이커 프로그램 추가\""
echo ""

# 원격 저장소 연결 안내
echo "GitHub 또는 다른 Git 호스팅 서비스에 저장소를 생성한 후,"
echo "다음 명령어로 원격 저장소를 연결하세요:"
echo "git remote add origin <원격 저장소 URL>"
echo "git push -u origin main"
echo ""

echo "Git 저장소 설정이 완료되었습니다!" 