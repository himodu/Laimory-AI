# Laimory-AI

Laimory AI 서버 프로젝트입니다.
FastAPI 기반으로 구성되어 있으며, Python 의존성 관리는 `uv`를 사용합니다.

## 개발 환경

* Python 3.14
* FastAPI
* Uvicorn
* uv
* PyCharm

## 프로젝트 실행 구조

```text
Laimory-AI/
├─ app/
│  ├─ __init__.py
│  └─ main.py
├─ .venv/
├─ .env
├─ .python-version
├─ pyproject.toml
├─ uv.lock
└─ README.md
```

## uv 설치 경로

Windows 기준 uv 실행 파일 위치:

```text
C:\Users\이동건\.local\bin\uv.exe
```

터미널에서 `uv` 명령어가 인식되지 않을 경우, 절대경로로 실행합니다.

```powershell
C:\Users\이동건\.local\bin\uv.exe --version
```

## 의존성 설치

`pyproject.toml`에 정의된 의존성을 설치합니다.

```powershell
C:\Users\이동건\.local\bin\uv.exe sync
```

## 의존성 추가

새 패키지를 추가할 때는 다음 명령어를 사용합니다.

```powershell
C:\Users\이동건\.local\bin\uv.exe add 패키지명
```

예시:

```powershell
C:\Users\이동건\.local\bin\uv.exe add python-dotenv
C:\Users\이동건\.local\bin\uv.exe add rich
```

이 명령어를 실행하면 `pyproject.toml`과 `uv.lock`이 함께 갱신됩니다.

## 서버 실행

터미널에서 직접 실행할 경우:

```powershell
C:\Users\이동건\.local\bin\uv.exe run uvicorn app.main:app --reload
```

실행 후 아래 주소에서 확인할 수 있습니다.

```text
http://127.0.0.1:8000/health
http://127.0.0.1:8000/docs
```

## PyCharm 원클릭 실행 설정

PyCharm에서 Run Configuration을 생성합니다.

```text
Run → Edit Configurations... → + → Python
```

설정값:

```text
Name: FastAPI
Script path:
C:\Users\이동건\Desktop\GitRepositories\Laimory-AI\.venv\Scripts\uvicorn.exe

Parameters:
app.main:app --reload

Working directory:
C:\Users\이동건\Desktop\GitRepositories\Laimory-AI

Python interpreter:
C:\Users\이동건\Desktop\GitRepositories\Laimory-AI\.venv\Scripts\python.exe
```

## 실행 전 uv sync 자동 실행 설정

PyCharm Run Configuration의 `Before launch`에 External Tool을 추가합니다.

```text
Before launch → + → Run External Tool → + 
```

External Tool 설정값:

```text
Name:
uv sync

Program:
C:\Users\이동건\.local\bin\uv.exe

Arguments:
sync

Working directory:
$ProjectFileDir$
```

이렇게 설정하면 PyCharm의 실행 버튼을 누를 때마다 다음 순서로 동작합니다.

```text
1. uv sync 실행
2. FastAPI 서버 실행
```

따라서 `pyproject.toml`에 의존성을 추가한 뒤 실행 버튼을 누르면, 의존성이 자동으로 반영된 후 서버가 실행됩니다.

## 환경변수 설정

프로젝트 루트에 `.env` 파일을 생성합니다.

```env
APP_ENV=local
OPENAI_API_KEY=test-api-key
```

`main.py`에서는 `python-dotenv`를 통해 `.env` 값을 불러옵니다.

```python
from dotenv import load_dotenv

load_dotenv()
```

## 주의사항

`.env` 파일에는 API Key 등 민감 정보가 들어갈 수 있으므로 Git에 올리지 않습니다.

`.gitignore`에 다음 내용을 추가합니다.

```gitignore
.venv/
.env
__pycache__/
.idea/
```
