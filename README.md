# GIF 메이커 (GIF Maker)

JPEG 이미지 시퀀스를 GIF 이미지로 변환하는 자동화 프로그램입니다.

## 설치 방법

### 방법 1: 가상 환경(venv) 사용 (권장)

가상 환경을 사용하면 프로젝트별로 독립된 Python 환경을 구성할 수 있어 의존성 충돌 문제를 방지할 수 있습니다.

1. 가상 환경 설정 스크립트 실행:

```bash
chmod +x setup_venv.sh
./setup_venv.sh
```

2. 가상 환경 활성화:

```bash
source venv/bin/activate
```

3. 가상 환경 비활성화 (작업 완료 후):

```bash
deactivate
```

### 방법 2: pip를 사용하여 설치

1. 필요한 라이브러리 설치:

```bash
pip install -r requirements.txt
```

### 방법 3: pip가 없는 경우

1. pip 설치하기:

```bash
./install_pip.sh
```

2. 설치 후 필요한 라이브러리 설치:

```bash
python3 -m pip install -r requirements.txt
```

### 방법 4: Homebrew를 사용하여 pip 없이 설치

1. 제공된 스크립트 실행:

```bash
./install_without_pip.sh
```

## 사용 방법

### 단일 GIF 생성

기본 사용법:

```bash
python3 gif_maker.py 입력_디렉토리 출력파일.gif
```

가상 환경 사용 시:

```bash
# 가상 환경 활성화 후
python gif_maker.py 입력_디렉토리 출력파일.gif
```

### 배치 처리 (여러 폴더 일괄 처리)

여러 하위 폴더의 이미지 시퀀스를 한 번에 처리하려면:

```bash
python3 batch_gif_maker.py 기본_디렉토리
```

가상 환경 사용 시:

```bash
# 가상 환경 활성화 후
python batch_gif_maker.py 기본_디렉토리
```

예를 들어:

```bash
python batch_gif_maker.py test_images
```

이 명령은 다음과 같은 폴더 구조를 처리합니다:
- 입력: `test_images/폴더1/폴더2/sequence/시퀀스파일.jpg`
- 출력: `test_images/폴더1/폴더2.gif`

즉, 각 `sequence` 폴더의 이미지 시퀀스를 상위 폴더에 GIF로 저장합니다. 프로그램은 자동으로 모든 `sequence` 폴더를 찾아서 처리합니다.

### 옵션

두 스크립트 모두 다음 옵션을 지원합니다:

- `-d`, `--duration`: 각 프레임 사이의 시간 간격 (밀리초), 기본값: 100ms
- `-l`, `--loop`: 반복 횟수 (0은 무한 반복), 기본값: 0
- `-q`, `--quality`: 이미지 품질 (1-100), 기본값: 100
- `-r`, `--resize`: 이미지 크기 조정 (예: 640x480)

### 사용 예시

1. 기본 설정으로 GIF 생성:
```bash
python gif_maker.py ./이미지폴더 output.gif  # 가상 환경 사용 시
```

2. 프레임 간격 및 크기 조정:
```bash
python gif_maker.py ./이미지폴더 output.gif -d 200 -r 800x600  # 가상 환경 사용 시
```

3. 반복 횟수 설정 (1회만 재생):
```bash
python gif_maker.py ./이미지폴더 output.gif -l 1  # 가상 환경 사용 시
```

4. 여러 폴더 일괄 처리 (배치 처리):
```bash
python batch_gif_maker.py test_images -d 200 -r 800x600  # 가상 환경 사용 시
```

## Git 저장소 설정 및 사용

프로젝트를 Git으로 관리하려면 다음 단계를 따르세요:

### 1. Git 저장소 설정

제공된 스크립트를 사용하여 Git 저장소를 설정할 수 있습니다:

```bash
chmod +x setup_git.sh
./setup_git.sh
```

이 스크립트는 다음 작업을 수행합니다:
- Git 저장소 초기화
- 적절한 `.gitignore` 파일 생성
- Git 사용자 정보 설정 및 커밋 방법 안내

### 2. 수동으로 Git 설정하기

1. Git 저장소 초기화:
```bash
git init
```

2. Git 사용자 정보 설정:
```bash
git config --global user.name "사용자 이름"
git config --global user.email "이메일 주소"
```

3. 파일 추가 및 커밋:
```bash
git add .
git commit -m "초기 커밋: GIF 메이커 프로그램 추가"
```

4. 원격 저장소 연결 (GitHub 등):
```bash
git remote add origin <원격 저장소 URL>
git push -u origin main
```

## 주의사항

- 입력 디렉토리에는 JPEG 이미지 파일(.jpg, .jpeg)만 처리됩니다.
- 이미지 파일은 파일명을 기준으로 자연스럽게 정렬됩니다 (예: 1.jpg, 2.jpg, ... 10.jpg).
- 이미지 크기가 크거나 수가 많을 경우 처리 시간이 오래 걸릴 수 있습니다.
- 배치 처리는 `sequence`라는 이름의 폴더를 자동으로 찾아서 처리합니다.
- 폴더 구조는 `test_images/폴더1/폴더2/sequence/이미지.jpg` 형태여야 합니다.

## 문제 해결

- Python이나 pip가 설치되어 있지 않은 경우, 제공된 `install_pip.sh` 또는 `install_without_pip.sh` 스크립트를 실행하세요.
- macOS에서는 `python` 대신 `python3` 명령어를 사용해야 할 수 있습니다.
- 배치 처리 시 `sequence` 폴더를 찾을 수 없다는 오류가 발생하면 폴더 구조를 확인하세요.
- 가상 환경 활성화 후에는 `python` 명령어를 사용하세요 (python3 대신).

## 라이선스

MIT 